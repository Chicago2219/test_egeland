import re

# Словарь для нормализации курсов
course_mapping = {
    r'Весенний курс ЕГЭ': 'ЕГЭ',
    r'Полугодовой курс ЕГЭ': 'ЕГЭ',
    r'Спецкурс': 'Спецкурс',
    # и тд, не стал уже все перечислять
}


# Функция для нормализации курсов
def normalize_course(course_name):
    for pattern, normalized_name in course_mapping.items():
        if re.search(pattern, course_name, re.IGNORECASE):
            return normalized_name
    return 'Другой'

# Применение нормализации
df['standardized_course'] = df['course_name'].apply(normalize_course)

# Функция для нормализации предметов
def normalize_subject(subject_name):
    # Пример нормализации
    if 'Математика' in subject_name:
        return 'Математика'
    elif 'Русский язык' in subject_name:
        return 'Русский язык'
    # Добавьте другие предметы
    return 'Другой'

# Применение нормализации
df['standardized_subject'] = df['subjects'].apply(normalize_subject)

# Вывод результата
print(df[['course_name', 'standardized_course', 'subjects', 'standardized_subject']].head())
