# -*- encoding=utf8 -*-
__author__ = "yk690"

from airtest.core.api import *

auto_setup(__file__)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//a[@href='http://news.baidu.com']").click()
driver.switch_to_new_tab()
driver.find_element_by_xpath("//a[@href='http://sports.cctv.com/']").click()
driver.switch_to_new_tab()



from poco.drivers.android.uiautomation import AndroidUiautomationPocopoco("com.tencent.mm:id/an3")

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
