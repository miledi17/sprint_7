import requests
import urls
import allure


@allure.step('Отправляем запрос на создание курьера')
def create_courier(data):
    return requests.post(urls.CREATE_COURIER, json=data)

@allure.step('Отправляем запрос на удаление курьера')
def delete_courier(courier_id):
    return requests.delete(urls.DELETE_COURIER + str(courier_id))

@allure.step('Отправляем запрос логина курьера')
def login_courier(data):
    return requests.post(urls.LOGIN_COURIER, json=data)

@allure.step('Отправляем запрос на создание заказа')
def create_order(data):
    return requests.post(urls.CREATE_ORDER, json=data)

@allure.step('Отправляем запрос на получение списка заказов')
def get_orders():
    return requests.get(urls.GET_ORDERS)