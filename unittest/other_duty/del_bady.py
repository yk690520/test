# -*- coding:utf-8 -*-
# 加入需要的python库:
# unittest为python的测试框架
# webdriver为python的selenium下的库
# sleep为睡眠时间，类似于lr的思考时间，页面停留，也可以直接写import time，但是用法就是time.sleep()
# os是为了创建目录time获取日期和时间

import unittest
from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def delate_bady():
    brower=webdriver.Chrome()
    brower.maximize_window()
    brower.implicitly_wait(15)
    brower.get('https://login.taobao.com/')
    print('请使用手机淘宝扫描登陆')
    brower.execute_script("alert('请在40秒内使用手机淘宝扫描登陆(该窗口5秒后自动消失）');")
    sleep(5)
    try:
        brower.switch_to.alert.accept()
    except:
        print('未找到窗口')
    WebDriverWait(brower,50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="J_SiteNavSeller"]/div[1]/span')))
    brower.find_element_by_xpath('//*[@id="J_SiteNavSeller"]/div[1]/span').click()
    print('点击出售中的宝贝')
    brower.find_element_by_partial_link_text('出售中的宝贝').click()
    while True:
        print('下架宝贝中')
        try:
            brower.find_element_by_id('J_onSaleCount_1')
        except:
            print('已经没有宝贝了')
            break
        sleep(2)
        brower.find_element_by_class_name('all-selector').click()
        brower.find_element_by_xpath('//*[@id="J_DataTable"]/div[2]/table/thead/tr[2]/td/div/button[2]').click()
    #删除宝贝
    brower.find_element_by_xpath('//*[@id="header"]/div/div/a').click()
    handler=brower.window_handles
    brower.switch_to.window(handler[-1])
    print('删除宝贝')
    allBaby=brower.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div[8]/div/div[2]/div/div/div[2]/ul/li/a/span[2]').text
    print('宝贝数为%s' % allBaby)
    if allBaby!='0':
        print('进入删除界面')
        brower.find_element_by_partial_link_text('等待上架的宝贝').click()
        handler = brower.window_handles
        brower.switch_to.window(handler[-1])
        while True:
            print('删除宝贝中')
            try:
                brower.find_element_by_id('J_onSaleCount_1')
            except:
                print('宝贝已删除完毕')
                break
            sleep(2)
            brower.find_element_by_id('all-select1').click()
            brower.find_element_by_xpath('//*[@id="J_DataTable"]/div[3]/table/tbody/tr/td/div/button[1]').click()
            sleep(1)
            brower.switch_to.alert.accept()

    brower.quit()

if __name__=='__main__':
    delate_bady()