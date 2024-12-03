import allure
from Urls.sites_url import MessageSuccess


class TestCreateOrder:
    @allure.title('Переход в раздел "Соберите бургер" нажатием "Конструктор"')
    def test_open_burger_constructor(self, driver, main_page, login_page):
        main_page.click_autorizations_button()
        login_page.wait_login_page()
        login_page.click_constructor_button()
        assert main_page.get_create_burger_text() == MessageSuccess.MAKE_BURGER

    @allure.title('Переход в раздел "Лента заказов" нажатием "Лента Заказов"')
    def test_open_list_orders(self, driver, main_page, list_orders_page):
        main_page.wait_main_page()
        main_page.click_list_the_order_button()
        assert list_orders_page.get_list_orders_header_text() == MessageSuccess.LIST_ORDER

    @allure.title('Проверяем открытие окна с деталями ингредиента нажатием на ингредиент')
    def test_open_details_on_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        main_page.click_ingredient_bun()
        assert main_page.check_open_popup_details_ingredient_bun()

    @allure.title('Проверяем, что окно с деталями ингредиента закрывается нажатием закрытия (крестик)')
    def test_close_details_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        main_page.click_ingredient_bun()
        main_page.close_popup_with_ingredient_details()
        assert main_page.check_close_of_popup_details_ingredient()

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_increase_counter_on_add_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        count_ingredient = main_page.get_count_ingredient_bun()
        main_page.move_ingredient_bun_to_constructor_burger()
        count_ingredient_after = main_page.get_count_ingredient_bun()
        assert count_ingredient_after == count_ingredient + 2

    @allure.title('Проверяем, что авторизованный пользователь может оформить заказ')
    def test_make_order_with_signin(self, driver, main_page, login_page, authorized_user):
        main_page.click_autorizations_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_create_order_after_loading_page()
        main_page.move_ingredient_bun_to_constructor_burger()
        main_page.click_creating_order_button()
        assert main_page.check_open_popup_with_order()
