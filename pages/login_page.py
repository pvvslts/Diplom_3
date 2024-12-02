import allure
from locators.logining_page_locators import LoginPageLocators as LoginLock
from pages.base_page import BasePage


class LoginPageStellarBurgers(BasePage):
    @allure.step('Ожидаем когда загрузится страница с формой авторизации')
    def wait_login_page(self):
        self.wait_elements_until_visible(LoginLock.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Нажимаем "Восстановить пароль"')
    def click_password_recovery_button(self):
        self.wait_element_until_clickable(LoginLock.PASSWORD_RECOVERY_BUTTON)
        self.click_element(LoginLock.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Вводим текст в поле email формы авторизации')
    def set_email(self, email):
        self.wait_element_until_clickable(LoginLock.USER_EMAIL_FIELD)
        self.write_text_to_element(LoginLock.USER_EMAIL_FIELD, email)

    @allure.step('Вводим текст в поле "Пароль" формы авторизации')
    def set_password(self, password):
        self.wait_element_until_clickable(LoginLock.USER_PASSWORD_FIELD)
        self.write_text_to_element(LoginLock.USER_PASSWORD_FIELD, password)

    @allure.step('Нажимаем "Войти" в форме авторизации')
    def click_login_button(self):
        self.click_element(LoginLock.LOGIN_BUTTON)

    @allure.step('Авторизация')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step('Нажимаем "Конструктор"')
    def click_constructor_button(self):
        self.wait_element_until_clickable(LoginLock.CONSTRUCTOR_BUTTON)
        self.click_element(LoginLock.CONSTRUCTOR_BUTTON)
