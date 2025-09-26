import time

from pages.web_tables_page import WebTables


# Тест-кейс
def test_sort(browser):
    webtables = WebTables(browser)

    # Проверка url
    webtables.visit()
    assert webtables.equal_url()

    # Проверка функциональности заголовка столба First Name (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('First Name')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('First Name')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('First Name')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Last Name (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('Last Name')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Last Name')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Last Name')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Age (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('Age')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Age')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Age')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Email (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('Email')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Email')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Email')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Salary (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('Salary')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Salary')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Salary')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Department (происходит сортировка таблицы по этому столбцу)
    webtables.click_header_cell_by_name('Department')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Department')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Department')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')

    # Проверка функциональности заголовка столба Action (происходит сортировка таблицы по этому столбцу)
    # Сортировка по этому столбцу не имеет смысла, но функциональность реализована.
    webtables.click_header_cell_by_name('Action')
    time.sleep(2)
    cell = webtables.get_header_row_cells_by_text('Action')
    assert '-sort-asc' in cell.get_dom_attribute('class')
    webtables.click_header_cell_by_name('Action')
    time.sleep(2)
    assert '-sort-desc' in cell.get_dom_attribute('class')