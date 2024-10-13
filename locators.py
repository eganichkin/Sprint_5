from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_PERSONAL_ACCOUNT_BTN = By.XPATH, "//p[text() = 'Личный Кабинет']"

    SEARCH_REG_LBL = By.XPATH, "//a[@href = '/register']"
    SEARCH_REG_NAME_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input"
    SEARCH_REG_EMAIL_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input"
    SEARCH_REG_PASSWORD_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[3]//input"
    SEARCH_REG_BTN = By.XPATH, "//button[text()='Зарегистрироваться']"

    SEARCH_LOGIN_EMAIL_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input"
    SEARCH_LOGIN_PASSWORD_INPUT = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input"
    SEARCH_LOGIN_BTN = By.XPATH, "//button[text()='Войти']"

    SEARCH_ERROR_LBL = By.XPATH, "//p[@class = 'input__error text_type_main-default']"

    SEARCH_LOGIN_TO_ACCOUNT_BTN = By.XPATH, "//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button"
    SEARCH_LOGIN_TO_ACCOUNT_LBL = By.XPATH, "//a[@class = 'Auth_link__1fOlj']"

    SEARCH_ACCOUNT_NAME_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[1]//input"
    SEARCH_ACCOUNT_EMAIL_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[2]//input"
    SEARCH_ACCOUNT_PASSWORD_INPUT = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[3]//input"

    SEARCH_FORGOT_PASSWORD_LBL = By.XPATH, "//a[@href = '/forgot-password' ]"
    SEARCH_CONSTRUCTOR_LBL = By.XPATH, "//p[text() = 'Конструктор' ]"
    SEARCH_HEADER_LOGO = By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2' ]"
    SEARCH_LOGOUT_BTN = By.XPATH, "//button[text()='Выход']"

    SEARCH_BUNS_SPAN = By.XPATH, "//span[text()='Булки']"
    SEARCH_BUNS_SECTION = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[1]"

    SEARCH_SAUCES_SPAN = By.XPATH, "//span[text()='Соусы']"
    SEARCH_SAUCES_SECTION = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[2]"

    SEARCH_FILING_SPAN = By.XPATH, "//span[text()='Начинки']"
    SEARCH_FILING_SECTION = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[3]"


