# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 08:30:21 2018

@author: mdcayoglu
"""

from Framework.common.locators import AdminportalLocators
from features.terrain import *


class Adminportal:

    def __init__(self):
        self.aL = AdminportalLocators()

    def verifyAddLabMenu(self):
        explicitWaitVisibility(self.aL.verifierAddLabMenu)

    def verifyLabEditorTab(self):
        explicitWaitVisibility(self.aL.verifierLabEditorTab)

    def verifyLabtestEditorTab(self):
        explicitWaitVisibility(self.aL.verifierLabtestEditorTab)

    def verifyOrgUnitEditorTab(self):
        explicitWaitVisibility(self.aL.verifierOrgUnitEditorTab)

    def verifyUserEditorTab(self):
        explicitWaitVisibility(self.aL.verifierUserEditorTab)

    def goToLabEditor(self):
        x = explicitWaitClickable(self.aL.labEditor)
        x.click()

    def goToLabtestEditor(self):
        x = explicitWaitClickable(self.aL.labtestEditor)
        x.click()

    def goToOrgUnitEditor(self):
        x = explicitWaitClickable(self.aL.orgunitEditor)
        x.click()

    def goToUserEditor(self):
        x = explicitWaitClickable(self.aL.userEditor)
        x.click()
