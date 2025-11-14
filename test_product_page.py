import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('url', [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
])
def test_guest_can_add_product_to_basket(browser, url):
    """
    Тест: гость может добавить товар в корзину
    
    Шаги:
    1. Открываем страницу товара с параметром promo=newYear
    2. Запоминаем название и цену товара
    3. Нажимаем на кнопку "Добавить в корзину"
    4. Решаем математическое выражение из alert'а
    5. Проверяем, что товар добавлен в корзину
    6. Проверяем, что цена корзины совпадает с ценой товара
    """
    
    # 1. Создаем объект страницы товара и открываем ее
    page = ProductPage(browser, url)
    page.open()
    
    # 2. Проверяем, что кнопка добавления в корзину есть
    page.should_be_add_to_basket_button()
    
    # 3. Запоминаем название и цену товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    print(f"\n📦 Product details:")
    print(f"   Name: {product_name}")
    print(f"   Price: {product_price}")
    
    # 4. Добавляем товар в корзину
    page.add_product_to_basket()
    
    # 5. Решаем математическое выражение и вводим код
    page.solve_quiz_and_get_code()
    
    # 6. Проверяем, что товар добавлен в корзину с правильным названием
    page.should_be_success_message_with_product_name(product_name)
    
    # 7. Проверяем, что стоимость корзины совпадает с ценой товара
    page.should_be_basket_total_with_price(product_price)
    
    print(f"\n✅ Test passed successfully!")
