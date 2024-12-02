from selenium.webdriver.common.by import By


class AccUserPageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href = '/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    ID_BOTTOM_ORDER_IN_HISTORY = (By.XPATH, ".//ul[contains(@class, 'OrderHistory')]/li[last()]//"
                                       "div[contains(@class, 'Box__3lgbs mb-6')]/p[contains(@class, 'digits-default')]")
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']")
