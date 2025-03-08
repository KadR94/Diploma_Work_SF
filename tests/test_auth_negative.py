from settings import invalid_email, invalid_password, invalid_phone, invalid_phone_short, invalid_login, invalid_ls
#import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage


@pytest.fixture(autouse=True)
def auth_page(web_browser):
    return AuthPage(web_browser)

#Проверка входа в систему с некорректными данными Телефона и пароля (ввод не зарегистрированного номера)
def test_auth_phone(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_phone.send_keys(invalid_phone)
    page.input_password.send_keys(invalid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный логин или пароль'


#Проверка входа в систему с некорректными данными Телефона и пароля (ввод номера не соотвествующего формата)
def test_auth_phone_short(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_phone.send_keys(invalid_phone_short)
    page.input_password.click()
    error_phone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username-meta"]')))
    assert error_phone.text == 'Неверный формат телефона'

#Проверка входа в систему с некорректными данными Электронной почты и пароля
def test_auth_mail(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_email.send_keys(invalid_email)
    page.input_password.send_keys(invalid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный логин или пароль'

#Проверка входа в систему с некорректными данными Логина и пароля
def test_auth_login(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_login.send_keys(invalid_login)
    page.input_password.send_keys(invalid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный логин или пароль'

#Проверка входа в систему с некорректными данными Лицевого счета и пароля
def test_auth_ls(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_ls.send_keys(invalid_ls)
    page.input_password.send_keys(invalid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный логин или пароль'