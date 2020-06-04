from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CreatePasswordPage(BasePage):
    sing_up_url = BasePage.base_url + "password-create"
    create_password_locator = (By.XPATH, "//input[@name='password']")
    confirm_password_locator = (By.XPATH, "//input[@name='repeatPassword']")
    create_password_button_locator = (By.XPATH, "//button[@class='ui basic button main-btn']")
    password = 'asdasdA1'

    def open_page(self):
        super().navigate_to(self.sing_up_url)
        return self

    def fill_field(self, locator, text):
        super().get_element(locator).send_keys(text)
        return CreatePasswordPage(self.driver)

    def press_button(self, locator):
        super().get_element(locator).click()

