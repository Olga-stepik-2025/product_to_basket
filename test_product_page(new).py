import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    """Параметризованный тест добавления товара в корзину"""

    # Извлекаем номер offer для отчета
    offer_number = link.split("promo=")[1]

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"\n🔍 Testing {offer_number}")
    print(f"📦 Product: {product_name}")
    print(f"💰 Price: {product_price}")

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    # Проверки - здесь может упасть тест
    try:
        page.should_be_success_message_with_product_name(product_name)
        page.should_be_basket_total_with_price(product_price)
        print(f"✅ {offer_number} - PASSED\n")
    except AssertionError as e:
        print(f"❌ {offer_number} - FAILED: {e}\n")
        raise
