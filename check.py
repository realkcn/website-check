# -*- coding: gbk -*-
import time
import configparser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


__author__ = 'kcn'

driver = webdriver.Firefox()

config = configparser.ConfigParser()
with open('/etc/kcn.conf', 'r') as cfgfile:
    config.read_file(cfgfile)
    username = config.get('moofeel', 'username')
    password = config.get('moofeel', 'password')


def start():
    driver.get("http://www.moofeel.com/forum.php")
    assert "ĥ��" in driver.title


def login():
    count = 0
    elem = driver.find_element_by_id("ls_username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("ls_password")
    elem.send_keys(password)
    # �����¼������3��
    while count < 3:
        count += 1
        time.sleep(3)
        try:
            submitbox = driver.find_element_by_css_selector("#lsform button[type=\"submit\"]")
        except NoSuchElementException:
            break
        submitbox.click()
        try:
            nick = driver.find_element_by_css_selector("#um a[title=\"�����ҵĿռ�\"]")
            if (nick != None) and (nick.text == username):
                break
        except NoSuchElementException:
            continue
    if count >= 3:
        driver.save_screenshot("/tmp/mofangloginerror.jpg")
        print("login error")
        raise Exception


def goto_check():
    driver.get("http://www.moofeel.com/forum-96-1.html")
    assert "��¥ǩ��" in driver.title
    normalthreads = driver.find_elements_by_css_selector("#moderate th.new a")

    normalthread = normalthreads[0]
    # print("click %s" % (normalthread.get_attribute("href")))
    normalthread.click()


def do_reply():
    editbox = driver.find_element_by_id("fastpostmessage")
    editbox.send_keys("ÿ��ǩ�������")

    submitbutton = driver.find_element_by_id("fastpostsubmit")
    submitbutton.submit()


def click_get():
    credit = driver.find_element_by_id("hcredit_3")
    oldcredit = credit.text
    img = driver.find_element_by_css_selector("img[alt=\"�ظ�����ǩ���󣬵�����ȡ 3 ĥ��\"]")
    img.click()
    time.sleep(10)
    credit = driver.find_element_by_id("hcredit_3")
    newcredit = credit.text
    print("ĥ�Ҵ�%s������%s" % (oldcredit, newcredit))


start()
login()
goto_check()
do_reply()
time.sleep(2)
click_get()
driver.close()
driver.quit()