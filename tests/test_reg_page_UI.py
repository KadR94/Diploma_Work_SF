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

#Проверка нахождения на странице Регистрации
def test_auth_page_title(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='kc-register']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='card-title']"))).text == 'Регистрация', 'Неверный заголовок страницы регистрации'

#Проверка полей ввода данных
def test_auth_page_inputs(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='kc-register']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']"))) #Поиск поля ввода имени
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']"))) #Поиск поля ввода фамилии
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange']"))) #Поиск поля ввода региона
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='address']"))) #Поиск поля ввода Номера телефона или Электронной почты
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))) #Поиск поля ввода пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))) #Поиск поля ввода подтверждения пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='register']"))) #Поиск кнопки Зарегистрироваться
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='rt-auth-agreement-link']"))) #Поиск ссылки на политику конфиденциальности

#Проверка левой части страницы
def test_page_left(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='kc-register']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//section[@id='page-left']"))).text == 'Личный кабинет' or 'Персональный помощник в цифровом мире Ростелекома'