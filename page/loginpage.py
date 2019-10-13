from time import sleep
from base.genrics import Genrics
from base.genricscreenshot import getScreenShot

class LoginPage(Genrics):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    usn_text_field='username'
    pwd_text_field='pwd'
    login_button='loginButton'

 # ************************************************************************
    def enterUsername(self,username):
        #self.getUsernameTextField().send_keys(username)
        self.sendData('id',self.usn_text_field,username)

    def enterPassword(self,password):
        #self.getPasswordTextField().send_keys(password)
        self.sendData('name',self.pwd_text_field,password)

    def clickLoginButton(self):
       # self.getLoginButton().click()
        self.clickOn('id',self.login_button)

# ************************************************************************

    def loginTest(self,usn,pwd):
        self.enterUsername(usn)
        self.enterPassword(pwd)
        self.clickLoginButton()

    def verifyLogin(self):
        expected_title='actiTIME - Enter Time-Track'
        sleep(3)
        actual_title=self.driver.title
        if expected_title != actual_title:
            getScreenShot(self.driver)
            assert expected_title==actual_title



 #************************************************************************
    '''def getUsernameTextField(self):
        return self.driver.find_element_by_id(self.usn_text_field)

    def getPasswordTextField(self):
        return self.driver.find_element_by_name(self.pwd_text_field)

    def getLoginButton(self):
        return self.driver.find_element_by_id(self.login_button)'''
