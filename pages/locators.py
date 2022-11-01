from selenium.webdriver.common.by import By


class MainPageLocators():
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    #READY_TO_ORDER = (By.XPATH, '//*[@id="content_inner"]/div[3]/div/div/a')
class CataloguePageLocators():
    CATALOGUE_PAGE_ICON = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > div > div > div.page-header.action > h1')
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    BOOK1 = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(1) > article > div.product_price > form > button')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(2) > a:nth-child(1)')
class CartPageLocators():
    READY_TO_ORDER = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(2) > a:nth-child(2)')
    ALL_GOODS = (By.CSS_SELECTOR, 'product_price')
    BOOK1_CART_PRICE = (By.CSS_SELECTOR, '#basket_formset > div > div > div.col-sm-1 > p')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#basket_totals > table > tbody > tr:nth-child(10) > td > h3')
    # prod_price_lists[0].find_element(By.CSS_SELECTOR,'.price_color').text