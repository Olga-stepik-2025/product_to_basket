from base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    """Страница логина"""

    def should_be_login_page(self):
        """Проверяем, что это страница логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяем, что в URL есть слово 'login'"""
        current_url = self.browser.current_url
        assert "login" in current_url, \
            f"Expected 'login' in URL, but got: {current_url}"
        print(f"✅ URL contains 'login': {current_url}")

    def should_be_login_form(self):
        """Проверяем наличие формы логина"""
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
            print("✅ Login form found!")
        except NoSuchElementException:
            raise AssertionError("Login form not found on page!")

    def should_be_register_form(self):
        """Проверяем наличие формы регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
            print("✅ Register form found!")
        except NoSuchElementException:
            raise AssertionError("Register form not found on page!")

    def should_be_login_username_input(self):
        """Проверяем наличие поля для ввода username в форме логина"""
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
            print("✅ Login username input found!")
        except NoSuchElementException:
            raise AssertionError("Login username input not found!")

    def should_be_login_password_input(self):
        """Проверяем наличие поля для ввода пароля в форме логина"""
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
            print("✅ Login password input found!")
        except NoSuchElementException:
            raise AssertionError("Login password input not found!")

    def should_be_login_button(self):
        """Проверяем наличие кнопки логина"""
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
            print("✅ Login button found!")
        except NoSuchElementException:
            raise AssertionError("Login button not found!")

    def should_be_register_username_input(self):
        """Проверяем наличие поля для ввода username в форме регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME)
            print("✅ Register username input found!")
        except NoSuchElementException:
            raise AssertionError("Register username input not found!")

    def should_be_register_email_input(self):
        """Проверяем наличие поля для ввода email в форме регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            print("✅ Register email input found!")
        except NoSuchElementException:
            raise AssertionError("Register email input not found!")

    def should_be_register_password_input(self):
        """Проверяем наличие поля для ввода пароля в форме регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
            print("✅ Register password input found!")
        except NoSuchElementException:
            raise AssertionError("Register password input not found!")

    def should_be_register_password_confirm_input(self):
        """Проверяем наличие поля для подтверждения пароля в форме регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
            print("✅ Register password confirm input found!")
        except NoSuchElementException:
            raise AssertionError("Register password confirm input not found!")

    def should_be_register_button(self):
        """Проверяем наличие кнопки регистрации"""
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
            print("✅ Register button found!")
        except NoSuchElementException:
            raise AssertionError("Register button not found!")
