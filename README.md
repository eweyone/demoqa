# DemoQA Automation Tests Project

## Overview

Automated tests for [DemoQA](https://demoqa.com) written in **Python** using **pytest** and **Selenium**.  
The project follows the **Page Object Model** pattern, tests are organized by site pages, and helper components are included.

## Project organisation

```text
demoqa
├── .gitignore                   <- Files and folders excluded from git
├── README.md                    <- Project description
├── chromedriver.exe             <- ChromeDriver binary for Selenium
├── components                   <- Shared UI components
│   └── components.py
├── conftest.py                  <- Pytest configuration and fixtures
├── main.py                      <- Main entry point (if used)
├── pages                        <- Page Object Model (site pages and elements)
│   ├── base_page.py             <- Base class for all pages
│   ├── demoqa.py                <- Main demoqa page
│   ├── elements_page.py         <- Elements page
│   ├── browser_tab.py           <- Browser tab handling page
│   ├── alerts.py                <- Alerts page
│   ├── accordian.py             <- Accordian page
│   ├── form_page.py             <- Form page
│   ├── links.py                 <- Links page
│   ├── modal_dialogs.py         <- Modal Dialogs page
│   ├── progress_bar.py          <- Progress Bar page
│   ├── radio.py                 <- Radio buttons page
│   ├── slider.py                <- Slider page
│   ├── textbox_page.py          <- Text Box page
│   └── web_tables_page.py       <- Web Tables page
├── pytest.ini                   <- Pytest configuration
├── requirements.txt             <- Project dependencies
├── structure.txt                <- Saved project tree
├── test_koup                    <- Additional module with "koup" tests
│   ├── pages
│   │   ├── koup_add_page.py
│   │   └── koup_page.py
│   └── tests
│       └── test_btn_add.py
├── tests
│   ├── test_alert.py
│   ├── test_attribute.py
│   ├── test_browser_tab.py
│   ├── test_check_icon_demoqa.py
│   ├── test_clear.py
│   ├── test_css.py
│   ├── test_decorator.py
│   ├── test_decorator_1.py
│   ├── test_decorator_mark.py
│   ├── test_elements.py
│   ├── test_go_to_page_elements.py
│   ├── test_login_form.py
│   ├── test_navigation.py
│   ├── test_progress_bar.py
│   ├── test_seo.py
│   ├── test_seo_meta.py
│   ├── test_size.py
│   ├── test_slider.py
│   ├── test_visible.py
│   ├── test_webtables.py
│   └── tests_hw
│       ├── test_check_alert.py
│       ├── test_check_modal.py
│       ├── test_check_text.py
│       ├── test_login_form_validate.py
│       ├── test_page_dialogs.py
│       ├── test_sort.py
│       ├── test_text_box.py
│       ├── test_visible_hw.py
│       ├── test_web_tables_hw.py
│       └── test_window_tab.py
```

## Installation

#### 1. Clone the repository:
```
git clone https://github.com/eweyone/demoqa.git
cd demoqa
```
#### 2. Install dependencies:
```
pip install -r requirements.txt
```
#### 3. Download chromedriver that matches your local Chrome version(if you don't use the one already provided)
[Download chromedriver.exe](https://chromedriver.chromium.org/downloads)

## Usage

#### Run all tests:
```
pytest
```
#### Run a specific test file:
```
pytest tests/test_alert.py
```
#### Run with verbose logs:
```
pytest -v -s
```

## Tech stack

* Python 3.9+
* pytest - testing framework
* Selenium - browser automation
* Page Object Model - test code organisation pattern

## Notes

* Keep ChromeDriver up to date with your Chrome version for stable runs.
* Tests are organized by site pages; each page being tested is implemented as a separate Page Object.
* Additional experiments and homework tasks are stored in ```tests_hw``` and ```test_koup```.