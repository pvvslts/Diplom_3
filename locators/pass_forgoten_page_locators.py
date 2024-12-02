from selenium.webdriver.common.by import By


class PasswordForgotPageLocators:
    HEADER_PASSWORD_FORGOT_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2")
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon-action')]")
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
