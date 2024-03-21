class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://sbis.ru/')

    def go_to_contacts(self):
        self.driver.find_element('link text', 'Контакты').click()

    def go_to_downlod(self):
        self.driver.find_element(
            'link text', 'Скачать локальные версии').click()
