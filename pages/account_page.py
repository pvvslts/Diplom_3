import allure
from pages.base_page import BasePage
from locators.account_locators import AccUserPageLocators as UserLock


class AccountPageStellarBurgers(BasePage):
    @allure.step('Ожидание, загрузки личного кабинет пользователя')
    def wait_account_page(self):
        self.wait_elements_until_visible(UserLock.SAVE_BUTTON)

    @allure.step('Нажимаем "История заказов" в личном кабинете пользователя')
    def click_the_order_history_button(self):
        self.wait_elements_until_visible(UserLock.ORDER_HISTORY_BUTTON)
        self.click_element(UserLock.ORDER_HISTORY_BUTTON)

    @allure.step('Нажимаем "Выход" в личном кабинете пользователя')
    def click_logout_button(self):
        self.wait_elements_until_visible(UserLock.LOGOUT_BUTTON)
        self.click_element(UserLock.LOGOUT_BUTTON)

    @allure.step('Получаем id последнего заказа пользователя')
    def get_id_order(self):
        self.wait_elements_until_visible(UserLock.ID_BOTTOM_ORDER_IN_HISTORY)
        return self.get_element_text(UserLock.ID_BOTTOM_ORDER_IN_HISTORY)

    @allure.step('Нажимаем "Лента заказов" в личном кабинете пользователя')
    def click_list_the_order_button(self):
        self.wait_elements_until_visible(UserLock.LIST_ORDER_BUTTON)
        self.click_element(UserLock.LIST_ORDER_BUTTON)
