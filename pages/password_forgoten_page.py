import allure
from locators.pass_forgoten_page_locators import PasswordForgotPageLocators as PasswordLock
from pages.base_page import BasePage
from data import FakeData


class PasswordForgotPageStellarBurgers(BasePage):
    @allure.step('Ожидаем, когда загрузится страница с формой восстановления пароля')
    def wait_password_forgot_page(self):
        self.wait_elements_until_visible(PasswordLock.HEADER_PASSWORD_FORGOT_FORM)

    @allure.step('Вводим текст в поле email формы восстановления пароля')
    def set_email(self):
        self.wait_element_until_clickable(PasswordLock.USER_EMAIL_FIELD)
        self.write_text_to_element(PasswordLock.USER_EMAIL_FIELD, FakeData.email())

    @allure.step('Нажимаем "Восстановить"')
    def click_recovery_button(self):
        self.scroll_to_element(PasswordLock.RECOVERY_BUTTON)
        self.click_element(PasswordLock.RECOVERY_BUTTON)

    @allure.step('Нажимаем "Показать/скрыть пароль"')
    def click_show_password_button(self):
        self.wait_element_until_clickable(PasswordLock.SHOW_PASSWORD_BUTTON)
        self.click_element(PasswordLock.SHOW_PASSWORD_BUTTON)

    @allure.step('Ожидаем пока кнопка "Сохранить" станет кликабельной в форме сброса пароля')
    def wait_save_button_clickable(self):
        self.wait_element_until_clickable(PasswordLock.SAVE_BUTTON)

    @allure.step('Проверяем, что поле "Пароль" активно')
    def check_password_field_active(self):
        return self.wait_elements_until_visible(PasswordLock.PASSWORD_FIELD_ACTIVE)
