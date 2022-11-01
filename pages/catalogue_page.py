from selenium.webdriver.common.by import By
import time

from .locators import CataloguePageLocators
from .locators import CartPageLocators
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import CartPageLocators

class CataloguePage(BasePage):
    def go_to_catalogue(self):
        assert self.element_is_present(*CataloguePageLocators.LINK_TO_PRODUCT_PAGE)


    def should_be_catalogue_line(self):
        self.browser.find_element(*CataloguePageLocators.CATALOGUE_PAGE_ICON)

    def go_to_catalogue(self):
        self.browser.find_element(*CataloguePageLocators.LINK_TO_PRODUCT_PAGE).click()

    def choose_products(self):
        self.browser.find_element(*CataloguePageLocators.BOOK1).click()

    def product_in_cart(self):
        assert self.element_is_present(*CataloguePageLocators.PRODUCT_IN_CART)

    def should_be_order_btn(self):
        assert self.element_is_present(*CartPageLocators.READY_TO_ORDER)

    def select_all_goods(self):
        self.browser.find_elements(*CartPageLocators.ALL_GOODS)


    def order_product(self):
        self.browser.find_element(*CataloguePageLocators.PRODUCT_IN_CART).click()

    # def choose_3(self):
    #
    #     products_page = self.browser.find_elements(By.CSS_SELECTOR, "ol.row li")
    #     for product in products_page:
    #         price = self.change_the_sign(
    #             product.find_element(By.CSS_SELECTOR, "p.price_color").text.strip(" £"))
    #         # book_array.append(product)
    #     # for product in book_array:
    #         if float(price) < 10.0:
    #             self.browser.find_element(By.CSS_SELECTOR, "[data-loading-text='Добавление...']").click()
    #     # self.browser.find_element(By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a').click() #(Открыть корзину)
    #     # self.browser.find_element(By.CSS_SELECTOR, '#default > div.container-fluid.page > div > div > aside > div.side_categories > ul > li:nth-child(2) > a').click()