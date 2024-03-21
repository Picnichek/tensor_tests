import pytest
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage


@pytest.mark.usefixtures("browser")
def test_page_objects(browser):
    main_page = MainPage(browser)
    main_page.go_to_contacts()
    contacts_page = ContactsPage(browser)
    contacts_page.go_to_tensor()
    tensor_page = TensorPage(browser)
    text = tensor_page.get_text()
    more_link = tensor_page.get_more_link()
    img_sizes = tensor_page.get_img_sizes()
    first_size = img_sizes[0]
    first_height = first_size['height']
    first_width = first_size['width']

    assert 'Сила в людях' in text, (
        f'На странице нет параграфа "Сила в людях"'
    )
    assert more_link == 'https://tensor.ru/about', (
        f'Ссылка {more_link} не соответствует "https://tensor.ru/about"')

    for img_size in img_sizes[1:]:
        assert img_size['height'] == first_height, (
            f'Высота не равна: {img_size["height"]} != {first_height}')
        assert img_size['width'] == first_width, (
            f'Ширина не равна: {img_size["width"]} != {first_width}')
