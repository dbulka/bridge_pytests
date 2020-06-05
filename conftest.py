import pytest
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def config():
    with open('ui_tests/config.json') as config_file:
        data = json.load(config_file)
        return data


@pytest.fixture
def driver(config):
    if config["browser"] == "chrome":
        driver_manager = ChromeDriverManager()
        driver = webdriver.Chrome(executable_path=driver_manager.install())
    elif config["browser"] == "firefox":
        driver_manager = GeckoDriverManager()
        driver = webdriver.Firefox(executable_path=driver_manager.install())
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(config['wait_time'])
    yield driver
    driver.quit()
