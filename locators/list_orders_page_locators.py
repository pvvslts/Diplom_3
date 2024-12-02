from selenium.webdriver.common.by import By


class ListOrdersPageLocators:
    ORDERS_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]")
    COUNT_ORDERS_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    COUNT_ORDERS_NOW = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    LIST_ORDERS_HEADER = (By.XPATH, ".//div[contains(@class, 'OrderFeed')]/h1[contains(@class, 'mt-10 mb-5')]")
    ONE_ORDER_IN_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    ORDER_POPUP_DETAILS = (By.XPATH, ".//p[text() = 'Cостав']/ancestor::div[contains(@class, 'container__Wo2l')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]")

    @staticmethod
    def search_order_id(id_order):
        return By.XPATH, f'.//ul[contains(@class, "OrderFeed_list")]//p[text() = "{id_order}"]'
