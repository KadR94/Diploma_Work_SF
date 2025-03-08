from settings import valid_email, valid_password, valid_phone, valid_ls, valid_login, invalid_phone_short
#import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

#Ремарка!
#Требуется пройти проверку (капча). Нужно ввести в ручную символы с картины во время функции time.sleep()

@pytest.fixture(autouse=True)
def auth_page(web_browser):
    return AuthPage(web_browser)


# Проверка нахождения на странице Восстановления пароля
def test_rec_pass_page_title(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='card-title']"))).text == 'Восстановление пароля', 'Неверный заголовок страницы восстановления пароля'


# Проверка отображения меню выбора типа ввода контактных данных
def test_rec_pass_tabs(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='t-btn-tab-phone']"))).text == 'Телефон', 'Отсутствует таб выбора восстановления пароля по номеру'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='t-btn-tab-mail']"))).text == 'Почта', 'Отсутствует таб выбора восстановления пароля по почте'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='t-btn-tab-login']"))).text == 'Логин', 'Отсутствует таб выбора восстановления пароля по логину'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='t-btn-tab-ls']"))).text == 'Лицевой счёт', 'Отсутствует таб выбора восстановления пароля по лицевому счету'


# Проверка отображения формы ввода "Номер" или "Логин" или "Почта" или “Лицевой счет”
def test_rec_pass_input_containers(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).text == 'Мобильный телефон' or 'Электронная почта' or 'Логин' or 'Лицевой счёт', 'Отсутствует форма ввода логина'


# Проверка отображения формы ввода "Капча"
def test_rec_pass_captcha(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//img[@class='rt-captcha__image']")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='captcha']")))


# Проверка отображения кнопки "Продолжить" и "Вернуться назад"
def test_rec_pass_reset_btn(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-back']")))


# Проверка формы выбора восстановления пароля, после введения телефона, почты, логина или ЛС
def test_rec_pass_methods(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='sms-reset-type']"))).text == 'По номеру телефона'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='email-reset-type']"))).text == 'По e-mail'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-cancel']")))