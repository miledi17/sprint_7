import string
import requests
import api
import random


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

"""Генерирует новые данные курьера."""
def generate_new_courier_personal_data(empty_field=None):
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    if empty_field is not None:
        courier_data[empty_field] = ''
    return courier_data


"""Создает данные для входа на основе данных курьера."""
def create_login_data(courier_data):
    return {
        'login': courier_data['login'],
        'password': courier_data['password']
    }


def login_courier(courier_data):
    login_data = create_login_data(courier_data)
    login_response = api.login_courier(login_data)
    courier_id = login_response.json().get('id')
    return courier_id


def create_courier(register=False):
    courier_data = generate_new_courier_personal_data()
    if register:
        api.create_courier(courier_data)
    return courier_data


def delete_courier(courier_data):
    courier_id = login_courier(courier_data)
    try:
        api.delete_courier(courier_id)
    except requests.exceptions.RequestException as e:
                print(f"Ошибка удаления курьера: {e}")