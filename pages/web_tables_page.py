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

        self.all_rows = WebElement(driver, '.rt-tr')
        self.rows = WebElement(driver, '.rt-tr-group')
        self.header_cells_common_class = WebElement(driver, '.rt-th')
        self.header_cells = WebElement(driver, '.rt-resizable-header-content')
        self.cells = WebElement(driver, '.rt-td')
        self.select_rows_per_page = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.page_info = WebElement(driver, 'span.-pageInfo')
        self.page_input_number = WebElement(driver, 'input[type=number]')

    # Метод для поиска всех ячеек в строке
    def get_row_cells(self, row):
        return row.find_elements(By.CSS_SELECTOR, '.rt-td')

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

    # Метод для поиска ячейки в строке шапки по тексту дочернего элемента
    def get_header_row_cells_by_text(self, text:str):
        header_cells = self.header_cells_common_class.find_elements()

        for cell in header_cells:
            content = cell.find_element(By.CSS_SELECTOR, '.rt-resizable-header-content')
            if content.text == text:
                return cell
        return None

    # Метод для клика по ячейке header в таблице по названию
    def click_header_cell_by_name(self, name):
        # Шапка не имеет уникального локатора, поэтому берем 1ый элемент из списка
        header_row = self.all_rows.find_elements()[0]
        # Получаем все ячейки только в шапке
        header_cells = header_row.find_elements(By.CSS_SELECTOR, '.rt-resizable-header-content')
        # Клик по нужной ячейке шапки по имени
        for cell in header_cells:
            if cell.text == name:
                cell.click()
                return cell