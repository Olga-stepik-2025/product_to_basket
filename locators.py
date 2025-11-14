from selenium.webdriver.common.by import By


class MainPageLocators():
    """Селекторы для главной страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Селекторы для страницы логина"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    """Селекторы для страницы товара"""
    
    # Название товара
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    
    # Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    
    # Кнопка "Добавить в корзину"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Сообщение об добавлении в корзину (содержит название товара)
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    
    # Сообщение со стоимостью корзины
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".basket-mini .basket-mini-b strong")
