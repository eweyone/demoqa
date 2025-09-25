import time

from pages.alerts import Alerts



def test_alert(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    assert not alerts_page.alert()

    alerts_page.btn_alert.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()

def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alert_page = Alerts(browser)
    name = 'Nikita'

    alert_page.visit()
    alert_page.btn_prompt.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.prompt_result.get_text() == f'You entered {name}'
