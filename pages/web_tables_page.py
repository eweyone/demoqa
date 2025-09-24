from pages.base_page import BasePage
from components.components import WebElement



class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table_rows = WebElement(driver, 'div.rt-tr-group')
        self.no_rows_found_block = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '[id^="delete-record-"]') # Локатор для всех id,
                                                                                  # которые начинаются с delete-record-