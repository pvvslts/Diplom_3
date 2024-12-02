import allure
from locators.main_page_locators import MainPageLocators as MainLock
from pages.base_page import BasePage


class MainPageStellarBurgers(BasePage):
    @allure.step('Ожидаем загрузки страницы')
    def wait_main_page(self):
        self.wait_elements_until_visible(MainLock.SIGNIN_IN_BUTTON)

    @allure.step('Нажимаем "Войти в аккаунт"')
    def click_autorizations_button(self):
        self.wait_elements_until_visible(MainLock.SIGNIN_IN_BUTTON)
        self.click_element(MainLock.SIGNIN_IN_BUTTON)

    @allure.step('Нажимаем "Личный кабинет"')
    def click_lk_button(self):
        self.wait_elements_until_visible(MainLock.USER_ACCOUNT_BUTTON)
        self.click_element(MainLock.USER_ACCOUNT_BUTTON)

    @allure.step('Ожидаем загрузки страницы после авторизации')
    def wait_create_order_after_loading_page(self):
        self.wait_elements_until_visible(MainLock.CONFIRM_ORDER_BUTTON)

    @allure.step('Получаем текст заголовка "Соберите бургер"')
    def get_create_burger_text(self):
        self.wait_main_page()
        return self.get_element_text(MainLock.MAKE_BURGER)

    @allure.step('Нажимаем "Лента Заказов"')
    def click_list_the_order_button(self):
        self.wait_elements_until_visible(MainLock.LIST_ORDER_BUTTON)
        self.click_element(MainLock.LIST_ORDER_BUTTON)

    @allure.step('Нажимаем на ингредиенту булка')
    def click_ingredient_bun(self):
        self.wait_elements_until_visible(MainLock.DEFAULT_BUN)
        self.click_element(MainLock.DEFAULT_BUN)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_popup_with_ingredient_details(self):
        self.wait_elements_until_visible(MainLock.CLOSE_INGREDIENT)
        self.click_element(MainLock.CLOSE_INGREDIENT)

    @allure.step('Получаем число со счетчика ингредиента булки')
    def get_count_ingredient_bun(self):
        count = int(self.get_element_text(MainLock.COUNTER_DEFAULT_BUN))
        return count

    @allure.step('Ожидаем, когда ингредиент булка появится в конструкторе бургера')
    def wait_ingredient_bun_in_constructor(self):
        self.wait_elements_until_visible(MainLock.DEFAULT_BUN_IN_BURGER)

    @allure.step('Перемещаем ингредиент булка в конструктор бургера')
    def move_ingredient_bun_to_constructor_burger(self):
        self.move_element(MainLock.DEFAULT_BUN, MainLock.CONSTRUCTOR_BURGER)
        self.wait_ingredient_bun_in_constructor()

    @allure.step('Нажимаем "Заказать бургер"')
    def click_creating_order_button(self):
        self.wait_create_order_after_loading_page()
        self.click_element(MainLock.CONFIRM_ORDER_BUTTON)

    @allure.step('Получаем id заказа со всплывающего окна с оформленным заказом')
    def get_id_order_in_popup(self):
        self.wait_text_element_after_change(MainLock.ID_ORDER, '9999')
        id_order = self.get_element_text(MainLock.ID_ORDER)
        return f"0{id_order}"

    @allure.step('Закрываем окно с деталями заказа')
    def close_popup_order_details(self):
        self.wait_text_element_after_change(MainLock.ID_ORDER, '9999')
        self.wait_element_until_clickable(MainLock.CLOSE_ORDER_DETAILS)
        self.click_element(MainLock.CLOSE_ORDER_DETAILS)

    @allure.step('Создать заказ')
    def create_order(self):
        self.wait_create_order_after_loading_page()
        self.move_ingredient_bun_to_constructor_burger()
        self.click_creating_order_button()
        self.check_open_popup_with_order()
        self.close_popup_order_details()

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_open_popup_details_ingredient_bun(self):
        self.wait_elements_until_visible(MainLock.INGREDIENT_POPUP_TITLE)
        return self.check_display_the_element(MainLock.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что окно с деталями ингредиента закрылось')
    def check_close_of_popup_details_ingredient(self):
        self.wait_close_element(MainLock.INGREDIENT_POPUP_TITLE)
        return self.check_invisibility(MainLock.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что появилось всплывающее окно с оформленным заказом')
    def check_open_popup_with_order(self):
        self.wait_elements_until_visible(MainLock.ORDER_IS_GO_PREPAIR)
        return self.check_display_the_element(MainLock.ORDER_IS_GO_PREPAIR)

    @allure.step('Проверить отображение элемента')
    def check_display_the_element(self, locator):
        return self.wait_elements_until_visible(locator).is_displayed()
