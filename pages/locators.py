from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class  LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, ".alert-info p:first-child strong")
    PRODUCT_PRICE_STORE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    MESSAGE_SUCCESS_ADD_PRODUCT_TO_CART = (By.CSS_SELECTOR, "#messages .alertinner strong")
