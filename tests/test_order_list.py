import api
import allure


class TestOrderList:
    @allure.title('Получение списка заказов.')
    @allure.description('Проверяет, что в тело ответа возвращается список заказов.')
    def test_list_orders_success(self):
        response = api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()