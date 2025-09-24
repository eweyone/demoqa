from pages.base_page import BasePage
from components.components import WebElement



class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name_field = WebElement(driver, '#userName')
        self.current_address_field = WebElement(driver, '#currentAddress')
        self.submit_button = WebElement(driver, '#submit')
        self.output_full_name = WebElement(driver, '#name')
        self.output_current_address = WebElement(driver, '#currentAddress.mb-1')