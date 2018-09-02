# -*- coding:utf-8 -*-
# 加入需要的python库:
# unittest为python的测试框架
# webdriver为python的selenium下的库
# sleep为睡眠时间，类似于lr的思考时间，页面停留，也可以直接写import time，但是用法就是time.sleep()
# os是为了创建目录time获取日期和时间

import unittest
from selenium import webdriver
from time import sleep
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 导入HTMLTestRunner库，这句也可以放在脚本开头
import HTMLTestRunner

#创建测试类LoginCase，用unittest的测试框架的格式
class LoginCase(unittest.TestCase):
    @classmethod
    def initPath(cls):
        '''
        初始化测试报告和截图的路径
        :return:
        '''
        #获取日期
        dates = time.strftime("%Y%m%d")
        #获取时间
        times = time.strftime("%Y%m%d%H%M%S")
        # 定义path为文件路径，目录级别，可根据实际情况自定义修改，并将其于测试类绑定
        cls.path = "%s\\%s\\%s\\%s\\" % (os.getcwd(), dates, "login", times)
        # 判断是否定义的路径目录存在，不能存在则创建
        if not os.path.exists(cls.path):
            os.makedirs(cls.path)

    @classmethod
    def setUpClass(cls):
        '''
        此方法仅调用一次，用于对测试的内容进行初始化
        :return:
        '''
        #启动chrome浏览器
        cls.dr=webdriver.Chrome()
        # 浏览器最大化
        cls.dr.maximize_window()
        #设置元素查找的超时时间
        cls.dr.implicitly_wait(20)
        #如果此测试不是通过__main__入口进入，则需要进行目录的初始化
        if not __name__=="__main__":
            cls.initPath()

    def login(self, username, password):
        '''
        登陆的主要测试方法，由测试方法调用
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        #需要测试的网页
        self.dr.get('https://passport.cnblogs.com/user/signin')
        #需要输入的用户名，变量名和方法中的一致，find_element_by_id('input1')为抓取到的用户名的输入框，用谷歌或者火狐F12可以抓取到
        self.dr.find_element_by_id('input1').send_keys(username)

        #需要输入的密码，变量名和方法中的一致，find_element_by_id('input2')为抓取到的密码的输入框
        self.dr.find_element_by_id('input2').send_keys(password)

        #点击登陆按钮，find_element_by_id('signin')为抓取到的登陆按钮，click()为点击事件

        self.dr.find_element_by_id('signin').click() #点击登陆按钮

        #如果密码或者用户名未输入，则不需要进入验证码输入步骤
        if not (password=='' or username==''):
            sleep(1)
            #获取极验控件
            check=self.dr.find_element_by_class_name('geetest_radar_tip')
            #点击极验控件
            check.click()
            #等待验证控件消失，这一步需要手动验证
            WebDriverWait(self.dr, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'geetest_radar_tip')))


        #定义测试方法，框架中测试方法以test_开头，底下引号中的中文会在报告中显示，利于清楚的知道测试目的
    def test_login_success(self):
        '''
        用户名，密码正确
        :return:
        '''
        #用户名、密码正确
        self.login('yk690520', 'yingke520_') #调用定义的login方法，传入正确用户名和密码
        sleep(1)
        #可以用get_screenshot_as_file方法用来截图，可自定义截图后的保存位置和图片命名
        user=self.dr.find_element_by_id("lnk_current_user")
        self.dr.get_screenshot_as_file(self.path+"login_success.jpg")

        #用assertTrue(x)方法来断言，登录成功后预期的值是否和定义的实际值一致
        self.assertEqual(user.text,'yk690520')

    def test_login_pwd_error(self):
        #用户名正确、密码不正确
        self.login('yk690520', '1') #正确用户名，错误密码
        tips=self.dr.find_element_by_id('tip_btn')
        self.dr.get_screenshot_as_file(self.path+"login_password_error.jpg")
        self.assertIn('用户名或密码错误',tips.text) #用assertIn(a,b)方法来断言


    def test_login_pwd_null(self):

        #用户名正确、密码为空
        self.login('1', '') #密码为空
        sleep(1)
        tips = self.dr.find_element_by_id('tip_input2')
        self.dr.get_screenshot_as_file(self.path+"login_password_null.jpg")
        self.assertEqual(tips.text,'请输入密码') #用assertEqual(a,b)方法来断言

    def test_login_user_error(self):
        #用户名错误、密码正确
        self.login('1', 'yingke520_') #密码正确，用户名错误
        tips=self.dr.find_element_by_id('tip_btn')
        self.dr.get_screenshot_as_file(self.path+"login_username_error.jpg")
        self.assertIn('用户不存在',tips.text) #用assertIn(a,b)方法来断言 a in b

    def test_login_user_null(self):

        #用户名为空、密码正确
        self.login('', '1') #用户名为空，密码正确
        sleep(1)
        tips=self.dr.find_element_by_id('tip_input1')
        self.dr.get_screenshot_as_file(self.path+"login_username_null.jpg")
        self.assertEqual(tips.text,'请输入登录用户名') #用assertEqual(a,b)方法来断言

    #每个test_执行完执行一次tearDown()方法
    def tearDown(self):
        sleep(1)
        #refresh()方法为刷新浏览器
        self.dr.refresh()


    @classmethod
    def tearDownClass(cls):
        '''
        此方法将被调用一次，用来关闭浏览器
        :return:
        '''
        cls.dr.quit()

if __name__=="__main__":
    # 定义脚本标题，加u为了防止中文乱码
    report_title = u'登陆模块测试报告'
    # 定义脚本内容，加u为了防止中文乱码
    desc = u'博客园登陆模块测试报告详情：'
    # 定义date为日期，time为时间
    # 定义报告文件路径和名字，路径为前面定义的self.path，名字为report（可自定义），格式为.html
    LoginCase.initPath()
    print(LoginCase.path)
    report_path = "%s%s" % (LoginCase.path, "report.html")
    # 定义一个测试容器
    testsuite = unittest.TestSuite()
    # 将测试用例添加到容器
    testsuite.addTest(LoginCase("test_login_success"))
    testsuite.addTest(LoginCase("test_login_pwd_error"))
    testsuite.addTest(LoginCase("test_login_pwd_null"))
    testsuite.addTest(LoginCase("test_login_user_error"))
    testsuite.addTest(LoginCase("test_login_user_null"))
    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(report, title=report_title, description=desc)
        runner.run(testsuite)
