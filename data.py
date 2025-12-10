CREATE_COURIER_DUPLICATION_ERROR = "Этот логин уже используется. Попробуйте другой."
CREATE_COURIER_EMPTY_FIELD_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR = "Учетная запись не найдена"
LOGIN_WITH_EMPTY_FIELD_ERROR = "Недостаточно данных для входа"


def order_data(color=''):
    data = {
        "firstName": "Настя",
        "lastName": "Мару",
        "address": "г.Москва",
        "metroStation": "Павелецкая",
        "phone": "+7 808 808 8888",
        "rentTime": 5,
        "deliveryDate": "2025-08-08",
        "comment": "Поехали",
    }
    if color:
        data["color"] = color

    return data