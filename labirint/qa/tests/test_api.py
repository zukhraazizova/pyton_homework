import requests
import allure
import pytest

from constants import BASE_URL, BASKET_URL, ADD_TO_CART_URL


@allure.suite("API Лабиринт")
@allure.title("Добавление книги в корзину")
@pytest.mark.api
def test_add_to_cart():
    with allure.step("Создаём сессию и получаем cookies"):
        session = requests.Session()
        session.get(BASE_URL)

    with allure.step("Отправляем POST-запрос на добавление товара"):
        data = "id=621345&imho=0&s=1&charity=0"

        response = session.post(
            ADD_TO_CART_URL,
            data=data,
            headers={"x-requested-with": "XMLHttpRequest"}
        )

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200


@allure.suite("API Лабиринт")
@allure.title("Проверка пустой корзины")
@pytest.mark.api
def test_empty_cart():
    with allure.step("Создаём сессию и получаем cookies"):
        session = requests.Session()
        session.get(BASE_URL)

    with allure.step("Отправляем GET-запрос к корзине"):
        response = session.get(
            BASKET_URL,
            headers={"x-requested-with": "XMLHttpRequest"}
        )

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что корзина пуста"):
        data = response.json()
        assert data.get("basket_count", 0) == 0


@allure.suite("API Лабиринт")
@allure.title("Изменение количества товара в корзине")
@pytest.mark.api
def test_update_quantity():
    with allure.step("Создаём сессию и получаем cookies"):
        session = requests.Session()
        session.get(BASE_URL)

    with allure.step("Добавляем товар с количеством 2"):
        data = "id=621345&imho=0&s=2&charity=0"

        response = session.post(
            ADD_TO_CART_URL,
            data=data,
            headers={"x-requested-with": "XMLHttpRequest"}
        )

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200


@allure.suite("API Лабиринт")
@allure.title("Доступ к корзине без авторизации (гостевая корзина)")
@pytest.mark.api
def test_unauthorized_access():
    with allure.step("Отправляем запрос без cookies"):
        response = requests.get(BASKET_URL)

    with allure.step("Проверяем, что доступ разрешён для гостя"):
        assert response.status_code == 200