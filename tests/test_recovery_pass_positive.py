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

# Проверка восстановления пароля с помощью Телефона
def test_rec_pass_phone(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='sms-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()

    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='otp-code-timeout']")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-cancel']"))).text == 'Вернуться назад'
    time.sleep(25)  # Данное время дается для ввода кода из СМС

    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='card-title']"))).text == 'Восстановление пароля', 'Переход на страницу Восстановления пароля не осуществлен'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))) #Поиск поля ввода нового пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))) #Поиск поля ввода подтверждения нового пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).text == 'Сохранить', 'Кнопка сохраненеия нового пароля не найдена'
    time.sleep(25)  # Данное время дается для ввода нового пароля. Использую 12345Qwerty (видоизменяю цифры)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()

# Проверка восстановления пароля с помощью Электронной почты
def test_rec_pass_mail(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='email-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()

    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='otp-code-timeout']")))
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-cancel']"))).text == 'Вернуться назад'
    time.sleep(25)  # Данное время дается для ввода кода из Почты

    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='card-title']"))).text == 'Восстановление пароля', 'Переход на страницу Восстановления пароля не осуществлен'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))) #Поиск поля ввода нового пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))) #Поиск поля ввода подтверждения нового пароля
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).text == 'Сохранить', 'Кнопка сохраненеия нового пароля не найдена'
    time.sleep(25)  # Данное время дается для ввода нового пароля. Использую 12345Qwerty (видоизменяю цифры)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()