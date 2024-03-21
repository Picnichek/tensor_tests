import pytest
import os
from pages.main_page import MainPage
from pages.download_page import DownloadPage
import math


def format_size(size_bytes):
    if size_bytes == 0:
        return "0 МБ"
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s}"


@pytest.mark.usefixtures("browser")
def test_download(browser):
    main_page = MainPage(browser)
    main_page.go_to_downlod()
    download_page = DownloadPage(browser)
    file_size, file_name = download_page.download_exe()
    download_dir = f'{os.getcwd()}\\tests'
    files = os.listdir(download_dir)
    size = os.stat(f'{download_dir}\\{file_name}').st_size
    formatted_size = format_size(size)

    assert file_name in files, (
        f'Файла {file_name} нет в: {files}'
    )
    assert float(formatted_size) == float(file_size), (
        f'Размер файла неправильный {file_size} МБ != {formatted_size} МБ'
    )
    os.remove(f'{download_dir}\\{file_name}')
