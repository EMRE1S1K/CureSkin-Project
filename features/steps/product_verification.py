from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application
from behave import given, when, then


@given('Open CureSkin main page')
def cureskin_product_page(context):
    context.app.main_page.product_page()


@then('Click on the 1st product')
def click_on_product(context):
    context.app.header.click_on_product()


@then('Verify product details page opened and {search_word} is correct')
def verification_product(context, search_word):
    context.app.search_results.verification_product(search_word)