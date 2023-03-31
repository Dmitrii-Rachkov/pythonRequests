import allure
import requests
from utils.logger import Logger

"""Список http методов"""

class Http_methods():
    # Информация которая передаётся с нашими запросами и возвращается в наших ответах
    headers = {'Content-type': 'application/json'}
    # Cookie пока не требуются поэтому оставляем пустыми
    cookie = ""

    # Создаём метод GET
    # Параметр 'self', который указывает принадлежость метода к классу 'Http_methods' не передаём,
    # т.к. методу будут статичные, мы сможем их вызывать абсолютно в любом классе или тесте
    # и не будем привязываться к классу 'Http_methods'
    # Для этого необходимо указать - '@staticmethod'

    @staticmethod
    def get(url):
        with allure.step("Method GET"):
            Logger.add_request(url=url, method="GET")
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            result.encoding = 'utf-8'
            Logger.add_response(result=result)
            return result

    # Создаём метод POST
    @staticmethod
    def post(url, body):
        with allure.step("Method POST"):
            Logger.add_request(url=url, method="POST")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            result.encoding = 'utf-8'
            Logger.add_response(result=result)
            return result

    # Создаём метод PUT
    @staticmethod
    def put(url, body):
        with allure.step("Method PUT"):
            Logger.add_request(url=url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            result.encoding = 'utf-8'
            Logger.add_response(result=result)
            return result

    # Создаём метод DELETE
    @staticmethod
    def delete(url, body):
        with allure.step("Method DELETE"):
            Logger.add_request(url=url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            result.encoding = 'utf-8'
            Logger.add_response(result=result)
            return result
