from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_MAIN_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')   # Кнопка входа в аккаунт на гланой
    REGISTRATION_BUTTON = (By.LINK_TEXT, 'Зарегистрироваться')   # Кнопка "Зарегистрироваться" на странице входа в аккаунт
    NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")   # Поле ввода имени на странице регистрации
    EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")   # Поле ввода эл почты на странице регистрации
    PASSWORD = (By.NAME, 'Пароль')   # Поле ввода почты на странице регистрации
    AUTH_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')   # Кнопка "Зарегистрироваться" на странице регистрации
    LOGIN_MASSAGE = (By.XPATH, '//h2[text()="Вход"]')   # Надпись "Вход" на странице входа в аккаунт
    PASSWORD_ERROR = (By.XPATH, '//p[@class="input__error text_type_main-default"]')   # Ошибка при регистрации с невалидным паролем
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')   # Кнопка входа в аккаунт на главной странице
    LOGIN_EMAIL = (By.NAME, 'name')   # Поле ввода эл почты на странице входа в аккаунт
    LOGIN_PASSWORD = (By.NAME, 'Пароль')   # Поле ввода пароля на странице входа в аккаунт
    SIGNIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')   # Кнопка авторизации на странице входа в личный аккаунт
    ORDER_FORM_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')   # Кнопка "Оформить заказ" на главной странице для авторизованного пользователя
    LOGIN_BUTTON_AUTH_PAGE = (By.XPATH, '//a[@href="/login"]')   # Кнопка "Войти" на странице регистрации
    NEW_PASSWORD_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')   # Кнопка "Восстановить пароль" на странице входа в кабинет
    LOGIN_BUTTON_NEW_PASSWORD_PAGE = (By.XPATH, '//a[@href="/login"]')   # Кнопка "Войти" на странице восстановления пароля
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор')   # Кнопка "Конструктор" в хедере
    LOGO = (By.XPATH, '//a[@href="/"]')   # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')  # Кнопка "Выход" в личном кабинете
    SAUCE_SECTION = (By.XPATH, '//span[text()="Соусы"]')   # Кнопка "Соусы" на главной
    BUNS_SECTION = (By.XPATH, '//span[text()="Булки"]')   # Кнопка "Булки" на главной
    FILLING_SECTION = (By.XPATH, '//span[text()="Начинки"]')   # Кнопка "Начинки" на главной
    BUNS_TITLE = (By.XPATH, '//h2[text()="Булки"]')   # Заголовок "Булки" в разделе "Булки"
    SAUCE_TITLE = (By.XPATH, '//h2[text()="Соусы"]')  # Заголовок "Соусы" в разделе "Соусы"
    FILLING_TITLE = (By.XPATH, '//h2[text()="Начинки"]')   # Заголовок "Начинки" в разделе "Начинки"
    CURRENT_STATE_SAUCE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]')   # Кнопка "Соусы" на главной, когда открыт раздел с соусами
    CURRENT_STATE_BUNS = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]')    # Кнопка "Булки" на главной, когда открыт раздел с булками
    CURRENT_STATE_FILLING = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]')   # Кнопка "Начинки" на главной, когда открыт раздел с начинками