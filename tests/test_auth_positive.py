from settings import valid_email, valid_password, valid_phone, valid_ls, valid_login
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

#Проверка входа в систему с корректными данными Электронной почты и пароля
def test_auth_mail(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_email.send_keys(valid_email)
    page.input_password.send_keys(valid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/h1[1]'))).text == 'Вход и безопасность', 'Не перенаправлен на страницу ЛК'

#Проверка входа в систему с корректными данными Телефона и пароля
def test_auth_phone(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_phone.send_keys(valid_phone)
    page.input_password.send_keys(valid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/h1[1]'))).text == 'Вход и безопасность', 'Не перенаправлен на страницу ЛК'

#Проверка входа в систему с корректными данными Логина и пароля
def test_auth_login(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_login.send_keys(valid_login)
    page.input_password.send_keys(valid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/h1[1]'))).text == 'Вход и безопасность', 'Не перенаправлен на страницу ЛК'

#Проверка входа в систему с корректными данными Лицевого счета и пароля
def test_auth_ls(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_ls.send_keys(valid_ls)
    page.input_password.send_keys(valid_password)
    page.btn_enter.click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main[1]/div[1]/h1[1]'))).text == 'Вход и безопасность', 'Не перенаправлен на страницу ЛК'