class ApplicationData:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN = f'{MAIN_URL}/login'
    FORGOT_PASSWORD = f'{MAIN_URL}/forgot-password'
    RESET_PASSWORD = f'{MAIN_URL}/reset-password'
    ACCOUNT_PROFILE = f'{MAIN_URL}/account/profile'
    ORDER_HISTORY = f'{MAIN_URL}/account/order-history'
    ENDPOINT_CREATING_ACCOUNT = '/api/auth/register'
    ENDPOINT_LOGIN = '/api/auth/login'
    ENDPOINT_USER = '/api/auth/user'


class MessageSuccess:
    MAKE_BURGER = "Соберите бургер"
    LIST_ORDER = "Лента заказов"