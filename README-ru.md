# DemoQA Автотесты

## Обзор

Автотесты для [demoqa.com](https://demoqa.com) на Python с использованием **pytest** и **Selenium**.  
Реализован паттерн **Page Object Model**, тесты разделены по страницам, присутствуют вспомогательные компоненты.

## Организация проекта

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

## Установка

#### 1. Склонировать репозиторий:
```
git clone https://github.com/eweyone/demoqa.git
cd demoqa
```
#### 2. Установить зависимости:
```
pip install -r requirements.txt
```
#### 3. Скачать chromedriver, подходящий к вашей локальной версии браузера Chrome (если не используете тот, что уже лежит в репозитории).
[Download chromedriver.exe](https://chromedriver.chromium.org/downloads)

## Использование

#### Запуск всех тестов:
```
pytest
```
#### Запуск конкретного файла:
```
pytest tests/test_alert.py
```
#### Запуск с отображением подробных логов:
```
pytest -v -s
```

## Стек технологий

* Python 3.9+
* pytest - тестовый фреймворк
* Selenium - управление браузером
* Page Object Model - структуризация кода проекта

## Примечание

* Для стабильной работы тестов рекомендуется обновлять ChromeDriver под свою версию браузера.
* Тесты организованы по страницам [DemoQA](https://demoqa.com/) (каждая тестируемая страница вынесена в отдельный Page Object).
* Дополнительные домашние задания и эксперименты вынесены в ```tests_hw``` и ```test_koup```.
