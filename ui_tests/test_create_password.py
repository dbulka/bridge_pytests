import pytest
import time
import allure

from pages.CreatePasswordPage import CreatePasswordPage


@allure.feature("Testing 'Create password' page")
@allure.label(allure.severity_level.BLOCKER)
@pytest.mark.create_password
class TestCreatePassword:

    def test_create_password(self, driver):
        browser = CreatePasswordPage(driver)
        browser.open_page()
        browser.fill_field(locator=CreatePasswordPage.create_password_locator, text=CreatePasswordPage.password)
        browser.fill_field(locator=CreatePasswordPage.confirm_password_locator, text=CreatePasswordPage.password)
        browser.press_button(locator=CreatePasswordPage.create_password_button_locator)
        time.sleep(1)
        current_url = browser.driver.current_url
        assert current_url == CreatePasswordPage.base_url + "sign-in"
