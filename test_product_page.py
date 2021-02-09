from pages.product_page import ProductPage
import time
import pytest


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)   
#     page.open()                      
#     page.add_product_to_cart()
#     time.sleep(5)
#     page.item_name_should_matched()
#     time.sleep(5)
#     page.item_price_should_matched()
#     time.sleep(5)
#     page.success_message_should_be()




@pytest.mark.parametrize('promo', ["promo=offer0",
                                  "promo=offer1",
                                  "promo=offer2",
                                  "promo=offer3",
                                  "promo=offer4",
                                  "promo=offer5",
                                  "promo=offer6",
                                   pytest.param("promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")),                                  
                                  "promo=offer8",
                                  "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo}"
    page = ProductPage(browser, link)   
    page.open()                      
    page.add_product_to_cart()
    time.sleep(5)
    page.item_name_should_matched()
    time.sleep(5)
    page.item_price_should_matched()
    time.sleep(5)
    page.success_message_should_be()


    


#
