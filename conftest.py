from pytest_bdd import given,when,parsers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@given("browser is opened",target_fixture="driver")
def browser_is_opened():
    print("open the chrome browser")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


@when(parsers.parse("we enter {url} in address bar"))
def enter_the_url(driver,url):
    print("Enter the url",url)
    driver.get(url)



def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    driver1=request.getfixturevalue('driver')
    print("*inside failed scenario*")
    driver1.save_screenshot("./screenshots/s1.png")
    driver1.close()