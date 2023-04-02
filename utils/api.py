from utils.http_methods import Http_methods

"""Методы для тестирования google maps api"""

base_url = "https://rahulshettyacademy.com"   # Базовая URL
key = "?key=qaclick123"                       # Параметр для всех запросов


class Google_maps_api():

    """Метод для создания новой локации"""
    @staticmethod
    def create_place():

        json_create_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"   # Ресурс метода post
        post_url = base_url + post_resource + key
        comment = f'Исходная URL метода POST:\n {post_url}'
        print(comment.encode('utf-8'))
       # print(f'Исходная URL метода POST:\n {post_url}'.encode('utf-8'))
        result_post = Http_methods.post(url=post_url, body=json_create_place)
        result_post.encoding = 'utf-8'
        print(f'Ответ POST:\n{result_post.text}'.encode('utf-8'))
        return result_post


    """Метод для проверки новой локации"""

    @staticmethod
    def get_place(place_id):

        get_resource = "/maps/api/place/get/json"   # Ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(f'Исходная URL метода GET:\n {get_url}'.encode('utf-8'))
        result_get = Http_methods.get(url=get_url)
        result_get.encoding = 'utf-8'
        print(f'Ответ GET:\n{result_get.text}'.encode('utf-8'))
        return result_get


    """Метод для изменения локации"""

    @staticmethod
    def update_place(place_id):

        put_resource = "/maps/api/place/update/json"   # Ресурс метода PUT
        put_url = base_url + put_resource + key
        print(f'Исходная URL метода PUT:\n {put_url}'.encode('utf-8'))
        json_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(url=put_url, body=json_update_location)
        result_put.encoding = 'utf-8'
        print(f'Ответ PUT:\n{result_put.text}'.encode('utf-8'))
        return result_put


    """Метод для удаления локации"""

    @staticmethod
    def delete_place(place_id):

        delete_resource = "/maps/api/place/delete/json"   # Ресурс метода DELETE
        delete_url = base_url + delete_resource + key
        print(f'Исходная URL метода DELETE:\n {delete_url}'.encode('utf-8'))
        json_delete_location = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(url=delete_url, body=json_delete_location)
        result_delete.encoding = 'utf-8'
        print(f'Ответ DELETE:\n{result_delete.text}'.encode('utf-8'))
        return result_delete









