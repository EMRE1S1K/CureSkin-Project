from selenium.webdriver.common.by import By
from pages.base_page import Page
#from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(Page):
    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, ".card-information")
    LAST_DISPLAYED_PRODUCTS = (By.XPATH, "//p[contains(text(), '3 of 18 products')]")
    PRODUCT_PRESENT = (By.CSS_SELECTOR, "#ProductCount")

    def verification_product(self):
        actual_result = self.find_elements(*self.DISPLAYED_PRODUCTS)
        expected_result = self.find_elements(*self.DISPLAYED_PRODUCTS)
        assert expected_result < actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
        print(f'{expected_result},PASSED')

    def verify_displayed_items(self):
        expected_result = self.wait_for_element_appear(*self.LAST_DISPLAYED_PRODUCTS).text
        expected_result_text = [expected_result.text for numbers in expected_result]
        for el in expected_result_text:
            if 0 < el < 18:
                print('PASSED')
            else:
                print('FAILED')

    def verify_results(self):
        self.wait_for_element_appear(*self.PRODUCT_PRESENT)