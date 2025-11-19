import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает страницу"""
        self.browser.get(self.url)
        return self

    def solve_quiz_and_get_code(self):
        """Решает математическое выражение из alert"""
        try:
            print("⏳ Waiting for alert...")
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())

            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"📝 Alert text: {alert_text}")

            # Извлекаем число из текста
            x = alert_text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            print(f"🧮 Calculated answer: {answer}")

            alert.send_keys(answer)
            alert.accept()

            # ✅ ИСПРАВЛЕНИЕ: Проверяем второй alert (может не быть)
            try:
                print("⏳ Waiting for second alert (code)...")
                WebDriverWait(self.browser, 5).until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                code = alert.text
                print(f"\n{'=' * 60}")
                print(f"🎉 YOUR CODE: {code}")
                print(f"{'=' * 60}\n")
                alert.accept()
            except (TimeoutException, NoAlertPresentException):
                # ✅ Это нормально - второй alert может не появиться
                print("ℹ️ No second alert presented (this is OK)")

        except TimeoutException as e:
            print(f"❌ Timeout waiting for alert: {e}")
            raise
        except Exception as e:
            print(f"❌ Error in solve_quiz_and_get_code: {e}")
            raise

        return self
