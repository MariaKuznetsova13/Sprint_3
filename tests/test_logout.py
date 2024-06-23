from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestLogout:
    def test_logout_from_account(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_MASSAGE))
