from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SingUpPage(BasePage):
    sing_up_url = BasePage.base_url + "password-create"
    account_name_locator = (By.XPATH, "//input[@name='accountName']")
    generated_wif_locator = (By.XPATH, "//input[@name='generatedWIF']")
    confirm_wif_locator = (By.XPATH, "//input[@name='confirmWIF']")
    lose_wif_label_locator = (By.XPATH, "//*[@class='label' and @for='1']")
    recover_wif_label_locator = (By.XPATH, "//*[@class='label' and @for='2']")
    store_wif_label_locator = (By.XPATH, "//*[@class='label' and @for='3']")
    create_account_button_locator = (
        By.XPATH, "//button[@type='submit' and @class='ui basic button main-btn fix-width']")
    account_name = "bigD"

    def open_page(self):
        super().navigate_to(self.sing_up_url)
        return self

    def fill_field(self, locator, text):
        super().get_element(locator).send_keys(text)
        return SingUpPage(self.driver)

    def click_element(self, locator):
        super().get_element(locator).click()

    def follow_link(self, locator):
        super().get_element(locator).click()

    def get_field_data(self, locator):
        text = super().get_element(locator).get_attribute('value')
        return text
