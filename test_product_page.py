import pytest
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    """Тест: гость может добавить товар в корзину"""

    # URL с промо-кодом
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # Открываем страницу
    page = ProductPage(browser, url)
    page.open()

    # Проверяем кнопку
    page.should_be_add_to_basket_button()

    # Получаем данные товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"\n📦 Product: {product_name}")
    print(f"💰 Price: {product_price}")

    # Добавляем в корзину
    page.add_product_to_basket()

    # Решаем квиз
    page.solve_quiz_and_get_code()

    # Проверки
    page.should_be_success_message_with_product_name(product_name)
    page.should_be_basket_total_with_price(product_price)

    print("✅ Test passed!")
