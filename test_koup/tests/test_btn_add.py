import time
from test_koup.pages.koup_page import Koup
from test_koup.pages.koup_add_page import KoupAdd



def test_btn_add(browser):
    koup_page = Koup(browser)
    koup_add_page = KoupAdd(browser)

    koup_page.visit()
    assert koup_page.add_remove_element_link.get_text() == 'Add/Remove Elements'
    koup_page.add_remove_element_link.click()
    time.sleep(2)

    assert koup_add_page.equal_url()
    assert koup_add_page.btn_add.get_text() == 'Add Element'
    assert koup_add_page.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for _ in range(4):
        koup_add_page.btn_add.click()

    assert koup_add_page.btns_delete.check_count_elements(4)

    for element in koup_add_page.btns_delete.find_elements(): # Для всех элементов
        assert element.text == 'Delete'

    # assert koup_add_page.btns_delete.get_text() == 'Delete' # Только для 1 элемента

    while koup_add_page.btns_delete.exist():
        koup_add_page.btns_delete.click()

    assert not koup_add_page.btns_delete.exist()