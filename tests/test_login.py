from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestLogin:
    def test_login_main_page(self, driver):
        password = '123456'
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))

    def test_login_account(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))

    def test_login_auth_page(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))

    def test_login_page_new_password(self, driver):
        password = '123456'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.NEW_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_NEW_PASSWORD_PAGE).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Constants.EMAIL_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGNIN_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_FORM_BUTTON))
