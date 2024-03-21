import pytest
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage


@pytest.mark.usefixtures("browser")
def test_region(browser):
    main_page = MainPage(browser)
    main_page.go_to_contacts()
    contacts_page = ContactsPage(browser)
    region = contacts_page.check_region()
    partners = contacts_page.check_partners()
    contacts_page.select_region()
    contacts_page.change_region()
    new_region = contacts_page.check_region()
    current_url = contacts_page.check_url()
    new_partners = contacts_page.check_partners()

    assert region == 'Свердловская обл.', (
        f'Не тот регион {region} != "Свердловская обл."'
    )
    assert partners != [], (
        f'В данном регионе нет партнеров {partners}'
    )
    assert new_region == 'Камчатский край', (
        f'Не тот регион {region} != "Камчатский край"'
    )
    assert current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients', (
        f'Не корректный url {current_url} != "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"'
    )
    assert new_partners != partners, (
        f'Не поменялся регион: {new_partners} == {partners}')
