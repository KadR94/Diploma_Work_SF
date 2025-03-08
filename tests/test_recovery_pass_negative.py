from settings import valid_email, valid_password, valid_phone, valid_ls, valid_login, invalid_phone_short
from selenium.webdriver import Keys
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
def test_rec_pass_phone_1(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='sms-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('123456')
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Неверный код. Повторите попытку'
    time.sleep(120)  #Переждать, пока не счетчик не дойдет до нуля
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('123456') #Ввод кода с "истекшим сроком действия"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Срок действия кода истёк. Пожалуйста, запросите код снова'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('qwerty')
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Неверный код. Повторите попытку'
    #Последняя проверка должна завершиться ошибкой, так как латиница не должна прописываться в поле и ошибка не должна появиться


def test_rec_pass_phone_2(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='sms-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()
    time.sleep(25)  # Данное время дается для ввода кода из СМС

    #Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль менее 8 символов. Должна быть ошибка "Длина пароля должна быть не менее 8 символов"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('Qwer')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('Qwer')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Длина пароля должна быть не менее 8 символов', 'Ошибка длины пароля'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль без заглавных букв. Должна быть ошибка "Пароль должен содержать хотя бы одну заглавную букву"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Пароль должен содержать хотя бы одну заглавную букву', 'Ошибка заглавной буквы'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль кириллицей. Должна быть ошибка "Пароль должен содержать только латинские буквы"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345йцукен')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345йцукен')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Пароль должен содержать только латинские буквы', 'Ошибка латиницы'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" разные пароли. Должна быть ошибка "Пароли не совпадают"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345Qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345ytrewQ')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-confirm-meta']"))).text == 'Пароли не совпадают', 'Ошибка совпадения паролей'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    time.sleep(20)
    # Ввести в поле "Пароль" и "Подтверждение пароля" пароль, который был уже применен предыдущие три раза. Должна быть ошибка "Этот пароль уже использовался, укажите другой пароль"
    # Как пример 12345Qwerty
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Этот пароль уже использовался, укажите другой пароль', 'Ошибка использования предыдущего пароля'


# Проверка восстановления пароля с помощью Электронной почты
def test_rec_pass_mail_1(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='email-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('123456')
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Неверный код. Повторите попытку'
    time.sleep(120)  #Переждать, пока не счетчик не дойдет до нуля
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('123456') #Ввод кода с "истекшим сроком действия"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Срок действия кода истёк. Пожалуйста, запросите код снова'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))).send_keys('qwerty')
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Неверный код. Повторите попытку'
    #Последняя проверка должна завершиться ошибкой, так как латиница не должна прописываться в поле и ошибка не должна появиться


def test_rec_pass_mail_2(auth_page, web_browser):
    wait = WebDriverWait(auth_page._web_driver, 5)
    page = AuthPage(web_browser)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys(valid_phone)
    time.sleep(25)  # Данное время дается для ввода капчи
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset']"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='email-reset-type']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='reset-form-submit']"))).click()
    time.sleep(25)  # Данное время дается для ввода кода из Почты

    #Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль менее 8 символов. Должна быть ошибка "Длина пароля должна быть не менее 8 символов"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('Qwer')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('Qwer')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Длина пароля должна быть не менее 8 символов'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль без заглавных букв. Должна быть ошибка "Пароль должен содержать хотя бы одну заглавную букву"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Пароль должен содержать хотя бы одну заглавную букву'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" новый пароль кириллицей. Должна быть ошибка "Пароль должен содержать только латинские буквы"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345йцукен')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345йцукен')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-new-meta']"))).text == 'Пароль должен содержать только латинские буквы'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ввести в поле "Пароль" и "Подтверждение пароля" разные пароли. Должна быть ошибка "Пароли не совпадают"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys('12345Qwerty')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345ytrewQ')
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='password-confirm-meta']"))).text == 'Пароли не совпадают'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-new']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    time.sleep(20)
    # Ввести в поле "Пароль" и "Подтверждение пароля" пароль, который был уже применен предыдущие три раза. Должна быть ошибка "Этот пароль уже использовался, укажите другой пароль"
    # Как пример 12345Qwerty
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='t-btn-reset-pass']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='form-error-message']"))).text == 'Этот пароль уже использовался, укажите другой пароль'
