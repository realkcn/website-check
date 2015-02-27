# -*- coding: gbk -*-
import time
import configparser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

__author__ = 'kcn'
def start(driver):
    driver.get("http://www.pt80.net/")
    assert "捌零音乐论坛" in driver.title

def isLogined(driver, username):
    try:
        nick = driver.find_element_by_css_selector("#um a[title=\"访问我的空间\"]")
        if nick and (nick.text == username):
            return True
        return False
    except NoSuchElementException:
        return False

def login(driver, username, password):
    count = 0
    elem = driver.find_element_by_id("ls_username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("ls_password")
    elem.send_keys(password)
    # 点击登录，尝试3次
    while True:
        count += 1
        time.sleep(3)
        try:
            submitbox = driver.find_element_by_css_selector("#lsform button[type=\"submit\"]")
            submitbox.click()
        except NoSuchElementException:
            if isLogined(driver, username):
                break
            if count >= 3:
                driver.save_screenshot("/tmp/mofangloginerror.jpg")
                print("login error")
                raise Exception

def dailydoit(driver):
    driver.get("http://www.pt80.net/plugin.php?id=dsu_paulsign:sign")

def checkit(driver):
    config = configparser.ConfigParser()
    with open('/etc/kcn.conf', 'r') as cfgfile:
        config.read_file(cfgfile)
        username = config.get('pt80', 'username')
        password = config.get('pt80', 'password')
    start(driver)
    login(driver, username, password)
    dailydoit(driver)
