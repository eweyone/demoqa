from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa



def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)

    modal_elements.visit()
    assert modal_elements.not_unique_button.check_count_elements(5)

def test_navigation_modal(browser):
    navigation_modal = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)

    navigation_modal.visit()
    browser.refresh()
    navigation_modal.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
