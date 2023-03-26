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
        print(f'Исходная URL метода POST:\n {post_url}')
        result_post = Http_methods.post(url=post_url, body=json_create_place)
        print(f'Ответ POST:\n{result_post.text}')
        return result_post


    """Метод для проверки новой локации"""

    @staticmethod
    def get_place(place_id):

        get_resource = "/maps/api/place/get/json"   # Ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(f'Исходная URL метода GET:\n {get_url}')
        result_get = Http_methods.get(url=get_url)
        print(f'Ответ GET:\n{result_get.text}')
        return result_get


    """Метод для изменения локации"""

    @staticmethod
    def update_place(place_id):

        put_resource = "/maps/api/place/update/json"   # Ресурс метода PUT
        put_url = base_url + put_resource + key
        print(f'Исходная URL метода PUT:\n {put_url}')
        json_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(url=put_url, body=json_update_location)
        print(f'Ответ PUT:\n{result_put.text}')
        return result_put


    """Метод для удаления локации"""

    @staticmethod
    def delete_place(place_id):

        delete_resource = "/maps/api/place/delete/json"   # Ресурс метода DELETE
        delete_url = base_url + delete_resource + key
        print(f'Исходная URL метода DELETE:\n {delete_url}')
        json_delete_location = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(url=delete_url, body=json_delete_location)
        print(f'Ответ DELETE:\n{result_delete.text}')
        return result_delete









