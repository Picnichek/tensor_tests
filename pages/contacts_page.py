from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_tensor(self):
        self.driver.find_element(
            'class name', 'sbisru-Contacts__border-left').find_element('tag name', 'a').click()

    def check_region(self):
        region = self.driver.find_element(
            'class name', 'sbis_ru-Region-Chooser__text')
        return region.text

    def check_partners(self):
        partners = self.driver.find_element(
            'class name', 'controls-ListViewV__itemsContainer').find_elements('class name', 'sbisru-Contacts-List__name')
        result = []
        for i in partners:
            result.append(i.text)
        return result

    def select_region(self):
        self.driver.find_element(
            'class name', 'sbis_ru-Region-Chooser__text').click()

    def change_region(self):
        self.driver.find_element(
            'class name', 'sbis_ru-Region-Panel__container').find_element(
                'xpath', '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span').click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(
            'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'))

    def check_url(self):
        current_url = self.driver.current_url
        return current_url
