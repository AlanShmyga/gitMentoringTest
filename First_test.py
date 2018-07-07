import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver(request):
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(5)
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys("AlanShmyga")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(ExpectedConditions.title_is("AlanShmyga - Поиск в Google"))
