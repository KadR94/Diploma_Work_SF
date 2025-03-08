from settings import valid_email, valid_password, valid_login, valid_ls
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

#Проверка нахождения на странице Авторизации
def test_auth_page_title(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    auth_title = wait.until(EC.presence_of_element_located((By.ID, 'card-title')))
    assert auth_title.text == 'Авторизация', 'Неверный заголовок страницы авторизации'

#Проверка отображения выбора типа авторизации
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

#Проверка отображения формы ввода "Номер" или "Логин" или "Почта" или “Лицевой счет” и Пароля
def test_input_containers(auth_page, web_browser):
    #wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    assert page.input_email.text == 'Мобильный телефон' or 'Электронная почта' or 'Логин' or 'Лицевой счёт', 'Отсутствует форма ввода логина'
    assert page.input_password.text == 'Пароль', 'Отсутствует форма ввода пароля'

#Проверка отображения левой части страницы на соответствие данным в брифе
def test_page_left(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page_left = wait.until(EC.presence_of_element_located((By.ID, "page-left")))
    assert page_left.text == 'Личный кабинет' or 'Персональный помощник в цифровом мире Ростелекома'

#Проверка автоматической смены таба при вводе Электронной почты (По умолчанию при открытии страницы выбран таб ввода Телефона)
def test_auto_tab_change_email(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_email.send_keys(valid_email)
    page.input_password.click()
    tab_mail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-input__placeholder--top')))
    assert tab_mail.text == 'Электронная почта', 'Не происходит автоматический переход на другой таб'

#Проверка автоматической смены таба при вводе Логина (По умолчанию при открытии страницы выбран таб ввода Телефона)
def test_auto_tab_change_login(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_email.send_keys(valid_login)
    page.input_password.click()
    tab_mail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-input__placeholder--top')))
    assert tab_mail.text == 'Логин', 'Не происходит автоматический переход на другой таб'

#Проверка автоматической смены таба при вводе Лицевого счета (По умолчанию при открытии страницы выбран таб ввода Телефона)
def test_auto_tab_change_ls(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.input_email.send_keys(valid_ls)
    page.input_password.click()
    tab_mail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rt-input__placeholder--top')))
    assert tab_mail.text == 'Лицевой счёт', 'Не происходит автоматический переход на другой таб'