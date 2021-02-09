from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   
    page.open()                      
    page.add_product_to_cart()
    time.sleep(5)
    page.item_name_should_matched()
    time.sleep(5)
    page.item_price_should_matched()
    time.sleep(5)
    page.success_message_should_be()



    



