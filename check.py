# -*- coding: utf-8 -*-
import sys, os
from selenium import webdriver
import sites
from sites import *
import io,time
from contextlib import redirect_stdout
from multiprocessing import Pool

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
            errorinfo = e
        finally:
            sys.stdout = sys.__stdout__
            print("%s output:" % sitename)
            content = buf.getvalue()
            print(content)
            if errorinfo:
                print("Exception: %s" % errorinfo)
    # driver = None

with Pool(processes=4) as pool:
    pool.map(checkit, sites.__all__)

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
