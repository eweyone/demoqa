import logging
from selenium.common.exceptions import NoAlertPresentException
from components.components import WebElement
import requests



class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        # Локатор 'head > meta' ловил только первый мета-тег, который не имел искомые атрибуты, несмотря на то,
        # что при мануальном тестировании всех страниц искомые атрибуты были в первом мета-теге.
        self.viewport = WebElement(driver, 'meta[name="viewport"]')

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False

    # Метод из урока, всегда возвращает False, даже если алерт есть.
    # def alert(self):
    #     try:
    #         return self.driver.switch_to_alert
    #     except Exception as ex:
    #         logging.log(1, ex)
    #         return False

    # Метод, который я нашел
    def alert(self):
        try:
            return self.driver.switch_to.alert
        except NoAlertPresentException:
            return False

    # Метод для проверки доступности страницы
    def is_page_available(self, url: str) -> bool:
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False