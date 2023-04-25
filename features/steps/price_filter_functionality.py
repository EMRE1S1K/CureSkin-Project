from behave import given, when, then


@given('Open cureskin homepage')
def open_cureskin_main(context):
    context.app.main_page.open_main()


@when('Click on Shop All section')
def shop_all(context):
    context.app.header.click_shop_all()


@then('Adjust the Price Filter such that there is a change in number of products')
def filter_adjustment(context):
    context.app.header.hover_price_options()


@then('Verify that number of products changes')
def product_count(context):
    context.app.header.product_count()


@then('Verify that products displayed are within the Price filter')
def count_dipslayed_elements(context):
    context.app.search_results.verify_displayed_items()