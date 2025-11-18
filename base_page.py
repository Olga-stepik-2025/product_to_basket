import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        return self

    def solve_quiz_and_get_code(self):
        """
        Решает математическое выражение из alert'а и вводит ответ
        Выводит код проверки в консоль
        """
        try:
            # ✅ Ждем появления alert (до 10 секунд)
            print("⏳ Waiting for alert...")
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())

            # Переключаемся на alert
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"📝 Alert text: {alert_text}")

            # Извлекаем число из текста
            x = alert_text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            print(f"🧮 Calculated answer: {answer}")

            # Вводим ответ и подтверждаем
            alert.send_keys(answer)
            alert.accept()

            # Проверяем наличие второго alert с кодом
            try:
                WebDriverWait(self.browser, 3).until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"✅ Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("ℹ️ No second alert presented")

        except Exception as e:
            print(f"❌ Error while solving quiz: {e}")
            raise

