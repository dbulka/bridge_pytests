import pytest
import time
import allure

from pages.CreatePasswordPage import CreatePasswordPage
from pages.SingInPage import SingInPage
from pages.SingUpPage import SingUpPage


@allure.feature("Testing 'Sign Up' page")
@allure.label(allure.severity_level.BLOCKER)
@pytest.mark.create_password
class TestSingUp:

    def test_sing_up(self, driver):
        browser = SingUpPage(driver)
        browser.open_page()
        browser.fill_field(locator=CreatePasswordPage.create_password_locator, text=CreatePasswordPage.password)
        browser.fill_field(locator=CreatePasswordPage.confirm_password_locator, text=CreatePasswordPage.password)
        browser.click_element(locator=CreatePasswordPage.create_password_button_locator)
        time.sleep(1)
        browser.follow_link(locator=SingInPage.sing_up_locator)
        time.sleep(1)
        browser.fill_field(locator=SingUpPage.account_name_locator, text=SingUpPage.account_name)
        generated_wif = browser.get_field_data(SingUpPage.generated_wif_locator)
        browser.fill_field(locator=SingUpPage.confirm_wif_locator, text=generated_wif)
        browser.click_element(locator=SingUpPage.lose_wif_label_locator)
        browser.click_element(locator=SingUpPage.recover_wif_label_locator)
        browser.click_element(locator=SingUpPage.store_wif_label_locator)
        browser.click_element(locator=SingUpPage.create_account_button_locator)
        time.sleep(5)
