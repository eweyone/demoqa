import time

from pages.alerts import Alerts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест-кейс
def test_check_alert(browser):
    alerts_page = Alerts(browser)

    # Проверка url, наличия кнопки timer alert(вторая Click me) на странице
    alerts_page.visit()
    assert alerts_page.equal_url()
    assert alerts_page.btn_timer_alert.exist()

    # Проверка функциональности кнопки timer alert(вторая Click me)
    alerts_page.btn_timer_alert.click()
    # Проверка, что алерт появляется через 5 секунд через time.sleep(5)
    time.sleep(5)
    alerts_page.alert().accept()

# Тот же тест-кейс, через модули библиотеки selenium
def test_check_alert_upgrade(browser):
    alerts_page = Alerts(browser)

    # Проверка url, наличия кнопки timer alert(вторая Click me) на странице
    alerts_page.visit()
    assert alerts_page.equal_url()
    assert alerts_page.btn_timer_alert.exist()

    alerts_page.btn_timer_alert.click()

    # Засекаем время старта(момент клика)
    start = time.time()
    # Ожидаем алерт максимум 10 секунд
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    # Время с момента клика до появления алерта
    elapsed = round(time.time() - start, 1)

    # Вывод в консоль, через сколько появился алерт
    print(f'Alert appeared after {elapsed} seconds')
    # Проверка появления алерта через 5 секунд в пределах погрешности (+-0.5)
    assert 4.5 <= elapsed <= 5.5
    # Закрытие алерта
    alert.accept()