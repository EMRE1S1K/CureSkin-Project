from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "#product-grid > li:nth-child(1) > div > a")

    def click_on_product(self):
        self.click(*self.FIRST_PRODUCT)
