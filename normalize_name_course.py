import re

# Словарь для нормализации курсов
course_mapping = {
    r'2 месяца годового платинум и марафон в подарок': 'Спецкурс',
    r'2 месяца годового стандарт и марафон в подарок': 'Спецкурс',
    r'2 месяца полугодового платинум и марафон в подарок': 'Спецкурс',
    r'2 месяца полугодового стандарт и марафон в подарок': 'Спецкурс',
    r'В погоне за пятеркой 2К25 стандарт': 'Весенний курс',
    r'В погоне за пятеркой 2к24': 'Весенний курс',
    r'В погоне за пятеркой 2к24 (Курс 2.0)': 'Весенний курс',
    r'В погоне за пятеркой 2к24 (полный курс 2.0)': 'Весенний курс',
    r'В погоне за пятеркой 2к24 (полный курс)': 'Весенний курс',

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
    return 'Другой'

# Применение нормализации
df['standardized_subject'] = df['subjects'].apply(normalize_subject)

# Вывод результата
print(df[['course_name', 'standardized_course', 'subjects', 'standardized_subject']].head())
