import pytest

from pages.radio import Radio



@pytest.mark.skipif(True, reason='just skip')
def test_decorator_1(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes_btn.click_force()
    choice = 'Yes'
    assert radio.text.get_text() == f'You have selected {choice}'

    radio.impressive_btn.click_force()
    choice = 'Impressive'
    assert radio.text.get_text() == f'You have selected {choice}'

    # assert 'disabled' in radio.no_btn.get_dom_attribute('class')
    assert not radio.no_btn.is_enabled()