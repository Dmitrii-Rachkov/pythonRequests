import json



"""Методы для проверки ответов наших запросов"""

class Checking():

    # Метод проверки статус кода ответа
    @staticmethod
    def check_status_code(status_code, result):
        assert status_code == result.status_code
        print(f'Запрос прошёл успешно! Статус код: {result.status_code}'.encode('utf-8'))


    # Метод для проверки наличия обязательных полей
    @staticmethod
    def check_fields(expected_fields, result):
        # Функция 'loads' модуля 'json' преобразует получаемую строку в json формат
        actual_fields = json.loads(result.text)
        assert list(actual_fields) == expected_fields
        print(f'Все обязательные поля присутствуют.'.encode('utf-8'))


    # Метод для проверки значений полей
    @staticmethod
    def check_value(expected_value, result, field_name):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Значение поля {field_name} верно.'.encode('utf-8'))



