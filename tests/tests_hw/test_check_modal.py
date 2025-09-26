import time
from pages.modal_dialogs import ModalDialogs
import requests
import pytest



# Метод для проверки доступности страницы
def is_page_available(url:str) -> bool:
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Тест-кейс
def test_check_modals(browser):
    modal_dialogs_page = ModalDialogs(browser)

    # Скип теста, если страница недоступна
    if not is_page_available(modal_dialogs_page.base_url):
        pytest.skip(f'{modal_dialogs_page.base_url} is not available')

    # Проверка url, наличия кнопок small modal и large modal на странице
    modal_dialogs_page.visit()
    assert modal_dialogs_page.equal_url()
    assert modal_dialogs_page.btn_small_modal.exist()
    assert modal_dialogs_page.btn_large_modal.exist()

    # Проверка функциональности кнопки Small modal, появления модального окна, функциональности кнопки Close
    modal_dialogs_page.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialogs_page.modal_content.exist()
    assert modal_dialogs_page.btn_close_small_modal.exist()
    modal_dialogs_page.btn_close_small_modal.click()
    assert not modal_dialogs_page.modal_content.exist()
    time.sleep(2)

    # Проверка функциональности кнопки Large modal, появления модального окна, функциональности кнопки Close
    modal_dialogs_page.btn_large_modal.click()
    time.sleep(2)
    assert modal_dialogs_page.modal_content.exist()
    assert modal_dialogs_page.btn_close_large_modal.exist()
    modal_dialogs_page.btn_close_large_modal.click()
    assert not modal_dialogs_page.modal_content.exist()