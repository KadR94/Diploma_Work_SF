from settings import valid_email, valid_password, invalid_email, invalid_password
#import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage


@pytest.fixture(autouse=True)
def auth_page(web_browser):
    return AuthPage(web_browser)

def test_auth_page_title(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    auth_title = wait.until(EC.presence_of_element_located((By.ID, 'card-title')))
    assert auth_title.text == 'Авторизация', 'Неверный заголовок страницы авторизации'

def test_auth_tabs(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    tab_phone = wait.until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
    tab_mail = wait.until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    tab_login = wait.until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
    tab_ls = wait.until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
    assert tab_phone.text == 'Телефон', 'Отсутствует таб выбора аутентификации по номеру'
    assert tab_mail.text == 'Почта', 'Отсутствует таб выбора аутентификации по почте и паролю'
    assert tab_login.text == 'Логин', 'Отсутствует таб выбора аутентификации по логину и паролю'
    assert tab_ls.text == 'Лицевой счёт', 'Отсутствует таб выбора аутентификации по лицевому счету и паролю'

def test_input_containers(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    input_container_login = wait.until(EC.presence_of_element_located((By.ID, "username")))
    input_container_pass = wait.until(EC.presence_of_element_located((By.ID, "password")))
    assert input_container_login.text == 'Мобильный телефон' or 'Электронная почта' or 'Логин' or 'Лицевой счёт', 'Отсутствует форма ввода логина'
    assert input_container_pass.text == 'Пароль', 'Отсутствует форма ввода пароля'

def test_page_left(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page_left = wait.until(EC.presence_of_element_located((By.ID, "page-left")))
    assert page_left.text == 'Личный кабинет' or 'Персональный помощник в цифровом мире Ростелекома'

def test_auto_tab_change(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    tab_mail = wait.until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    page = AuthPage(web_browser)
    page.input_email.send_keys(valid_email)
    page.input_password.click()

def sfhjg()
    #assert input_container_login. == 'Пароль', 'Отсутствует форма ввода пароля'
    #Нужно написать проверку того, что tab_mail имеет измененное значение
