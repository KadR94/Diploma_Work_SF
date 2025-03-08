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
#После нескольких попыток может потребовать пройти проверку (капча). Нужно ввести в ручную символы с картины

@pytest.fixture(autouse=True)
def auth_page(web_browser):
    return AuthPage(web_browser)

#Проверка нахождения на странице Входа по временному коду
def test_auth_temp_ui(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-description"]'))).text == 'Укажите почту или номер телефона, на которые необходимо отправить код подтверждения'
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-title"]'))).text == 'Вход по временному коду'
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]')))
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]')))

#Проверка UI станицы отправки временного кода
def test_auth_temp_login_ui(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]'))).send_keys(valid_phone)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]'))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-title"]'))).text == 'Код подтверждения отправлен', 'Не найден Загаловок'
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp-code-form-description"]')))
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp-back"]'))).text == 'Изменить номер', 'Не найдена ссылка "Изменить номер"'
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-code-input"]')))
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp-code-timeout"]')))

#Вводим данные телефона для получения временного кода
def test_auth_temp_login(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]'))).send_keys(valid_phone)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]'))).click()
    time.sleep(30) #Данное время дается для получения по СМС временного кода и ее ввода в поле
    current_url = page.get_current_url()
    redirect_url = 'https://lk.rt.ru/#'
    assert redirect_url == current_url

#Проверка ввода неправильного временного кода
def test_auth_temp_login_incorrect_code(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]'))).send_keys(valid_phone)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-code-input"]'))).send_keys('123456')
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный код. Повторите попытку'

#Проверка ввода латиницы вместо цифр в поле временного кода. Данный тест должен провалиться
def test_auth_temp_login_latin_code(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]'))).send_keys(valid_phone)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-code-input"]'))).send_keys('abcdef')
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-error-message"]'))).text == 'Неверный код. Повторите попытку'

#Вводим данные телефона нестандартного формата (не хватает количество цифр в номере) для получения временного кода
def test_auth_temp_login_short_phone(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    page.get('https://lk.rt.ru/')
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address"]'))).send_keys(invalid_phone_short)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp_get_code"]'))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-meta"]'))).text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
