from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestStellaBurgersSite:
    url = 'https://stellarburgers.nomoreparties.site/'
    name = 'ganickin_14_001'
    email = 'ganickin_14_001@yandex.ru'
    password = '123456'
    timeout = 5

    def test_successful_registration_with_correct_name_login_password(self, driver, random_correct_account):
        driver.get(self.url + 'register')
        self.name = random_correct_account['name']
        self.email = random_correct_account['email']
        self.password = random_correct_account['password']
        self.account_registration(driver, self.name, self.email, self.password)
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_REG_BTN))

        self.account_login(driver, self.email, self.password, self.timeout, True)
        result_login = self.check_login(driver, self.timeout)
        assert result_login['name'] == self.name and result_login['email'] == self.email

    def test_failed_registration_with_not_correct_password(self, driver, random_incorrect_account):
        driver.get(self.url + 'register')
        self.name = random_incorrect_account['name']
        self.email = random_incorrect_account['email']
        self.password = random_incorrect_account['password']

        self.account_registration(driver, self.name, self.email, self.password)
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ERROR_LBL))

        error_text = driver.find_element(*TestLocators.SEARCH_ERROR_LBL).text
        assert error_text == 'Некорректный пароль'

    def test_login_by_clicking_login_to_account_button(self, driver):
        driver.get(self.url)
        driver.find_element(*TestLocators.SEARCH_LOGIN_TO_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_LOGIN_TO_ACCOUNT_BTN))

        self.account_login(driver, self.email, self.password, self.timeout, True)
        result_login = self.check_login(driver, self.timeout)
        assert result_login['name'] == self.name and result_login['email'] == self.email

    def test_login_by_clicking_personal_account_button(self, driver):
        driver.get(self.url)
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_BTN))

        self.account_login(driver, self.email, self.password, self.timeout, True)
        result_login = self.check_login(driver, self.timeout)
        assert result_login['name'] == self.name and result_login['email'] == self.email

    def test_login_from_the_registration_form(self, driver):
        driver.get(self.url + 'register')
        driver.find_element(*TestLocators.SEARCH_LOGIN_TO_ACCOUNT_LBL).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_REG_BTN))

        self.account_login(driver, self.email, self.password, self.timeout, True)
        result_login = self.check_login(driver, self.timeout)
        assert result_login['name'] == self.name and result_login['email'] == self.email

    def test_login_from_forgot_password_form(self, driver):
        driver.get(self.url + 'forgot-password')
        driver.find_element(*TestLocators.SEARCH_LOGIN_TO_ACCOUNT_LBL).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN_BTN))

        self.account_login(driver, self.email, self.password, self.timeout, True)
        result_login = self.check_login(driver, self.timeout)
        assert result_login['name'] == self.name and result_login['email'] == self.email

    def test_moving_from_main_to_personal_account(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        assert driver.current_url == self.url + 'account/profile'

    def test_moving_from_personal_account_to_main_by_clicking_on_constructor(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_LBL).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        assert driver.current_url == self.url

    def test_moving_from_personal_account_to_main_by_clicking_on_logo(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        driver.find_element(*TestLocators.SEARCH_HEADER_LOGO).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        assert driver.current_url == self.url

    def test_logout_from_personal_account(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        driver.find_element(*TestLocators.SEARCH_LOGOUT_BTN).click()
        WebDriverWait(driver, self.timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        assert driver.current_url == self.url + 'login'

    def test_moving_to_section_sauces(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_SAUCES_SPAN).click()

        assert 'current' in driver.find_element(*TestLocators.SEARCH_SAUCES_SECTION).get_attribute('class')

    def test_moving_to_section_buns(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_SAUCES_SPAN).click()
        driver.find_element(*TestLocators.SEARCH_BUNS_SPAN).click()

        assert 'current' in driver.find_element(*TestLocators.SEARCH_BUNS_SECTION).get_attribute('class')

    def test_moving_to_section_filling(self, driver):
        self.account_login(driver, self.email, self.password, self.timeout)
        driver.find_element(*TestLocators.SEARCH_FILING_SPAN).click()

        assert 'current' in driver.find_element(*TestLocators.SEARCH_FILING_SECTION).get_attribute('class')

    @staticmethod
    def account_registration(driver, name, email, password):
        driver.find_element(*TestLocators.SEARCH_REG_NAME_INPUT).send_keys(name)
        driver.find_element(*TestLocators.SEARCH_REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_REG_BTN).click()

    @staticmethod
    def account_login(driver, email, password, timeout, url_is_get=False):
        if not url_is_get:
            driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*TestLocators.SEARCH_LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BTN).click()
        WebDriverWait(driver, timeout).until(
            expected_conditions.invisibility_of_element_located(TestLocators.SEARCH_LOGIN_BTN))

    @staticmethod
    def check_login(driver, timeout):
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, timeout).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_NAME_INPUT))

        return {"name": driver.find_element(*TestLocators.SEARCH_ACCOUNT_NAME_INPUT).get_attribute("value"),
                "email": driver.find_element(*TestLocators.SEARCH_ACCOUNT_EMAIL_INPUT).get_attribute("value")}
