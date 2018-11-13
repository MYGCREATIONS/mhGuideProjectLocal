# -*- encoding: utf-8 -*-
"""
Created on Fri Jun 15 18:19:59 2018

@author: mdcayoglu
"""

from lettuce import step
from Framework.pages.dashboardPage import Dashboard
from Framework.pages.adminPortalPage import Adminportal
from Framework.pages.variantPage import CreateVariant
from Framework.pages.settingsPage import Settings



dashboard = Dashboard()
admin = Adminportal()
variant = CreateVariant()
settings=Settings()



@step('I click on \[(.*)\]')
def clickSave(step, action):
    if action == 'save':
        dashboard.clickSaveButton()
    if action == 'confirm':
        dashboard.clickConfirmButton()
    if action == 'yes':
        dashboard.clickYesButton()

@step(u'When I click on the arrow for the case \[(.*)\]')
def expandDetails(step,case):
    dashboard.expandArrowByCase(case)


@step('Then Verify the \[(.*)\] \[(.*)\] in the expanded list')
def VerifyDetailsForCaseByExpandingArrrow(step,detail,expectedDetail):
    dashboard.verifyCaseDetailsOnExpandedArrow(detail,expectedDetail)


@step('I am in the \[(.*)\]')
def inPortal(step, action):
    if action == 'Reporter portal':
        assert dashboard.isTitleMatches()
    elif action == 'Admin portal':
        assert admin.isTitleMatches()
    elif action == 'Variants tab':
        assert dashboard.verifyVariantsTab()
    elif action == 'CVIs tab':
        assert dashboard.verifyCviTab()
    elif action == 'Dashboard':
        assert dashboard.verifyDashboard()
    else:
        print ("Step not defined")
        raise AssertionError


@step('I go to the \[(.*)\] tab')
def goToTab(step, action):
    if action == 'Dashboard':
        dashboard.goToDashboard()
    elif action == 'CVIs':
        dashboard.goToCviTab()
    elif action == 'Variants':
        dashboard.goToVariantsTab()
    elif action == 'Settings':
        dashboard.goToSettings()
    elif action == 'Prognostic & Diagnostic':
        dashboard.goToPrognosticDiagnosticTab()
    elif action == 'Filters and rulesets':
        settings.goToTab(action)
        settings.goToFiltersAndRulesets()
    elif action == 'Lineage and zygosity':
        settings.goToLineageAndZygosity()
    else:
        settings.goToTab(action)


@step('I expand the details \[(.*)\]')
def expandDetails(step, details):
    dashboard.goToExpandDetails()


@step('I click on the case \[(.*)\]')
def clickOnCase(step,case):
    dashboard.clickOntheCase(case)


@step('I click on \[(.*)\]')
def clickCreateOrAdd(step, action):
    if action == 'create add lab':
        dashboard.clickAddButton()
        admin.verifyAddLabMenu()
    if action == 'additional test results':
        dashboard.clickAddButton()
        variant.verifyManageAdditionalTestResults()
    if action == 'add another biomarker':
        variant.clickAddAnotherBiomarker()
    if action == 'create cvi':
        dashboard.clickCreateButton()


@step(u'I search for the case \[(.*)\] \[(.*)\]')
def i_go_to_the_case_casename(step, orgUnit, caseName):
    dashboard.justGoToCase(orgUnit, caseName)


@step(u'I see the case \[(.*)\]')
def thenVerifyCaseList(step,text):
    dashboard.verifyCaseList(text)


@step(u'I click on the \[(.*)\] tab')
def click_On_Tab(step,tab):
    dashboard.clickOnTab(tab)
