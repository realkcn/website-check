# -*- coding: gbk -*-
import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

__author__ = 'kcn'

driver = webdriver.Firefox()

def start():
    driver.get("http://www.moofeel.com/forum.php")
    assert "磨坊" in driver.title

def login():
    elem = driver.find_element_by_id("ls_username")
    elem.send_keys("username")
    elem = driver.find_element_by_id("ls_password")
    elem.send_keys("password")
    time.sleep(5)
    submitbox = driver.find_element_by_css_selector("#lsform button[type=\"submit\"]")
    submitbox.click()

def goto_check():
    driver.get("http://www.moofeel.com/forum-96-1.html")
    assert "抢楼签到" in driver.title
    normalthreads = driver.find_elements_by_css_selector("#moderate th.new a")

    normalthread = normalthreads[0]
    print("click %s" % (normalthread.get_attribute("href")))
    normalthread.click()

def do_reply():
    editbox = driver.find_element_by_id("fastpostmessage")
    editbox.send_keys("每天签到身体好")

    submitbutton = driver.find_element_by_id("fastpostsubmit")
    submitbutton.submit()

def click_get():
    img = driver.find_element_by_css_selector("img[alt=\"回复帖子签到后，点这领取 3 磨币\"]")
    img.click()

start()
login()
goto_check()
do_reply()
time.sleep(2)
click_get()
driver.close()
driver.quit()