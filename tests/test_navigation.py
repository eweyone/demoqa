from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage



def test_navigation(browser):
    demoqa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demoqa_page.visit()
    demoqa_page.button_elements.click()

    elements_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()