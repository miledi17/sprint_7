import pytest
import api
import helpers
import data
import allure

class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается код 201 и {"ok": true}.')
    def test_can_create_courier(self, courier_credentials):
        response = api.create_courier(courier_credentials)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверка создания двух курьеров с одинаковыми данными.')
    def test_cannot_create_duplicate_courier(self, courier_credentials):
        response_first = api.create_courier(courier_credentials)
        assert response_first.status_code == 201

        response_second = api.create_courier(courier_credentials)
        assert response_second.status_code == 409
        assert response_second.json()['message'] == data.CREATE_COURIER_DUPLICATION_ERROR


    @allure.title('Создание курьера с пустым обязательным полем')
    @allure.description('Проверка, что нельзя создать курьера с пустым обязательным полем (логин или пароль).')
    @pytest.mark.parametrize('courier_credentials',
        [
            helpers.generate_new_courier_personal_data(empty_field='login'),
            helpers.generate_new_courier_personal_data(empty_field='password')
        ])
    def test_create_courier_with_empty_login_or_password(self, courier_credentials):
        create_response = api.create_courier(courier_credentials)

        assert create_response.status_code == 400
        assert create_response.json()["message"] == data.CREATE_COURIER_EMPTY_FIELD_ERROR


    @allure.title('Создание курьера с логином, который уже есть')
    @allure.description('Проверка, что нельзя создать курьера с логином, который уже есть.')
    def test_create_courier_existing_login(self, courier_credentials):
        courier_data = helpers.generate_new_courier_personal_data()
        response = api.create_courier(courier_data)
        assert response.status_code == 201

        new_data = helpers.generate_new_courier_personal_data()
        new_data['login'] = courier_data['login']
        create_response = api.create_courier(new_data)

        assert create_response.status_code == 409
        assert create_response.json()["message"] == data.CREATE_COURIER_DUPLICATION_ERROR