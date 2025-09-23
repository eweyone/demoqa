from pages.accordian import Accordian
import time



def test_visible_accordian(browser):
    accordian = Accordian(browser)

    accordian.visit()
    assert accordian.section_one_content.visible()

    accordian.section_one_heading.click()
    time.sleep(2)
    assert not accordian.section_one_content.visible()

def test_visible_accordion_default(browser):
    accordian = Accordian(browser)

    accordian.visit()
    assert not accordian.section_two_content_child_one.visible()
    assert not accordian.section_two_content_child_two.visible()
    assert not accordian.section_three_content.visible()