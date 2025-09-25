import time
from pages.web_tables_page import WebTables



def test_web_tables_add(browser):
    web_tables = WebTables(browser)

    # Проверка наличия кнопки Add на странице
    web_tables.visit()
    web_tables.btn_add.exist()

    # Проверка открытия диалогового окна
    web_tables.btn_add.click()
    assert web_tables.modal_content.exist()

    # Проверка невозможности сохранения пустой формы
    web_tables.btn_modal_submit.click()
    assert web_tables.modal_content.exist()

    # Добавление новой записи в таблицу
    web_tables.modal_first_name.send_keys('test1')
    web_tables.modal_last_name.send_keys('test2')
    web_tables.modal_email.send_keys('test@test.com')
    web_tables.modal_age.send_keys('28')
    web_tables.modal_salary.send_keys('300')
    web_tables.modal_department.send_keys('test3')
    time.sleep(2)
    web_tables.btn_modal_submit.click()
    assert not web_tables.modal_content.exist()
    assert web_tables.row_exists('test1', 'test2')

    # Проверка функциональности кнопки Edit(карандаш)
    web_tables.click_edit_by_name('test1', 'test2')
    assert web_tables.modal_content.exist()

    # Изменение имени в созданной записи и сохранение изменения с проверкой самого изменения в таблице
    web_tables.modal_first_name.clear()
    web_tables.modal_first_name.send_keys('test11')
    web_tables.btn_modal_submit.click()
    assert not web_tables.modal_content.exist()

    # Проверка изменения данных в строке таблицы
    assert not web_tables.row_exists('test1', 'test2')
    assert web_tables.row_exists('test11', 'test2')

    # Проверка функциональности кнопки Delete(корзина) + проверка изменения данных в строке таблицы(строка удалена)
    web_tables.click_delete_by_name('test11', 'test2')
    assert not web_tables.row_exists('test11', 'test2')
    time.sleep(2)

def test_web_tables_next_previous(browser):
    # Предусловие
    web_tables = WebTables(browser)
    web_tables.visit()
    assert web_tables.equal_url()
    web_tables.select_rows_per_page.scroll_to_element()
    web_tables.set_rows_per_page('5')
    time.sleep(2)
    assert web_tables.rows.check_count_elements(5)

    # Тест-кейс
    # Проверка заблокированных кнопок Next и Previous на клик и атрибут 'disabled'
    assert web_tables.btn_next.exist()
    assert not web_tables.btn_next.click_force()
    assert web_tables.btn_next.get_dom_attribute('disabled')
    assert web_tables.btn_previous.exist()
    assert not web_tables.btn_previous.click_force()
    assert web_tables.btn_previous.get_dom_attribute('disabled')

    # Добавление 1 записи в таблицу с проверкой
    assert web_tables.btn_add.exist()
    web_tables.btn_add.scroll_to_element()
    web_tables.btn_add.click()
    assert web_tables.modal_content.exist()
    web_tables.modal_first_name.send_keys('test1')
    web_tables.modal_last_name.send_keys('test1')
    web_tables.modal_email.send_keys('test@testtest.com')
    web_tables.modal_age.send_keys('28')
    web_tables.modal_salary.send_keys('301')
    web_tables.modal_department.send_keys('test4')
    time.sleep(2)
    web_tables.btn_modal_submit.click()
    assert not web_tables.modal_content.exist()
    assert web_tables.row_exists('test1', 'test1')

    # Добавление 2 записи в таблицу с проверкой
    web_tables.btn_add.click()
    assert web_tables.modal_content.exist()
    web_tables.modal_first_name.send_keys('test2')
    web_tables.modal_last_name.send_keys('test2')
    web_tables.modal_email.send_keys('test@test.com')
    web_tables.modal_age.send_keys('28')
    web_tables.modal_salary.send_keys('302')
    web_tables.modal_department.send_keys('test5')
    time.sleep(2)
    web_tables.btn_modal_submit.click()
    assert not web_tables.modal_content.exist()
    assert web_tables.row_exists('test2', 'test2')

    # Добавление 3 записи в таблицу
    web_tables.btn_add.click()
    assert web_tables.modal_content.exist()
    web_tables.modal_first_name.send_keys('test3')
    web_tables.modal_last_name.send_keys('test3')
    web_tables.modal_email.send_keys('test@testttt.com')
    web_tables.modal_age.send_keys('30')
    web_tables.modal_salary.send_keys('303')
    web_tables.modal_department.send_keys('test6')
    time.sleep(2)
    web_tables.btn_modal_submit.click()
    assert not web_tables.modal_content.exist()

    # Проверка появления 2ой страницы и доступности кнопки Next
    assert web_tables.page_info.get_text() == 'Page of 2'
    assert web_tables.btn_next.is_enabled()
    web_tables.btn_next.click()
    time.sleep(2)

    # Проверка добавления 3 записи в таблицу
    assert web_tables.row_exists('test3', 'test3')

    # Проверка открытия 2ой страницы, блокировки кнопки Next, доступности кнопки Previous
    assert web_tables.page_input_number.get_dom_attribute('value') == '2'
    assert web_tables.btn_next.get_dom_attribute('disabled')
    assert web_tables.btn_previous.is_enabled()

    # Проверка открытия 1ой страницы, блокировка кнопки Previous, доступности кнопки Next
    web_tables.btn_previous.click()
    time.sleep(2)
    assert web_tables.page_input_number.get_dom_attribute('value') == '1'
    assert web_tables.btn_previous.get_dom_attribute('disabled')
    assert web_tables.btn_next.is_enabled()
    time.sleep(2)