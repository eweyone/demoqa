from pages.textbox_page import TextBox
import time



def test_clear(browser):
    textbox = TextBox(browser)

    textbox.visit()
    textbox.full_name_field.send_keys('test')
    time.sleep(2)
    textbox.full_name_field.clear()
    time.sleep(2)
    assert textbox.full_name_field.get_text() == ''