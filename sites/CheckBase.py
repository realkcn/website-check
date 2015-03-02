# -*- coding: utf-8 -*-
# FileName: CheckBase.py

import configparser


class CheckBase:
    """ class for baidu ktv download
    """

    def __init__(self, driver):
        self.driver = driver
        self.__class__

    def checkit(self, config):
        raise NotImplementedError('Should create the method function')

    def log(self, level, message):
        print(type(self) + ":" + message)

    def error(self, message):
        self.driver.save_screenshot("/tmp/" + type(self) +".jpg")
        print(message)
        raise Exception
