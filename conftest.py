import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера"""
    # Опции для Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Раскомментируйте для headless режима
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Инициализация браузера
    driver = webdriver.Chrome(options=options)
    
    # Явно ждем загрузки элементов
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрытие браузера после теста
    driver.quit()
