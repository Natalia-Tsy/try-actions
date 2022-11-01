import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.catalogue_page import CataloguePage
from .pages.cart_page import CartPage

link = 'http://selenium1py.pythonanywhere.com/ru/'

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с товарами
@pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_product_page()
    # переходит на страницу с товарами
    page.go_to_product_page()

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу авторизации
@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # переходит на страницу авторизации
    page.go_to_login_page()
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()

# Тест проверяет, что пользователь может зарегистрироваться
def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу авторизации
    page.open_page()
    # регистрирует нового пользователя
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    # проверяет, что пользователь авторизован
    page.should_be_autorized_user()

def test_guest_can_go_to_catalogue(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_product_page()
    # переходит на страницу с товарами
    page.go_to_product_page()

def test_user_can_choose_products(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
    page = CataloguePage(browser, link)
    page.open_page()
    page.should_be_catalogue_line()
    #page.go_to_catalogue()
    page.choose_products()
    time.sleep(3)
    page.product_in_cart()
    page.should_be_order_btn()
    time.sleep(2)


def test_user_can_order(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
    page = CataloguePage(browser, link)
    page.open_page()
    page.choose_products()
    page.order_product()
    link = 'https://selenium1py.pythonanywhere.com/ru/basket/'
    page = CartPage(browser, link) #переопределить?
    page.compare_prices() #?????

# def test_order_3(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
#     page = CataloguePage(browser, link)
#     page.open_page()
#     page.select_all_goods()
#     page.choose_3()
#     time.sleep(5)


# def test_cart(browser): #Корзина изначально пустая
#     link = 'https://selenium1py.pythonanywhere.com/ru/basket/'
#     page = CartPage(browser, link)
#     page.open_page()
#     page.compare_prices()