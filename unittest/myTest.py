import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTest(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.brower=webdriver.Chrome()




    def test_01(self):

        pass