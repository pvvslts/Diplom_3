import allure
from Urls.sites_url import ApplicationData

class TestLKAccount:
    @allure.title('Проверяем переход в личный кабинет пользователя по нажатию "Личный кабинет"')
    def test_open_lk_profile(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.click_lk_button()
        user_account_page.wait_account_page()
        assert user_account_page.get_current_url() == ApplicationData.ACCOUNT_PROFILE

    @allure.title('Проверяем переход в историю заказов в личном кабинете')
    def test_open_order_history_in_lk(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.click_lk_button()
        user_account_page.wait_account_page()
        user_account_page.click_the_order_history_button()
        assert user_account_page.get_current_url() == ApplicationData.ORDER_HISTORY

    @allure.title('Проверяем выход из аккаунта нажатию на кнопку "Выход" в личном кабинете')
    def test_logout(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.click_lk_button()
        user_account_page.wait_account_page()
        user_account_page.click_logout_button()
        login_page.wait_login_page()
        assert login_page.get_current_url() == ApplicationData.LOGIN
