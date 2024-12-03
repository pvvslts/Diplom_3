import allure
import pytest
from locators.list_orders_page_locators import ListOrdersPageLocators as ListOrdersLock

class TestListOrders:
    @allure.title('Проверяем открытие окна с деталями заказа нажатием на заказ')
    def test_open_details_order(self, driver, main_page, list_orders_page):
        main_page.wait_main_page()
        main_page.click_list_the_order_button()
        list_orders_page.click_one_order_in_list()
        assert list_orders_page.check_open_popup_with_details_order()

    @allure.title('Проверяем: заказы пользователя из «История заказов» отображаются на странице «Лента заказов»')
    def test_show_list_orders_add_new_order_from_history(self, driver, main_page, login_page, list_orders_page,
                                                              user_account_page, authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.create_order()
        main_page.click_lk_button()
        user_account_page.wait_account_page()
        user_account_page.click_the_order_history_button()
        id_last_order = user_account_page.get_id_order()
        user_account_page.click_list_the_order_button()
        list_orders_page.wait_orders_page()
        assert list_orders_page.check_id_order_user_in_list_orders(id_last_order)

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время"/"Выполнено за сегодня"'
                  ' увеличивается')
    @pytest.mark.parametrize('counter', [ListOrdersLock.COUNT_ORDERS_ALL_TIME,
                                         ListOrdersLock.COUNT_ORDERS_NOW])
    def test_increas_count_add_new_order_now_and_all(self, driver, main_page, login_page, list_orders_page,
                                                       authorized_user, counter):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.click_list_the_order_button()
        count_orders = list_orders_page.get_count_orders(counter)
        list_orders_page.click_constructor_button()
        main_page.create_order()
        main_page.click_list_the_order_button()
        count_orders_new = list_orders_page.get_count_orders(counter)
        assert count_orders_new > count_orders

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_showing_in_progress(self, driver, main_page, login_page, list_orders_page,
                                                    authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.move_ingredient_bun_to_constructor_burger()
        main_page.click_creating_order_button()
        main_page.check_open_popup_with_order()
        id_order = main_page.get_id_order_in_popup()
        main_page.close_popup_order_details()
        main_page.click_list_the_order_button()
        id_order_in_processing = list_orders_page.get_id_order_in_progress()
        assert id_order == id_order_in_processing
