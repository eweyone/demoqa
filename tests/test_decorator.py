import pytest

from pages.demoqa import DemoQa



@pytest.mark.skip
def test_decorator(browser):
    demoqa = DemoQa(browser)

    demoqa.visit()
    assert demoqa.h5.check_count_elements(6)

    for element in demoqa.h5.find_elements():
        assert element.text != ''