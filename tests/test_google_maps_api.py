import win_unicode_console
win_unicode_console.enable()
from utils.api import Google_maps_api

"""Создание, изменение, удаление локации в google maps api"""
class Test_create_place():

    # Создание новой локации
    def test_create_new_place(self):

        print("Method POST")
        # result_post : Response = Google_maps_api.create_place() - устаревшая конструкция
        result_post = Google_maps_api.create_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        # Проверим, что локация действительно создалась
        print('\nMethod GET for checking POST')
        # result_get: Response = Google_maps_api.get_place(place_id=place_id) - устаревшая конструкция
        result_get = Google_maps_api.get_place(place_id=place_id)

        # Изменим адрес локации
        print('\nMethod PUT')
        result_put = Google_maps_api.update_place(place_id=place_id)

        # Проверим, что адрес локации изменился
        print('\nMethod GET for checking PUT')
        result_get = Google_maps_api.get_place(place_id=place_id)

        # Удалим локацию
        print('\nMethod DELETE')
        result_delete = Google_maps_api.delete_place(place_id=place_id)

        # Проверим, что локация действительно отсутствует
        print('\nMethod GET for checking DELETE')
        result_get = Google_maps_api.get_place(place_id=place_id)









