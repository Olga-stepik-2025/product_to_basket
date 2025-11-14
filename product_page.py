from base_page import BasePage
from locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    """Page Object для страницы товара"""

    def add_product_to_basket(self):
        """Добавляет товар в корзину"""
        print(f"📦 Adding product to basket...")
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        return self

    def get_product_name(self):
        """Возвращает название товара"""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        """Возвращает цену товара"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_success_message_with_product_name(self, product_name):
        """
        Проверяет, что товар добавлен в корзину
        И что название товара совпадает с ожидаемым
        """
        try:
            # Ждем появления сообщения об успехе
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
            )
            success_message = self.browser.find_element(
                *ProductPageLocators.SUCCESS_MESSAGE
            )
            message_text = success_message.text
            
            # Проверяем, что название товара в сообщении совпадает
            assert product_name in message_text, \
                f"Expected '{product_name}' in message, but got: {message_text}"
            
            print(f"✅ Success message found with product name '{product_name}'")
            print(f"   Message: {message_text}")
            return self
            
        except Exception as e:
            print(f"❌ Error: {e}")
            raise

    def should_be_basket_total_with_price(self, product_price):
        """
        Проверяет, что стоимость корзины совпадает с ценой товара
        """
        try:
            # Ждем появления сообщения о стоимости корзины
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL_MESSAGE)
            )
            basket_total = self.browser.find_element(
                *ProductPageLocators.BASKET_TOTAL_MESSAGE
            )
            total_text = basket_total.text
            
            # Проверяем, что цены совпадают
            assert product_price in total_text, \
                f"Expected '{product_price}' in basket total, but got: {total_text}"
            
            print(f"✅ Basket total message found with price '{product_price}'")
            print(f"   Message: {total_text}")
            return self
            
        except Exception as e:
            print(f"❌ Error: {e}")
            raise

    def should_be_add_to_basket_button(self):
        """Проверяет наличие кнопки добавления в корзину"""
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
            print("✅ Add to basket button found")
            return self
        except Exception as e:
            print(f"❌ Add to basket button not found: {e}")
            raise AssertionError("Add to basket button not found!")
