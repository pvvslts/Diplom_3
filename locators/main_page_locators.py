from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGNIN_IN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    USER_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    MAKE_BURGER = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]/h1")
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']")
    DEFAULT_BUN = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_POPUP_TITLE = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали')]")
    CLOSE_INGREDIENT = (By.XPATH, ".//section[contains(@class, 'Modal_modal_open')]//button[contains(@class, 'close')]")
    COUNTER_DEFAULT_BUN = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p")
    CONSTRUCTOR_BURGER = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    DEFAULT_BUN_IN_BURGER = (By.XPATH, ".//div[contains(@class, 'pos_top')]//span[contains(text(), 'Флюоресцентн')]")
    ORDER_IS_GO_PREPAIR = (By.XPATH, ".//p[contains(text(), 'заказ начали готовить')]")
    ID_ORDER = (By.XPATH, ".//div[contains(@class, 'container__Wo2l')]//h2[contains(@class, 'title_shadow__3ikwq Mod')]")
    CLOSE_ORDER_DETAILS = (By.XPATH, ".//button[contains(@class, 'modal__close__TnseK')]")
