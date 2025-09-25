from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table_rows = WebElement(driver, 'div.rt-tr-group')
        self.no_rows_found_block = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '[id^="delete-record-"]')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_content = WebElement(driver, 'div.fade.modal.show > div > div')
        self.modal_first_name = WebElement(driver, '#firstName')
        self.modal_last_name = WebElement(driver, '#lastName')
        self.modal_email = WebElement(driver, '#userEmail')
        self.modal_age = WebElement(driver, '#age')
        self.modal_salary = WebElement(driver, '#salary')
        self.modal_department = WebElement(driver, '#department')
        self.btn_modal_submit = WebElement(driver, '#submit')

        # self.row_4 = WebElement(driver, 'div:nth-child(4) > div > div')
        # self.row_4_name = WebElement(driver, 'div.rt-tr-group:nth-of-type(4) div.rt-td:nth-child(1)')
        # self.btn_edit_4 = WebElement(driver, '#edit-record-4')
        # self.btn_delete_row_4 = WebElement(driver, '#delete-record-4')

        self.rows = WebElement(driver, '.rt-tr-group')
        self.cells = WebElement(driver, '.rt-td')
        self.select_rows_per_page = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.page_info = WebElement(driver, 'span.-pageInfo')
        self.page_input_number = WebElement(driver, 'input[type=number]')

    # Метод для поиска всех ячеек в строке
    def get_row_cells(self, row):
        return row.find_elements(By.CSS_SELECTOR, '.rt-td')

    # Метод для сохранения всех данных строки
    def get_rows_data(self):
        rows = self.rows.find_elements()
        table_data = []
        for row in rows:
            cells = self.get_row_cells(row)
            row_values = [cell.text for cell in cells]
            table_data.append(row_values)
        return table_data

    # Метод для проверки строки по имени и фамилии(предполагаем, что комбинация этих данных в строке всегда уникальная)
    def row_exists(self, first_name, last_name):
        for row in self.rows.find_elements():
            cells = self.get_row_cells(row)
            if cells[0].text == first_name and cells[1].text == last_name:
                return True
        return False

    # Метод для нажатия на кнопку Edit(карандаш) в конкретной строке по имени и фамилии
    def click_edit_by_name(self, first_name, last_name):
        for row in self.rows.find_elements():
            cells = self.get_row_cells(row)
            if cells[0].text == first_name and cells[1].text == last_name:
                edit_btn = row.find_element(By.CSS_SELECTOR, '[id^="edit-record"]')
                edit_btn.click()
                break

    # Метод для нажатия на кнопку Delete(корзина) в конкретной строке по имени и фамилии
    def click_delete_by_name(self, first_name, last_name):
        for row in self.rows.find_elements():
            cells = self.get_row_cells(row)
            if cells[0].text == first_name and cells[1].text == last_name:
                delete_btn = row.find_element(By.CSS_SELECTOR, '[id^="delete-record"]')
                delete_btn.click()
                break

    # Метод для выбора варианта из выпадающего списка
    def set_rows_per_page(self, value:str) -> str:
        select = Select(self.select_rows_per_page.find_element())
        select.select_by_value(value)