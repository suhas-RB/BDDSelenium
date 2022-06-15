import time

import pytest_bdd
from pytest_bdd import given, when, then, parsers, scenario
from functools import partial

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

scenario = partial(pytest_bdd.scenario, "login.feature")


@scenario("valid login")
def test_valid_login():
    print("test_valid_login")


@scenario("invalid login")
def test_invalid_login():
    print("test_invalid_login")


@given("login page is displayed")
def login_page_displayed(driver):
    title1 = driver.title
    assert "Login" in title1

    print("login page displayed")


@when(parsers.parse("we enter {un} in username"))
def enter_username(driver, un):
    driver.find_element(By.ID, "username").send_keys(un)


@when(parsers.parse("we enter {pw} in password"))
def enter_pwd(driver, pw):
    driver.find_element(By.NAME, "pwd").send_keys(pw)


@when("we click on login button")
def click_login_button(driver):
    print("click login button")

    driver.find_element(By.XPATH, "//div[.='Login ']").click()


@then("home page should be displayed")
def home_page_displayed(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.title_contains("Time-Track"))
        print("Home page is displayed")

    except:
        print("Home page is not displayed")
        assert False


@then("error msg should be displayed")
def error_msg_displayed(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'invalid')]")))
        print("error msg is displayed")

    except:
        print("error msg is not displayed")
        assert False
