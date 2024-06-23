from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestRegistration:
    def test_success_registration(self, driver):
        password = '123456'
        name = 'Мария'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_MASSAGE))

    def test_invalid_passport_negative_result(self, driver):
        password = '12345'
        name = 'Мария'
        driver.find_element(*Locators.ACCOUNT_MAIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        mess_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR)).text
        assert mess_error == 'Некорректный пароль'
