from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url('https://shop.cureskin.com/')

    def product_page(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')
