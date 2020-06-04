from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SingInPage(BasePage):
    sing_up_url = BasePage.base_url + "sing-up"
    sing_up_locator = (By.XPATH, "//*[@class='link main-link']")

    def follow_link(self, locator):
        super().get_element(locator).click()