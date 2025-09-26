import time

from pages.links import Links



# Тест-кейс
def test_window_tab(browser):
    links = Links(browser)

    # Проверка открытия страницы, количества открытых окон браузера, ссылки Home, атрибута и текста у ссылки Home
    links.visit()
    assert links.equal_url()
    assert len(browser.window_handles) == 1
    assert links.link_home.exist()
    assert links.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert links.link_home.get_text() == 'Home'

    # Проверка функциональности ссылки, количества открытых окон браузера
    links.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2