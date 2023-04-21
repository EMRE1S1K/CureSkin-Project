from selenium.webdriver.common.by import By
from pages.base_page import Page
#from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage(Page):
    PRODUCT = (By.CSS_SELECTOR, ".product__title")

    def verification_product(self):
        self.wait_for_element_appear(*self.PRODUCT)