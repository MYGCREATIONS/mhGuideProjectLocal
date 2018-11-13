# -*- encoding: utf-8 -*-
"""
Created on Fri Jun 22 14:15:56 2018

@author: mdcayoglu
"""

from lettuce import step
from Framework.pages.loginPage import LoginPage

login = LoginPage()


@step("I am logged in")
def loggedIn(step):
    login.quickLogin()






