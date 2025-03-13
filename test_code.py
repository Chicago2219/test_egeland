import pytest

def test_normalize_course():
    assert normalize_course('Весенний курс ЕГЭ') == 'ЕГЭ'
    assert normalize_course('Полугодовой курс ЕГЭ') == 'ЕГЭ'
    assert normalize_course('Спецкурс') == 'Спецкурс'
    assert normalize_course('Неизвестный курс') == 'Другой'

def test_normalize_subject():
    assert normalize_subject('Математика 85+ баллов') == 'Математика'
    assert normalize_subject('Русский язык / Нормис') == 'Русский язык'
    assert normalize_subject('Неизвестный предмет') == 'Другой'

if __name__ == "__main__":
    pytest.main()