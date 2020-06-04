import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver_manager = ChromeDriverManager()
    driver = webdriver.Chrome(executable_path=driver_manager.install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
