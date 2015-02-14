# -*- coding: gbk -*-
import time
import configparser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


__author__ = 'kcn'

def checkit(driver):
    print("测试中文")
