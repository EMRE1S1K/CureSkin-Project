from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    POPUP_EXIT = (By.CSS_SELECTOR, ".popup-close")
    SEARCH_ICON = (By.CSS_SELECTOR, "#shopify-section-header > sticky-header > header > search-modal > details > summary")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "#product-grid > li:nth-child(1) > div > a")
    SHOP_ALL = (By.CSS_SELECTOR, "a[href='/collections/all'] span")
    PRODUCT_COUNT = (By.CSS_SELECTOR, "#ProductCount")
    TARGET_1 = (By.CSS_SELECTOR, "div.price-range__thumbs.is-upper")
    TARGET_2 = (By.CSS_SELECTOR, ".div.price-range__thumbs.is-lower")

    def click_on_product(self):
        self.click(*self.FIRST_PRODUCT)

    def click_on_search_button(self):
        self.click(*self.SEARCH_ICON)

    def click_shop_all(self):
        self.wait_for_element_click(*self.SHOP_ALL)

    def close_popup(self):
        self.wait_for_element_click(*self.POPUP_EXIT)
        sleep(3)

    def hover_price_options(self):
        product_count = self.find_element(*self.PRODUCT_COUNT)
        print(product_count)
        target_1 = self.find_element(*self.TARGET_1)
        # target_2 = self.find_elements(*self.TARGET_2)
        actions = ActionChains(self.driver)
        actions.move_to_element(target_1)
        actions.click_and_hold(target_1)
        actions.move_by_offset(-120, 0)
        # actions.drag_and_drop(target_1, target_2)
        actions.release()
        actions.perform()
        sleep(15)

    def product_count(self):
        product_count = self.find_element(*self.PRODUCT_COUNT)
        print(product_count)

    def search_item(self, text):
        self.input_text(text, *self.SEARCH_ICON)