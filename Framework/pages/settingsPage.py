# -*- encoding: utf-8 -*-
"""
Created on Fri Jul 13 13:20:14 2018

@author: mdcayoglu
"""

from Framework.common.locators import SettingsLocators, DashboardLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from features.terrain import *
from selenium.webdriver.common.action_chains import ActionChains


class Settings():

    def __init__(self):
        self.sL = SettingsLocators()
        self.dashL = DashboardLocators()

    def verifyTabExistsInSettings(self, tabName):
        explicitWaitVisibility(self.sL.parseSpecificSettingsTab(tabName))

    def verifyBackButtonUnderLogo(self):
        explicitWaitVisibility(self.sL.backButtonUnderLogo)

    def verifyGlobalSettingsTab(self):
        explicitWaitVisibility(self.sL.verifierGlobalSettingsTab)


    def verifyVariantFilterTab(self):
        explicitWaitVisibility(self.sL.verifierVariantFilterTab)

    def verifyInSpecificTabOfVariantFilter(self, tabName):
        explicitWaitVisibility(self.sL.verifierInSpecificTabOfVariantFilter(tabName))

    """
    checking functions /start
    """

    def checkExpText(self, varType):
        expText = world.settingsdata["explanationText"][varType]
        explicitWaitVisibility(self.sL.parseExplanationText(expText))

    def checkAmountOfSaveButton(self, amount):
        count = world.browser.find_elements(self.dashL.saveButton)
        try:
            assert len(count) == int(amount)
        except AssertionError:
            raise Exception("No equal amount")

    def checkAmountOfCancelButton(self, amount):
        count = world.browser.find_elements(self.dashL.cancelButton)
        try:
            assert len(count) == int(amount)
        except AssertionError:
            raise Exception("No equal amount")

    def checkAmountOfOkButton(self, amount):
        count = world.browser.find_elements(self.dashL.okButton)
        try:
            assert len(count) == int(amount)
        except AssertionError:
            raise Exception("No equal amount")

    def checkDefaultAssignGermlineValueBetweenRange(self, expectedValueLower, expectedValueUpper):
        realValueLower = float(
            explicitWaitVisibility(self.sL.assignGermlineBetweenLowerLimit).get_attribute("value"))
        realValueUpper = float(
            explicitWaitVisibility(self.sL.assignGermlineBetweenUpperLimit).get_attribute("value"))
        try:
            assert realValueLower == float(expectedValueLower)
            assert realValueUpper == float(expectedValueUpper)
        except AssertionError:
            raise Exception("No equal value")

    def checkValueInVariantFilter(self, valueName, expectedValueLower, expectedValueUpper):
        realValueLower = float(
            explicitWaitVisibility(self.sL.parseSpecificValueInVariantFilterLower(valueName)).get_attribute("value"))
        realValueUpper = float(
            explicitWaitVisibility(self.sL.parseSpecificValueInVariantFilterUpper(valueName)).get_attribute("value"))
        try:
            assert realValueLower == float(expectedValueLower)
            assert realValueUpper == float(expectedValueUpper)
        except AssertionError:
            raise Exception("No equal value")

    def checkMatchingCVIAvailable(self, expectedValue):
        realValue = explicitWaitVisibility(self.sL.matchingCVIAvailable)
        try:
            assert realValue.text == str(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultAssignGermlineValueInLineageAndZygosity(self, expectedValue):
        realValue = explicitWaitVisibility(self.sL.assignGermlineValue)
        try:
            assert realValue.text == str(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultVariantLineageInLineageAndZygosity(self, expectedValue):
        realValue = explicitWaitVisibility(self.sL.lineageFilterVariantLineage)
        try:
            assert realValue.text == str(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultConsiderForCVIMatching(self, expectedValue):
        realValue = explicitWaitVisibility(self.sL.considerForCVIMatching)
        try:
            assert realValue.text == str(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultValueInLabtestProperties(self, valueName, expectedValue):
        realValue = float(explicitWaitVisibility(
            self.sL.parseSpecificValueInLabtestProperties(valueName)).get_attribute("value"))
        try:
            assert realValue == float(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultValueInLineageAndZygosity(self, valueName, expectedValue):
        if valueName.startswith("Population frequency") or valueName.startswith("Assign Homozygous (Hom)"):
            element = explicitWaitVisibility(self.sL.parseSpecificValueInLineageAndZygosityFrequency(valueName))
        else:
            element = explicitWaitVisibility(self.sL.parseSpecificValueInLineageAndZygosity(valueName))
        realValue = float(element.get_attribute("value"))
        try:
            assert realValue == float(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultValueLineageFilterAndPolymorphismFilter(self, valueName, status):
        explicitWaitVisibility(self.sL.parseCheckboxStatus(valueName, status))
        return True

    def checkDefaultValueInCVIMatching(self, valueName, expectedValue):
        element = explicitWaitVisibility(self.sL.parseSpecificValueInCVIMatchQuality(valueName))
        realValue = float(element.get_attribute("value"))
        try:
            assert realValue == float(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkSliderStatusLineageFilter(self, status):
        waitingLess()
        if status == 'on':
            explicitWaitVisibility(self.sL.lineageFilterSliderTrue)
            waiting()
        if status == 'off':
            explicitWaitVisibility(self.sL.lineageFilterSliderFalse)
            waiting()
        else:
            raise Exception("Invalid status")

    def checkDefaultValueLineageFilterColourbar(self, valueName, expectedValue):
        explicitWaitVisibility(self.sL.parseColourbarLineageFilter(valueName, expectedValue))
        return True

    def checkDefaultValueInFalsePositiveFilter(self, valueName, expectedValue):
        element = explicitWaitVisibility(self.sL.parseSpecificValueInFalsePositiveFilter(valueName))
        realValue = float(element.get_attribute("value"))
        try:
            assert realValue == float(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    def checkDefaultValueInPolymorphismFilter(self, valueName, expectedValue):
        element = explicitWaitVisibility(self.sL.parseSpecificValueInPolymorphismFilter(valueName))
        realValue = float(element.get_attribute("value"))
        try:
            assert realValue == float(expectedValue)
        except AssertionError:
            raise Exception("No equal value")

    """
    checking functions /end
    """

    def goToTab(self, tabName):
        tab = explicitWaitClickable(self.sL.parseSpecificSettingsTab(tabName))
        tab.click()
        tinySleep()

    def goToCVIMatchQuality(self):
        qualityTab = explicitWaitClickable(self.sL.cviMatchQualityTab)
        qualityTab.click()

    def goToFiltersAndRulesets(self):
        filtersAndRulesetsTab = explicitWaitClickable(self.sL.filtersRulesetsTab)
        filtersAndRulesetsTab.click()

    def goToLineageAndZygosity(self):
        lineageAndZygosityTab = explicitWaitClickable(self.sL.lineageAndZygosityTab)
        lineageAndZygosityTab.click()


    def expandDetails(self, orgUnit, labtestConfig):
        element = self.sL.parseExpandArrowFiltersAndRulesets(orgUnit, labtestConfig)
        find_elem = None
        waitingShortening()
        tinySleep()
        actions = ActionChains(world.browser)
        explicitWaitVisibility(self.sL.scrollFiltersElement).send_keys(Keys.NULL)
        while not find_elem:
            i = 0
            while i < 3:
                actions.send_keys(Keys.PAGE_DOWN)
                actions.perform()
                #world.browser.find_element(self.sL.scrollFiltersElement).send_keys(Keys.PAGE_DOWN)
                i = i + 1
            i = 0
            try:
                find_elem = explicitWaitPresence(element)
            except TimeoutException:
                pass
        expandButton = explicitWaitClickable(element)
        expandButton.click()
        waiting()

    def changeLineageFilterStatus(self, status):
        waitingLess()
        if status == 'on':
            try:
                world.browser.find_element(self.sL.lineageFilterSliderTrue)
            except NoSuchElementException:
                slider = explicitWaitClickable(self.sL.lineageFilterSliderFalse)
                slider.click()
                waiting()
        if status == 'off':
            try:
                world.browser.find_element(self.sL.lineageFilterSliderFalse)
            except NoSuchElementException:
                slider = explicitWaitClickable(self.sL.lineageFilterSliderTrue)
                slider.click()
                waiting()

    def changeValueInFalsePositiveFilter(self, valueName, newValue):
        falsePositiveValue = explicitWaitVisibility(self.sL.parseSpecificValueInFalsePositiveFilter(valueName))
        falsePositiveValue.clear()
        falsePositiveValue.send_keys(newValue)
        try:
            assert falsePositiveValue.get_attribute("value") == int(newValue)
        except AssertionError:
            raise Exception("No equal value")

    def changeValueInPolymorphismFilter(self, valueName, newValue):
        polymorphismValue = explicitWaitVisibility(self.sL.parseSpecificValueInPolymorphismFilter(valueName))
        polymorphismValue.clear()
        polymorphismValue.send_keys(newValue)
        try:
            assert polymorphismValue.get_attribute("value") == int(newValue)
        except AssertionError:
            raise Exception("No equal value")


    def changeValueInVariantFilterLower(self, valueName, newValue):
        variantValue = explicitWaitVisibility(self.sL.parseSpecificValueInVariantFilterLower(valueName))
        variantValue.clear()
        variantValue.send_keys(newValue)
        try:
            assert variantValue.get_attribute("value") == int(newValue)
        except AssertionError:
            raise Exception("No equal value")


    def changeValueInVariantFilterUpper(self, valueName, newValue):
        variantValue = explicitWaitVisibility(self.sL.parseSpecificValueInVariantFilterUpper(valueName))
        variantValue.clear()
        variantValue.send_keys(newValue)
        try:
            assert variantValue.get_attribute("value") == int(newValue)
        except AssertionError:
            raise Exception("No equal value")

    def changeStatusOfCheckbox(self, valueName, status):
        waitingShortening()
        x = self.checkDefaultValueLineageFilterAndPolymorphismFilter(valueName, status)
        waiting()
        if x is not True:
            xpath = explicitWaitClickable(self.sL.changeCheckbox(valueName, status))
            xpath.click()
        explicitWaitVisibility(self.sL.parseCheckboxStatus(valueName, status))

    def changeValueMatchingCVIAvailable(self, newValue):
        xpath = self.sL.matchingCVIAvailable
        actions = ActionChains(world.browser)
        while world.browser.find_element(*xpath).text != newValue:
            world.browser.find_element(*xpath).click()
            world.tinySleep()
            actions.send_keys(Keys.ARROW_UP)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        try:
            assert world.browser.find_element(*xpath).text == newValue
        except AssertionError:
            raise Exception("No equal value")

    def clickBackButton(self):
        backButton = explicitWaitClickable(self.sL.backButtonUnderLogo)
        backButton.click()
