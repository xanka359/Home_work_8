from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


@pytest.fixture(scope='session', autouse=True)
def manage_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    #browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    #browser.config.window_height = 1080  # задает высоту окна браузера
    #browser.config.window_width = 1920
    browser = Browser(Config(driver))

    yield browser
    browser.quit()