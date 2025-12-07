import pytest
import helpers


@pytest.fixture
def courier_credentials():
    courier_data = helpers.create_courier()
    yield courier_data
    helpers.delete_courier(courier_data)


@pytest.fixture
def created_courier_credentials():
    courier_data = helpers.create_courier(register=True)
    yield courier_data
    helpers.delete_courier(courier_data)