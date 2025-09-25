import time
from selenium.webdriver.common.by import By

import pytest
from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize('pages', [Accordian, Alerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)

    # Проверка атрибутов первого мета-тега
    first_meta = browser.find_element(By.CSS_SELECTOR, 'head > meta')
    print('First <meta>:', first_meta.get_dom_attribute('outerHTML'))
    print('name=', first_meta.get_dom_attribute('name'))
    print('content=', first_meta.get_dom_attribute('content'))

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'