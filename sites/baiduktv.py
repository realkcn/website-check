# -*- coding: utf-8 -*-
import time, random
import configparser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from . import CheckBase


class BaiduKTV(CheckBase.CheckBase):
    """ class for baidu ktv download
    """

    username = None
    password = None
    url = None

    # def __init__(self, driver):
    #     CheckBase.__init__(self, driver)

    def login(self):
        with self.driver as driver:
            driver.get("http://yun.baidu.com/")
            element = driver.find_element_by_id("TANGRAM__PSP_4__userName")
            element.send_keys(self.username)
            element = driver.find_element_by_id("TANGRAM__PSP_4__password")
            element.send_keys(self.password)
            element = driver.find_element_by_id("TANGRAM__PSP_4__submit")
            element.click()
            count = 0
            while count < 3:
                count += 1
                time.sleep(3)
                try:
                    element = driver.find_element_by_id("TANGRAM__PSP_4__userName")
                except NoSuchElementException:
                    break
            if count == 3:
                driver.save_screenshot("/tmp/baiduloginerror.jpg")
                print("login error")
                raise Exception

    def checkit(self, config):
        self.username = config.get('baiduktv', 'username')
        self.password = config.get('baiduktv', 'password')
        self.url = config.get('baiduktv', 'url')

        self.driver.get(self.url)


def checkit(driver):
    object = BaiduKTV(driver)
    config = configparser.ConfigParser()
    with open('/etc/kcn.conf', 'r') as cfgfile:
        config.read_file(cfgfile)
        object.checkit()

