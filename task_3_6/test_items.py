import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


urls = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
    'http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/',
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/',
    'http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/',
]


@pytest.mark.parametrize('url', urls)
def test_btn_add_to_basket_is_avalible(browser, url):
    browser.get(url)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#add_to_basket_form > button'))
    )
    time.sleep(5)
