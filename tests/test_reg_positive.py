import time

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
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']"))).send_keys(name) #Заполнение поля "Имя"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']"))).send_keys(last_name) #Заполнение поля "Фамилия"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange']"))).click() #Открытие всплявающего окна выбора региона
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[72]"))).click() #Выбор региона. В примере Республика Татарстан
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='address']"))).send_keys(new_valid_email) #Заполнение поля "E-mail или мобильный телефон"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(valid_password) #Заполнение поля "Пароль"
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(valid_password) #Заполнение поля "Подтверждение пароля"
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='register']"))).click() #Нажать кнопку "Зарегистрироваться"

    # Ожидание перехода на страницу ввода временного кода
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='card-title']"))).text == 'Подтверждение email', 'Не осуществлен переход по ссылке'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='otp-back']"))).text == 'Изменить email'
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='rt-code-input']"))) #Поиск поля ввода кода
    time.sleep(25) #Время для ввода кода из почты/СМС