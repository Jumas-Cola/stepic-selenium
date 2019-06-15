from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def page_test(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
        )
        print()
        print('Got It!')
        button = self.driver.find_element_by_css_selector('#book')
        button.click()
        val = self.driver.find_element_by_css_selector('#input_value').text
        inp = self.driver.find_element_by_css_selector('#answer')
        inp.send_keys(str(self.calc(int(val))))
        btn = self.driver.find_element_by_css_selector('#solve')
        btn.click()

    @staticmethod
    def calc(x):
        return math.log(abs(12 * math.sin(x)))

    def close(self):
        self.driver.quit()


driver = Driver()
driver.page_test("https://suninjuly.github.io/explicit_wait2.html")
# driver.close()
