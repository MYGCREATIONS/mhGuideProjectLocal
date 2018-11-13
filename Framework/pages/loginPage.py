# -*- encoding: utf-8 -*-
from Framework.common.locators import LoginPageLocators
from features.terrain import *
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    
    def __init__(self):
        self.loginL = LoginPageLocators()

    def quickLogin(self):
        user = world.config['LOGINDATA']['USERNAME']
        password = world.config['LOGINDATA']['PASSWORD']
        world.browser.get(world.config['DEFAULT']['REPORTER_PORTAL'])
        usernameBox = explicitWaitVisibility(self.loginL.userBox)
        passwordBox = explicitWaitVisibility(self.loginL.passwordBox)
        loginButton = explicitWaitClickable(self.loginL.loginButton)
        usernameBox.send_keys(user)
        passwordBox.send_keys(password)
        loginButton.click()

    def typeUsername(self, username):
        explicitWaitVisibility(self.loginL.userBox).send_keys(username)

    def typePassword(self, password):
        explicitWaitVisibility(self.loginL.passwordBox).send_keys(password)

    def submitLogin(self):
        explicitWaitClickable(self.loginL.loginButton).click()

    def submitLoginFailed(self):
        explicitWaitClickable(self.loginL.loginButton).click()

    def getLabel(self):
        explicitWaitClickable(self.loginL.labelOfLogin).text()

    def quickLogin3LS(self):
        self.typeUsername(world.config['LOGINDATA']['USERNAME_3LS'])
        self.typePassword(world.config['LOGINDATA']['PASSWORD_3LS'])
        self.submitLogin()

    def quickLoginHGCP(self):
        self.typeUsername(world.config['LOGINDATA']['USERNAME_HGCP'])
        self.typePassword(world.config['LOGINDATA']['PASSWORD_HGCP'])
        self.submitLogin()

    def quickLoginHG(self):
        self.typeUsername(world.config['LOGINDATA']['USERNAME_HG'])
        self.typePassword(world.config['LOGINDATA']['PASSWORD_HG'])
        self.submitLogin()

    def verifyUser(self, desiredUser):
        userBox = explicitWaitVisibility(self.loginL.userBox)
        try:
            userBox.text == str(desiredUser)
        except AssertionError:
            raise Exception("Expected user is not logged in")