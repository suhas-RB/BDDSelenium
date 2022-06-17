import time

import pytest_bdd
from pytest_bdd import given, when, then, parsers, scenario
from functools import partial

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.login_page import LoginPage
from page.Enter_time_track_page import EnterTimeTrackPage



scenario = partial(pytest_bdd.scenario, "login.feature")


@scenario("valid login")
def test_valid_login():
    print("test_valid_login")


@scenario("invalid login")
def test_invalid_login():
    print("test_invalid_login")


@given("login page is displayed",target_fixture='login_page')
def login_page_displayed(driver):
    login_page=LoginPage(driver)
    wait=WebDriverWait(driver,10)
    result=login_page.verify_loginpage_is_displayed(wait)
    assert result
    return login_page
    print("login page displayed")


@when(parsers.parse("we enter {un} in username"))
def enter_username(login_page, un):
    #driver.find_element(By.ID, "username").send_keys(un)
    login_page.set_username(un)


@when(parsers.parse("we enter {pw} in password"))
def enter_pwd(login_page, pw):
    #driver.find_element(By.NAME, "pwd").send_keys(pw)
    login_page.set_password(pw)


@when("we click on login button")
def click_login_button(login_page):
    #driver.find_element(By.XPATH, "//div[.='Login ']").click()
    login_page.click_loginbutton()


@then("home page should be displayed")
def home_page_displayed(driver):
    wait = WebDriverWait(driver, 10)
    home_page=EnterTimeTrackPage(driver)
    result=home_page.verify_homepage_is_displayed(wait)
    assert result
    print("home page is displayed")

@then("error msg should be displayed")
def error_msg_displayed(login_page,driver):
    wait = WebDriverWait(driver, 10)
    result=login_page.verify_err_msg_displayed(wait)
    assert result
    print("error msg is displayed")