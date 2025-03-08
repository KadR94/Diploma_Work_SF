from .base import WebPage
from .elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(web_driver, url)

    btn_tab_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    btn_tab_email = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    btn_tab_login = WebElement(xpath='//*[@id="t-btn-tab-login"]')
    btn_tab_ls = WebElement(xpath='//*[@id="t-btn-tab-ls"]')

    input_phone = WebElement(xpath='//*[@id="username"]')
    input_password = WebElement(xpath='//input[@id="password"]')
    input_email = WebElement(xpath='//*[@id="username"]')
    input_login = WebElement(xpath='//*[@id="username"]')
    input_ls = WebElement(xpath='//*[@id="username"]')
    btn_enter = WebElement(xpath='//*[@id="kc-login"]')