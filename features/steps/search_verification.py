from behave import given, when, then


@given('Open main page')
def cureskin_product_page(context):
    context.app.main_page.open_main()


@when('Close the pop up')
def closing_popup(context):
    context.app.header.close_popup()


@when('Click on search icon in the header')
def click_search_button(context):
    context.app.header.click_on_search_button()

