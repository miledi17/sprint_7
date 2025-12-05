import api
import helpers
import data
import allure


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера.')
    @allure.description('Проверяет, что курьер может авторизоваться.')
    def test_courier_login_success(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 200
        assert "id" in login_response.json()


    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать логин при авторизации')
    def test_courier_login_invalid_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        new_login_data = helpers.generate_new_courier_personal_data()
        login_data['login'] = new_login_data['login']
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 404
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR


    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать пароль при авторизации')
    def test_courier_login_invalid_password(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        new_login_data = helpers.generate_new_courier_personal_data()
        login_data['password'] = new_login_data['password']
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 404
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR


    @allure.title('Авторизация курьера без логина')
    @allure.description('Проверка, что система вернет ошибку, если не указать логин при авторизации')
    def test_courier_login_empty_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_data['login'] = ''
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 400
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR


    @allure.title('Авторизация курьера без пароля')
    @allure.description('Проверка, что система вернет ошибку, если не указать пароль при авторизации')
    def test_courier_login_empty_password(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_data['password'] = ''
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 400
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR