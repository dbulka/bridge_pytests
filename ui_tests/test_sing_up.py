import pytest
import time

from pages.CreatePasswordPage import CreatePasswordPage
from pages.SingInPage import SingInPage
from pages.SingUpPage import SingUpPage


@pytest.mark.sing_up
class TestSingUp:

    def test_sing_in(self, driver):
        browser = SingUpPage(driver)
        browser.open_page()
        browser.fill_field(locator=CreatePasswordPage.create_password_locator, text=CreatePasswordPage.password)
        browser.fill_field(locator=CreatePasswordPage.confirm_password_locator, text=CreatePasswordPage.password)
        browser.press_button(locator=CreatePasswordPage.create_password_button_locator)
        time.sleep(1)
        browser.follow_link(locator=SingInPage.sing_up_locator)
        time.sleep(1)
