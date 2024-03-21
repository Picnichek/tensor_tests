class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(
            'class name', 'tensor_ru-CookieAgreement__close').click()

    def get_text(self):
        field = self.driver.find_element(
            'class name', 'tensor_ru-Index__block4-content').find_elements('tag name', 'p')
        result = []
        for i in field:
            result.append(i.text)
        return result

    def get_more_link(self):
        more = self.driver.find_element(
            'class name', 'tensor_ru-Index__block4-content').find_element('tag name', 'a')
        more_link = more.get_attribute('href')
        more.click()
        return more_link

    def get_img_sizes(self):
        block_work = self.driver.find_element('class name',
                                              'tensor_ru-About__block3').find_element('class name', 's-Grid-container').find_elements('class name', 'tensor_ru-About__block3--col-sm12')
        img_sizes = []
        for i in range(len(block_work)):
            size_element = block_work[i].find_element('tag name', 'img').size
            img_sizes.append(size_element)
        return img_sizes
