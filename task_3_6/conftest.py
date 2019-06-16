import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help='Choose language of browser.\
                           For example: --language="es"')


@pytest.fixture
def browser(request):
    lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
