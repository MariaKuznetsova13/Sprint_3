from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestConstructor:
    def test_click_constructor_button(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))

    def test_click_logo(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))
