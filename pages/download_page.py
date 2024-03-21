import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage:
    def __init__(self, driver):
        self.driver = driver

    def download_finished(self):
        download_dir = f'{os.getcwd()}\\tests'
        files = os.listdir(download_dir)
        return any(file.endswith('.exe') for file in files)

    def download_exe(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(
            'https://sbis.ru/download?tab=ereport&innerTab=ereport25'))
        self.driver.find_element(
            'xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]').click()
        l = self.driver.find_element('xpath',
                                     '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
        size = l.text[13:17]
        name = l.get_attribute('href')[48:]
        l.click()
        start_time = time.time()
        while True:
            if DownloadPage.download_finished(self):
                break
            if time.time() - start_time > 60:
                break
        return size, name
