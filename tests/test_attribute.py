from pages.textbox_page import TextBox



def test_attribute(browser):
    textbox = TextBox(browser)

    textbox.visit()
    assert textbox.full_name_field.get_dom_attribute('placeholder') == 'Full Name'