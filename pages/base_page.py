import re
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import CataloguePageLocators
from .locators import CartPageLocators

class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_autorized_user(self):
        assert self.element_is_present(*BasePageLocators.USER_ICON)

    # def should_go_to_catalogue(self):
    #     assert self.element_is_present(*CataloguePageLocators.CATALOGUE_PAGE)

    # def product_should_be_in_basket(self):
    #     assert self.element_is_present(*BasePageLocators.READY_TO_ORDER)

    def click_on_the_element(self, how, locator):
        """Метод, который производит нажатие на элемент сайта"""
        element = self.browser.find_element(how, locator)
        element.click()

    def change_the_sign(self, price):
        """Метод, который заменяет символ запятой, на точку, для приведения цены к вещественному числу"""
        return re.sub(",", ".", price)