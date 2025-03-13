import pandas as pd
import asyncio
import asyncpg

# Чтение CSV-файла
df = pd.read_csv('Тестовая таблица - Sheet1.csv')

# Придумаем названия столбцов
df.columns = ['student_name', 'source', 'order_date', 'price', 'subjects', 'course_name', 'duration', 'col8', 'col9',
              'col10', 'col11', 'col12', 'col13']

# Нормализация данных: создание справочных таблиц
courses = df[['course_name']].drop_duplicates().reset_index(drop=True)
subjects = df[['subjects']].drop_duplicates().reset_index(drop=True)

# Добавляем id для курсов и предметов
courses['course_id'] = courses.index + 1
subjects['subject_id'] = subjects.index + 1

# Объединяем с основным DataFrame
df = df.merge(courses, on='course_name', how='left')
df = df.merge(subjects, on='subjects', how='left')

# Удаляем старые столбцы
df = df.drop(columns=['course_name', 'subjects'])


# Подключение к БД
async def connect_to_db():
    return await asyncpg.connect(user='your_user', password='your_password',
                                 database='your_db', host='localhost')


# Создание таблиц в БД
async def create_tables(conn):
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            course_name TEXT
        );
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id SERIAL PRIMARY KEY,
            subject_name TEXT
        );
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            student_name TEXT,
            source TEXT,
            order_date TIMESTAMP,
            price NUMERIC,
            duration TEXT,
            course_id INT REFERENCES courses(course_id),
            subject_id INT REFERENCES subjects(subject_id)
        );
    ''')


# Загрузка данных в БД
async def load_data(conn, df):
    # Загрузка курсов
    await conn.copy_records_to_table('courses', records=courses[['course_id', 'course_name']].to_records(index=False))

    # Загрузка предметов
    await conn.copy_records_to_table('subjects', records=subjects[['subject_id', 'subjects']].to_records(index=False))

    # Загрузка заказов
    await conn.copy_records_to_table('orders', records=df[
        ['student_name', 'source', 'order_date', 'price', 'duration', 'course_id', 'subject_id']].to_records(
        index=False))


async def main():
    conn = await connect_to_db()
    await create_tables(conn)
    await load_data(conn, df)
    await conn.close()


asyncio.run(main())
