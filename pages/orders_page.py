import allure
from pages.base_page import BasePage
from locators.list_orders_page_locators import ListOrdersPageLocators as ListOrdersLock


class ListOrdersPageStellarBurgers(BasePage):
    @allure.step('Ожидаем загрузки страницы')
    def wait_orders_page(self):
        self.wait_elements_until_visible(ListOrdersLock.ORDERS_ALL_TIME)

    @allure.step('Получаем текст заголовка "Лента заказов"')
    def get_list_orders_header_text(self):
        self.wait_orders_page()
        return self.get_element_text(ListOrdersLock.LIST_ORDERS_HEADER)

    @allure.step('Нажимаем на первый заказ в ленте заказов')
    def click_one_order_in_list(self):
        self.wait_elements_until_visible(ListOrdersLock.ONE_ORDER_IN_LIST)
        return self.click_element(ListOrdersLock.ONE_ORDER_IN_LIST)

    @allure.step('Получаем количестов заказов')
    def get_count_orders(self, locator):
        self.wait_orders_page()
        self.wait_elements_until_visible(locator)
        return self.get_element_text(locator)

    @allure.step('Нажимаем "Конструктор"')
    def click_constructor_button(self):
        self.wait_element_until_clickable(ListOrdersLock.CONSTRUCTOR_BUTTON)
        self.click_element(ListOrdersLock.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем id заказ, который находится в разделе "В работе"')
    def get_id_order_in_progress(self):
        self.wait_elements_until_visible(ListOrdersLock.ORDER_IN_PROGRESS)
        return self.get_element_text(ListOrdersLock.ORDER_IN_PROGRESS)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями заказа')
    def check_open_popup_with_details_order(self):
        self.wait_elements_until_visible(ListOrdersLock.ORDER_POPUP_DETAILS)
        return self.check_display_the_element(ListOrdersLock.ORDER_POPUP_DETAILS)

    @allure.step('Проверяем, что заказ пользователя есть в "Ленте заказов"')
    def check_id_order_user_in_list_orders(self, id_order):
        order_locator = ListOrdersLock.search_order_id(id_order)
        self.wait_elements_until_visible(order_locator)
        return self.check_display_the_element(order_locator)
