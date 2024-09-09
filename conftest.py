# import pytest

# @pytest.fixture
# def sample_data():
#     return "sample data"

# def test_sample(sample_data):
#     assert sample_data == "sample data"

import pytest
from selene import browser

@pytest.fixture()
def setting_browser():
    # Устанавливаем размеры окна браузера
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    # Закрываем браузер после выполнения теста
    browser.quit()
