import time

from pages.progress_bar import ProgressBar



def test_progress_bar(browser):
    progressbar = ProgressBar(browser)

    progressbar.visit()
    time.sleep(2)
    progressbar.start_stop_btn.click()
    while True:
        if progressbar.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progressbar.start_stop_btn.click()
            break

    assert progressbar.progress_bar.get_dom_attribute('aria-valuenow') == '51'