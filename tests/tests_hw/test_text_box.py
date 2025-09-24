from pages.textbox_page import TextBox
import time



def test_text_box(browser):
    textbox_page = TextBox(browser)

    textbox_page.visit()
    textbox_page.full_name_field.send_keys('test')
    textbox_page.current_address_field.send_keys('test-test')
    textbox_page.submit_button.click()
    time.sleep(2)
    assert textbox_page.output_full_name.find_element()
    assert textbox_page.output_current_address.find_element()
    assert textbox_page.output_full_name.get_text() == 'Name:test'

    # Ошибка в html - лишний пробел перед двоеточием "Current Address :"
    assert textbox_page.output_current_address.get_text() == 'Current Address :test-test'