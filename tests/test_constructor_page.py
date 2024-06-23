from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructorPage:
    def test_constructor_sections(self, driver):
        driver.find_element(*Locators.SAUCE_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCE_TITLE))
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CURRENT_STATE_SAUCE))

        driver.find_element(*Locators.BUNS_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS_TITLE))
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CURRENT_STATE_BUNS))

        driver.find_element(*Locators.FILLING_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLING_TITLE))
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CURRENT_STATE_FILLING))
