from .base_page import BasePage
from .locators import ProductPageLocators
import time



class ProductPage(BasePage): 
    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
        time.sleep(2)

    def success_message_should_be(self):
    	success_message_added_to_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS_ADD_PRODUCT_TO_CART)    	
    	assert success_message_added_to_cart, "Success message is not in the page"


    def item_name_should_matched(self):
    	product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE).text
    	product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
    	assert product_name_in_store == product_name_in_cart, "The item name in cart is not matched"


    def item_price_should_matched(self):
    	product_price_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE).text
    	product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART).text
    	assert product_price_in_store == product_price_in_cart , "The item price in cart is not matched"



   