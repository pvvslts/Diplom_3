import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains


class BasePage:
    @allure.step('Добавляем драйвер в конструктор')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение элемента')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step('Ожидаем, что элемент появился на странице и его видно')
    def wait_elements_until_visible(self, locator):
        WebDriverWait(self.driver, 20, poll_frequency=1).until(EC.visibility_of_element_located(locator))
        return self.find_element(locator)

    @allure.step('Ожидаем, что элемент на странице кликабелен')
    def wait_element_until_clickable(self, locator):
        WebDriverWait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator))
        return self.find_element(locator)

    @allure.step('Кликаем по элементу')
    def click_element(self, test_locator):
        target = self.find_element(test_locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Вводим текст в элемент')
    def write_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Проверка текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Ждем закрытие элемента')
    def wait_close_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Перемещение элемента на другой элемент')
    def move_element(self, locator_element, locator_target):
        element = self.wait_elements_until_visible(locator_element)
        target = self.wait_elements_until_visible(locator_target)
        drag_and_drop(self.driver, element, target)

    @allure.step('Ожидаем изменение текста элемента')
    def wait_text_element_after_change(self, test_locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(test_locator, value))

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверить отображение элемента')
    def check_display_the_element(self, locator):
        return self.wait_elements_until_visible(locator).is_displayed()

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))
