from utils.api import Google_maps_api

"""Создание, изменение, удаление локации в google maps api"""
class Test_create_place():

    # Создание новой локации
    def test_create_new_place(self):

        print("Метод POST")
        # result_post : Response = Google_maps_api.create_place() - устаревшая конструкция
        result_post = Google_maps_api.create_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        # Проверим, что локация действительно создалась
        print("\nМетод GET для проверки POST")
        # result_get: Response = Google_maps_api.get_place(place_id=place_id) - устаревшая конструкция
        result_get = Google_maps_api.get_place(place_id=place_id)

        # Изменим адрес локации
        print("\nМетод PUT")
        result_put = Google_maps_api.update_place(place_id=place_id)

        # Проверим, что адрес локации изменился
        print("\nМетод GET для проверки PUT")
        result_get = Google_maps_api.get_place(place_id=place_id)

        # Удалим локацию
        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_place(place_id=place_id)

        # Проверим, что локация действительно отсутствует
        print("\nМетод GET для проверки DELETE")
        result_get = Google_maps_api.get_place(place_id=place_id)









