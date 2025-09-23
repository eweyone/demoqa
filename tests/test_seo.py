from pages.demoqa import DemoQa



def test_seo(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert browser.title == 'DEMOQA'