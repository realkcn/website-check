# -*- coding: gbk -*-
import time
import configparser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


__author__ = 'kcn'

def start(driver):
    driver.get("http://www.hdarea.co/login.php")
    assert "HDArea" in driver.title


def login(driver, username, password):
    count = 0
    elem = driver.find_element_by_css_selector("input[name=username]")
    elem.send_keys(username)
    elem = driver.find_element_by_css_selector("input[name=password]")
    elem.send_keys(password)
    # 点击登录，尝试3次
    while count < 3:
        count += 1
        time.sleep(3)
        submitbox = driver.find_element_by_css_selector("form[action=\"takelogin.php\"]  input[type=\"submit\"]")
        submitbox.click()
        try:
            url = driver.current_url
            if url.startswith("http://www.hdarea.co/index.php"):
                break
        except NoSuchElementException:
            continue
    if count >= 3:
        driver.save_screenshot("/tmp/mofangloginerror.jpg")
        print("login error")
        raise Exception


def checkit(driver):
    config = configparser.ConfigParser()
    with open('/etc/kcn.conf', 'r') as cfgfile:
        config.read_file(cfgfile)
        username = config.get('hdarea', 'username')
        password = config.get('hdarea', 'password')
    start(driver)
    login(driver, username, password)
