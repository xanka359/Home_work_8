import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    # Масштабирование страницы
    browser.driver.set_window_size(1920, 1080)  # Устанавливаем размер окна браузера
    browser.driver.set_window_position(0, 0)  # Устанавливаем позицию окна браузера на экране

    # Прокрутка страницы
    #browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()