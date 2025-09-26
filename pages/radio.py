from pages.base_page import BasePage
from components.components import WebElement



class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes_btn = WebElement(driver, '#yesRadio')
        self.impressive_btn = WebElement(driver, '#impressiveRadio')
        self.no_btn = WebElement(driver, '#noRadio')
        self.text = WebElement(driver, '.mt-3')