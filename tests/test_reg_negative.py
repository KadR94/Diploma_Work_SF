import time

from selenium.webdriver import Keys

from settings import new_valid_email, valid_password, new_valid_login, new_valid_ls, name, last_name
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
def test_registration(auth_page):
    wait = WebDriverWait(auth_page._web_driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='kc-register']"))).click() #Переход на страницу регистрации
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='register']"))).click() #Нажать кнопку "Зарегистрироваться с пустыми полями"
    # Ожидание появления ошибки при пустом поле "Имя"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[1]/span"))).text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', 'Не выдала ошибку поля "Имя"'

    # Ожидание появления ошибки при пустом поле "Фамилия"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/span"))).text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', 'Не выдала ошибку поля "Фамилия"'

    # Ожидание появления ошибки при пустом поле "Регион"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[2]/div/span"))).text == 'Укажите регион', 'Не выдала ошибку поля "Регион"'

    # Ожидание появления ошибки при пустом поле "E-mail или мобильный телефон"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[3]/div/span"))).text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru', 'Не выдала ошибку поля "E-mail или мобильный телефон"'

    # Ожидание появления ошибки при пустом поле "Пароль"
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))).text == 'Длина пароля должна быть не менее 8 символов', 'Не выдала ошибку поля "Пароль"'

    # Ожидание появления ошибки при пароле без заглавной буквы
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys('12345qwerty') #Заполнение поля "Пароль" без заглавной буквы
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))).text == 'Пароль должен содержать хотя бы одну заглавную букву', 'Не выдала ошибку с паролем без заглавной буквы'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ожидание появления ошибки при пароле с использованием кириллицы
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys('12345йцукен')  # Заполнение поля "Пароль" кириллицей
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))).text == 'Пароль должен содержать только латинские буквы', 'Не выдала ошибку с паролем с ипользованием кириллицы'
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(Keys.SHIFT + Keys.HOME + Keys.BACKSPACE)

    # Ожидание появления ошибки при не совпадении пароля и подтверждения пароля
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys('12345Qwerty')  # Заполнение поля "Пароль"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys('12345Qwert') # Заполнение поля "Подтверждение пароля" отличающимся паролем
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='register']"))).click()
    assert wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/span"))).text == 'Пароли не совпадают', 'Не выдала ошибку о несовпадении паролей'


