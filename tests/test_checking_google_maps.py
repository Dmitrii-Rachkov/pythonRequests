import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
from utils.api import Google_maps_api
from utils.checking import Checking
import allure

"""Создание, изменение, удаление локации в google maps api"""

@allure.epic("Create new location with checking")
class Test_place_cheking():

    # Создание новой локации
    @allure.description("Test CRUD of new location")
    def test_new_place(self):

        print('\nMethod POST')
        result_post = Google_maps_api.create_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        # Проверим статус код ответа
        Checking.check_status_code(status_code=200, result=result_post)
        # Проверим обязательные поля
        Checking.check_fields(expected_fields=['status', 'place_id', 'scope', 'reference', 'id'], result=result_post)
        # Проверим значение поля 'Status'
        Checking.check_value(expected_value="OK", result=result_post, field_name='status')

        # Проверим, что локация действительно создалась
        print('\nMethod GET for checking POST')
        # result_get: Response = Google_maps_api.get_place(place_id=place_id) - устаревшая конструкция
        result_get = Google_maps_api.get_place(place_id=place_id)
        Checking.check_status_code(status_code=200, result=result_get)
        Checking.check_fields(expected_fields=['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'], result=result_get)
        Checking.check_value(expected_value="29, side layout, cohen 09", result=result_get, field_name='address')

        # Изменим адрес локации
        print('\nMethod PUT')
        result_put = Google_maps_api.update_place(place_id=place_id)
        Checking.check_status_code(status_code=200, result=result_put)
        Checking.check_fields(expected_fields=['msg'], result=result_put)
        Checking.check_value(expected_value="Address successfully updated", result=result_put, field_name='msg')

        # Проверим, что адрес локации изменился
        print('\nMethod GET for cheking PUT')
        result_get = Google_maps_api.get_place(place_id=place_id)
        Checking.check_status_code(status_code=200, result=result_get)
        Checking.check_fields(expected_fields=['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'], result=result_get)
        Checking.check_value(expected_value="100 Lenina street, RU", result=result_get, field_name='address')


        # Удалим локацию
        print('\nMethod DELETE')
        result_delete = Google_maps_api.delete_place(place_id=place_id)
        Checking.check_status_code(status_code=200, result=result_delete)
        Checking.check_fields(expected_fields=['status'], result=result_delete)
        Checking.check_value(expected_value="OK", result=result_delete, field_name='status')

        # Проверим, что локация действительно отсутствует
        print('\nMethod GET for checking DELETE')
        result_get = Google_maps_api.get_place(place_id=place_id)
        Checking.check_status_code(status_code=404, result=result_get)
        Checking.check_fields(expected_fields=['msg'], result=result_get)
        Checking.check_value(expected_value="Get operation failed, looks like place_id  doesn't exists",
                             result=result_get, field_name='msg')

        print('\nTesting of creating, changing, deleting a location in google maps api is completed.')

