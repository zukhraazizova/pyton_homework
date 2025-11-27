import pytest
import requests
import allure
BASE_URL_API= "https://www.labirint.ru"
HTTOKEN = "qAP4TRGTdNf0VaxSVswbCIZnLKSiwRe_uOfMg-UHIDyzaz16NHDojLuvyZzh9wPICFa67F4WvQXvFVLAhM9dTpKFheNi80SRvJBoCzqckGfLzksFf7srVkhWzwLcoJrJoVA"

HEADERS = {
    "Authorization": f"Bearer {HTTOKEN}",
    "Content-Type": "application/json"
}

BOOK_ID = 918221  # "Идиот" Ф. Достоевский
@allure.suite("API Лабиринт")
@allure.title("Поиск книги по названию")
@pytest.mark.api
def test_search_book():
    query = "Идиот"
    with allure.step(f"Делаем GET запрос на поиск книги: {query}"):
        response = requests.get(
            f"{BASE_URL_API}/search/v2/search",
            params={"query": query, "page": 1, "pageSize": 10},
            headers=HEADERS
        )
    with allure.step("Проверяем статус код"):
        assert response.status_code == 200
    with allure.step("Проверяем что в результатах есть книга с названием 'Идиот'"):
        books = response.json().get("books", [])
        assert any(query.lower() in book["title"].lower() for book in books)


@allure.suite("API Лабиринт")
@allure.title("Просмотр книги")
@pytest.mark.api
def test_view_book():
    with allure.step(f"GET запрос книги с ID {BOOK_ID}"):
        response = requests.get(f"{BASE_URL_API}/books/{BOOK_ID}/", headers=HEADERS)
    with allure.step("Проверяем статус код"):
        assert response.status_code == 200
    with allure.step("Проверяем, что в ответе есть название книги 'Идиот'"):
        assert "Идиот" in response.text


@allure.suite("API Лабиринт")
@allure.title("Добавление книги в корзину")
@pytest.mark.api
def test_add_to_cart():
    with allure.step(f"POST запрос на добавление книги {BOOK_ID} в корзину"):
        response = requests.post(
            f"{BASE_URL_API}/cart/add/",
            headers=HEADERS,
            json={"bookId": BOOK_ID, "quantity": 1}
        )
    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


@allure.suite("API Лабиринт")
@allure.title("Удаление книги из корзины")
@pytest.mark.api
def test_remove_from_cart():
    with allure.step(f"DELETE запрос на удаление книги {BOOK_ID} из корзины"):
        response = requests.delete(f"{BASE_URL_API}/cart/remove/{BOOK_ID}/", headers=HEADERS)
    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


@allure.suite("API Лабиринт")
@allure.title("Добавление книги в избранное и просмотр избранного")
@pytest.mark.api
def test_add_and_view_favorites():
    with allure.step(f"POST запрос на добавление книги {BOOK_ID} в избранное"):
        response_add = requests.post(
            f"{BASE_URL_API}/favorite/add/",
            headers=HEADERS,
            json={"bookId": BOOK_ID}
        )
    assert response_add.status_code == 200

    with allure.step("GET запрос списка избранного"):
        response_view = requests.get(f"{BASE_URL_API}/favorite/", headers=HEADERS)
    assert response_view.status_code == 200
    assert any(str(BOOK_ID) in str(book.get("id", "")) for book in response_view.json().get("books", []))
