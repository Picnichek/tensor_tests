import pytest
from selenium import webdriver
import os


@pytest.fixture(scope='session')
def browser():
    download_dir = f'{os.getcwd()}\\tests'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,  # Отключаем защиту от небезопасных загрузок

    })
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get('https://sbis.ru/')
    driver.find_element(
        'class name', 'sbis_ru-CookieAgreement__close').click()
    # driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()
