from pages.web_tables_page import WebTables
import time



def test_webtables(browser):
    webtables_page = WebTables(browser)

    webtables_page.visit()
    assert webtables_page.table_rows.exist()

    assert not webtables_page.no_rows_found_block.exist()

    while webtables_page.btn_delete_row.exist():
        webtables_page.btn_delete_row.click()
    time.sleep(2)

    assert webtables_page.no_rows_found_block.exist()