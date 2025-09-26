from selenium.webdriver.common.keys import Keys
from pages.slider import Slider



def test_slider(browser):
    slider_page = Slider(browser)

    slider_page.visit()
    assert slider_page.equal_url()
    assert slider_page.slider.exist()
    assert slider_page.slider_value.exist()

    while  not slider_page.slider_value.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_value.get_dom_attribute('value') == '50'