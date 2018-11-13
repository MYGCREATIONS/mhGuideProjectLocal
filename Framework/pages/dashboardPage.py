# -*- encoding: utf-8 -*-
"""
Created on Fri Jun 08 17:39:58 2018

@author: mdcayoglu
"""

from Framework.common.locators import DashboardLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from features.terrain import *








class Dashboard():

    def __init__(self):
        self.dashL = DashboardLocators()

    def clickAddButton(self):
        bigSleep()
        addButton = explicitWaitClickable(self.dashL.addButton)
        addButton.click()

    def clickCreateButton(self):
        createButton = explicitWaitClickable(self.dashL.createButton)
        createButton.click()

    def clickSaveButton(self):
        saveButton = explicitWaitClickable(self.dashL.saveButton)
        saveButton.click()

    def clickCancelButton(self):
        cancelButton = explicitWaitClickable(self.dashL.cancelButton)
        cancelButton.click()

    def clickConfirmButton(self):
        confirmButton = explicitWaitClickable(self.dashL.confirmButton)
        confirmButton.click()

    def clickOkButton(self):
        okButton = explicitWaitClickable(self.dashL.okButton)
        okButton.click()

    def clickYesButton(self):
        yesButton = explicitWaitClickable(self.dashL.yesButton)
        yesButton.click()

    def typeSearch(self, text):
        searchField = explicitWaitClickable(self.dashL.searchField)
        searchField.clear()
        searchField.send_keys(text)
        searchField.send_keys(Keys.ENTER)

    def goToDashboard(self):
        dashboard = explicitWaitClickable(self.dashL.goToDashboard)
        dashboard.click()

    def goToSettings(self):
        settings = explicitWaitClickable(self.dashL.goToSettings)
        settings.click()

    def goToCase(self, orgUnit, caseName):
        if orgUnit == "none":
            text = caseName
        else:
            text = orgUnit + ":" + caseName
        self.typeSearch(text)
        case = explicitWaitClickable(self.dashL.passSpecificCase(text))
        case.click()


    def justGoToCase(self, orgUnit, caseName):
        if orgUnit == "none":
            text = caseName
        else:
            text = orgUnit + ":" + caseName
        self.typeSearch(text)


    def clickOntheCase(self,text):
        case = explicitWaitClickable(self.dashL.passSpecificCase(text))
        case.click()


    def goToSpecificTab(self, tabName):
        pass  # might be implemented

    def goToVariantsTab(self):
        variantsTab = explicitWaitClickable(self.dashL.goToVariantsTab)
        variantsTab.click()

    def goToCviTab(self):
        cviTab = explicitWaitClickable(self.dashL.goToCviTab)
        cviTab.click()

    def goToPrognosticDiagnosticTab(self):
        prognosticDiagnosticTab = explicitWaitClickable(self.dashL.goToPrognosticDiagnosticTab)
        prognosticDiagnosticTab.click()

    def goToExpandDetails(self):
        expandDetails = explicitWaitClickable(self.dashL.expandDetailsButton)
        expandDetails.click()


    def expandArrowByCase(self,case):
        expandArrow=explicitWaitClickable(self.dashL.clickArrowByCase(case))
        expandArrow.click()


    def verifyCaseDetailsOnExpandedArrow(self,details,expectedDetail):
        RealDetail= explicitWaitVisibility(self.dashL.CaseDetailsOnExpandedArrow(details))
        try:
            assert RealDetail.text == str(expectedDetail)
        except AssertionError:
            raise Exception("Values are not equal")


    def goToEdit(self):
        editTab = explicitWaitClickable(self.dashL.editButton)
        editTab.click()

    def verifyCaseList(self, text):
        explicitWaitVisibility(self.dashL.verifyCaseList(text))




    def verifyVariantList(self, geneName, variantName):
        wanted = geneName + ' ' + variantName
        self.typeSearch(str(wanted))
        try:
            world.browser.find_element(self.dashL.verifyCaseList(variantName))
        except NoSuchElementException:
            print("Variant has no TME")
            try:
                self.driver.find_element(self.dashL.verifyVariantList(variantName))
            except NoSuchElementException:
                return False
        return True

    def verifyVariantsTab(self):
        explicitWaitVisibility(self.dashL.verifierVariantsTab)

    def verifyCviTab(self):
        explicitWaitVisibility(self.dashL.verifierCviTab)

    def verifyDashboard(self):
        explicitWaitVisibility(self.dashL.verifierDashboard)



    def clickOnTab(self,tab):
        if tab == 'CVIs':
            tab=explicitWaitClickable(self.dashL.parseGoToTab(tab))
            tab.click()

        elif tab == 'Effective':
            tab = explicitWaitClickable(self.dashL.parseGoToTab(tab))
            tab.click()

        elif tab == 'Ineffective & Toxic':
            tab = explicitWaitClickable(self.dashL.parseGoToTab(tab))
            tab.click()

        elif tab == 'Prognostic & Diagnostic':
            tab = explicitWaitClickable(self.dashL.parseGoToTab(tab))
            tab.click()

        elif tab == 'Report':
            tab = explicitWaitClickable(self.dashL.parseGoToTab(tab))
            tab.click()

        else:
            raise Exception("Step not implemented")


