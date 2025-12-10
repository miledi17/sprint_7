import pytest
import helpers


@pytest.fixture
def courier_with_generated_credentials():
    """Фикстура для курьера без регистрации (только данные)."""
    courier_data = helpers.create_courier()
    yield courier_data
    helpers.delete_courier(courier_data)


@pytest.fixture
def fully_registered_courier():
    """Фикстура для полностью зарегистрированного курьера."""
    courier_data = helpers.create_courier(register=True)
    yield courier_data
    helpers.delete_courier(courier_data)