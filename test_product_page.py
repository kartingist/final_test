from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
from .pages.product_page import Result

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = Result(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
