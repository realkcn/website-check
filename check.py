#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import traceback
import logging
import io
import argparse
from contextlib import redirect_stdout
from multiprocessing import Pool

from selenium import webdriver

import sites


__author__ = 'kcn'

def checkit(sitename):
    with io.StringIO() as buf, redirect_stdout(buf):
        errorinfo = None
        try:
            if sitename != "test":
                driver = webdriver.Firefox()
            else:
                driver = None
            eval(sitename + ".checkit(driver)")
        except Exception as e:
            errorinfo = traceback.format_exc()

        finally:
            sys.stdout = sys.__stdout__
            print("%s output:" % sitename)
            content = buf.getvalue()
            print(content)
            if errorinfo:
                print("Exception: %s" % errorinfo)
            else:
                print("成功")
            driver.close()
            driver.quit()
    # driver = None

# 使用一个名字为checkin的logger
logger = logging.getLogger('使用一个名字为checkin的logger')
# 设置logger的level为DEBUG
logger.setLevel(logging.DEBUG)
# 创建一个输出日志到控制台的StreamHandler
hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)
# 给logger添加上handler
logger.addHandler(hdr)

parser = argparse.ArgumentParser(description='checkin')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', default=False,
                    help='Enable debug info')
parser.add_argument('-m', '--module', nargs='+', dest='modules',
                    help='Special module should be run')

args = parser.parse_args()

if args.verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.ERROR)

if args.modules is not None and len(args.modules) > 1:
    for module in args.modules:
        print(module)
#        checkit(module)
else:
    with Pool(processes=4) as pool:
        print("all")
#        pool.map(checkit, sites.__all__)

# for site in sites.__all__:
    # child = os.fork()
    # if child == 0:
    #     with io.StringIO() as buf, redirect_stdout(buf):
    #         errorinfo = None
    #         try:
    #             checkit(site)
    #         except Exception as e:
    #             errorinfo = e
    #         finally:
    #             sys.stdout = sys.__stdout__
    #             print("%s output:" % site)
    #             print(buf.getvalue())
    #             if errorinfo:
    #                 print("Exception: %s" % e)
    # else:
    #     pid, status = os.waitpid(child, 0)
        # print("wait returned, pid = %d, status = %d" % (pid, status))
