from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestAccount:
    def test_click_account_main_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_MASSAGE))
