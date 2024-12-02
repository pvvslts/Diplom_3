from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    USER_PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
