from selenium import webdriver
from time import sleep
from page.loginpage import LoginPage
import pytest
import unittest
from base import genricsxl

@pytest.mark.usefixtures('prePostMethod')
class TestDemo(unittest.TestCase):
    file_path="C:\\Users\\admin\\Desktop\\testdata.xlsx"
    pagename="Sheet2"

    @pytest.fixture(autouse=True)
    def classObj(self,prePostMethod):
        # create object for LopginPage class
        self.lp = LoginPage(self.driver)

    def testValidLogin(self):
        username=genricsxl.readData(self.file_path,self.pagename,0,0)
        password=genricsxl.readData(self.file_path,self.pagename,0,1)
        self.lp.loginTest(username,password)
        self.lp.verifyLogin()
        sleep(3)

    def testInvalidLogin(self):
        username = genricsxl.readData(self.file_path, self.pagename, 1, 0)
        password = genricsxl.readData(self.file_path, self.pagename, 1, 1)
        self.lp.loginTest(username,password)
        self.lp.verifyLogin()
        sleep(3)
















