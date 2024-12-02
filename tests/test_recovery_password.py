import allure
from data import ApplicationData


class TestPasswordRecovery:
    @allure.title('Проверяем переход на страницу восстановления пароля по нажатию "Восстановить пароль"')
    def test_forgot_password_page_recovery_button(self, driver, main_page,
                                                              login_page, password_forgot_page):
        main_page.click_autorizations_button()
        login_page.click_password_recovery_button()
        password_forgot_page.wait_password_forgot_page()
        assert password_forgot_page.get_current_url() == ApplicationData.FORGOT_PASSWORD

    @allure.title('Проверяем переход на форму сброса пароля по нажатию "Восстановить"')
    @allure.description('''Заполняем поле email в форме восстановления пароля, нажимаем "Восстановить", 
                        проверяем, что перешли на форму сброса пароля''')
    def test_open_reset_pass_page_recovery_button(self, driver, main_page,
                                                    login_page, password_forgot_page):
        main_page.click_autorizations_button()
        login_page.click_password_recovery_button()
        password_forgot_page.set_email()
        password_forgot_page.click_recovery_button()
        password_forgot_page.wait_save_button_clickable()
        assert password_forgot_page.get_current_url() == ApplicationData.RESET_PASSWORD

    @allure.title('Нажатие на кнопку "показать/скрыть пароль" делает поле активным в форме сброса пароля')
    @allure.description('''Заполняем поле email в форме восстановления пароля, нажимаем "Восстановить", 
                            в форме сброса пароля нажимаем "Скрыть/показать пароль", проверяем,
                            что поле "Пароль" становится активным"''')
    def test_active_field_password_show_pass_button(self, driver, main_page, login_page,
                                                                password_forgot_page):
        main_page.click_autorizations_button()
        login_page.click_password_recovery_button()
        password_forgot_page.set_email()
        password_forgot_page.click_recovery_button()
        password_forgot_page.click_show_password_button()
        assert password_forgot_page.check_password_field_active()
