from selenium.webdriver.common.by import By
from pages.base_page import Page
#from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(Page):
    PRODUCT = (By.CSS_SELECTOR, ".product__title")
    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, ".card-information")

    def verification_product(self):
        first_product_list = self.wait_for_element_appear(*self.PRODUCT)
        print(first_product_list)

    def verify_displayed_items(self):
        second_product_list = self.find_elements(*self.DISPLAYED_PRODUCTS)
        print(second_product_list)
