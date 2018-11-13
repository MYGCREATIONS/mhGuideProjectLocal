# -*- encoding: utf-8 -*-
"""
Created on Fri Jul 13 13:27:57 2018

@author: mdcayoglu
"""
from lettuce import step
from Framework.pages.settingsPage import Settings

settings = Settings()


@step("I am in the global settings tab")
def verifyGlobalSettings(step):
    settings.verifyGlobalSettingsTab()


# @step("I go to the [\[(.*)\] tab")
# def tabInGlobalSettings(step,tab):
#     settings.got
#


@step(u"I am in the variant filter tab")
def verifyVariantFilter(step):
    settings.verifyVariantFilterTab()


@step(u"I am under Variant filter in the \[(.*)\] tab")
def verifyInSpecificTab(step, tabName):
    settings.verifyInSpecificTabOfVariantFilter(tabName)


@step(u"The default \[(.*)\] in Lineage and Zygosity of \[(.*)\] is \[(.*)\]")
def checkDefaultValueInLineageAndZygosity(step, decision, valueName, expectedValue):
    if valueName == "Assign Germline if a dbSNP entry is available or skip the check":
        assert settings.checkDefaultAssignGermlineValueInLineageAndZygosity(expectedValue)
    elif valueName == "Variant lineage":
        assert settings.checkDefaultVariantLineageInLineageAndZygosity(expectedValue)
    elif valueName == "Set the variant to" or valueName == "Otherwise, set the variant to":
        assert settings.checkDefaultValueLineageFilterColourbar(valueName, expectedValue)
    else:
        assert settings.checkDefaultValueInLineageAndZygosity(valueName, expectedValue)


@step(u"The default value in CVI match quality of \[(.*)\] is \[(.*)\]")
def checkDefaultValueInCVIMatchQuality(step, valueName, expectedValue):
    if valueName.startswith("Enter the labtest target region size"):
        assert settings.checkDefaultValueInLabtestProperties()
    elif valueName == "Consider for CVI matching":
        assert settings.checkDefaultConsiderForCVIMatching(expectedValue)
    else:
        assert settings.checkDefaultValueInCVIMatching(valueName, expectedValue)


@step(u"The default value in Lineage and Zygosity of \[(.*)\] is between \[(.*)\] and \[(.*)\]")
def checkDefaultValueOfAssignGermlineBetweenAF(step, valueName, expectedValueLower, expectedValueUpper):
    assert settings.checkDefaultAssignGermlineValueBetweenRange(expectedValueLower, expectedValueUpper)


@step(u"The default value in Labtest properties of \[(.*)\] is \[(.*)\]")
def checkDefaultValueInLabtestProperties(step, valueName, expectedValue):
    assert settings.checkDefaultValueInLabtestProperties(valueName, expectedValue)


@step(u"The default checkbox in \[(.*)\] of \[(.*)\] is ticked \[(.*)\]")
def checkDefaultCheckboxStatusLineageFilter(step, inWhat, valueName, status):
    assert settings.checkDefaultValueLineageFilterAndPolymorphismFilter(valueName, status)


@step(u"I can see a \[(.*)\] tab")
def checkTabExists(step, tabName):
    assert settings.verifyTabExistsInSettings(tabName)


@step(u"I can see an explanation text of \[(.*)\]")
def checkExpText(step, expText):
    assert settings.checkExpText(expText)


@step(u"I can see only \[(.*)\] \[(.*)\] button")
def checkAmountOfSaveButtons(step, amount, buttonType):
    if buttonType == 'save':
        assert settings.checkAmountOfSaveButton(amount)
    if buttonType == 'cancel':
        assert settings.checkAmountOfCancelButton(amount)
    if buttonType == 'ok':
        assert settings.checkAmountOfOkButton(amount)


@step("I can see a back button under the MH-Guide logo")
def checkUnderMHGuideLogo(step):
    assert settings.verifyBackButtonUnderLogo()


@step("When I expand the details with org unit \[(.*)\] and labtest configuration \[(.*)\]")
def expandDetails(step, orgUnit, labtestConfig):
    settings.expandDetails(orgUnit, labtestConfig)


@step("I click on the back button")
def clickBackButton(step):
    settings.clickBackButton()


@step("I switch \[(.*)\] the \[(.*)\] slider")
def switchFilterSlider(step, status, slider):
    if slider == 'Lineage filter':
        settings.changeLineageFilterStatus(status)


@step("the \[(.*)\] slider is \[(.*)\]")
def checkSliderStatus(step, slider, status):
    if slider == 'Lineage filter':
        assert settings.checkSliderStatusLineageFilter(status)
    else:
        assert False


@step("I change under \[(.*)\] the value of \[(.*)\] to \[(.*)\]")
def changeValueInFilter(step, filterName, valueName, newValue):
    if filterName == 'False positive filter':
        if valueName == 'Matching CVI available':
            settings.changeValueMatchingCVIAvailable(newValue)
        else:
            settings.changeValueInFalsePositiveFilter(valueName, newValue)
    elif filterName == 'Polymorphism filter':
        settings.changeValueInPolymorphismFilter(valueName, newValue)


@step(u"I change the checkbox value of \[(.*)\] to \[(.*)\]")
def changeCheckboxValue(step, impact, status):
    settings.changeStatusOfCheckbox(impact, status)


@step(u"I change the value of \[(.*)\] to between \[(.*)\] and \[(.*)\]")
def changeValueBetweenLowerUpper(step, filterName, lowerValue, upperValue):
    settings.changeValueInVariantFilterLower(filterName, lowerValue)
    settings.changeValueInVariantFilterUpper(filterName, upperValue)


@step(u"I check under \[(.*)\] that the value of \[(.*)\] is \[(.*)\]")
def checkValueInFilter(step, filterName, valueName, expectedValue):
    if filterName == 'False positive filter':
        if valueName == 'Matching CVI available':
            assert settings.checkMatchingCVIAvailable(expectedValue)
        else:
            assert settings.checkDefaultValueInFalsePositiveFilter(valueName, expectedValue)
    elif filterName == 'Polymorphism filter':
        assert settings.checkDefaultValueInPolymorphismFilter(valueName, expectedValue)


@step(u"I check that the checkbox value of \[(.*)\] is \[(.*)\]")
def checkCheckboxValue(step, impact, status):
    assert settings.checkDefaultValueLineageFilterAndPolymorphismFilter(impact, status)


@step(u"I check that the value of \[(.*)\] is between \[(.*)\] and \[(.*)\]")
def checkValueBetweenLowerUpper(step, filterName, lowerValue, upperValue):
    assert settings.checkValueInVariantFilter(filterName, lowerValue, upperValue)
    