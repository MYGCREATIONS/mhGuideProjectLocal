# -*- encoding: utf-8 -*-
"""
Created on Fri Jun 22 15:19:28 2018

@author: mdcayoglu
"""

from lettuce import step
from Framework.pages.variantPage import CreateVariant
from Framework.pages.dashboardPage import Dashboard

variant = CreateVariant()
dashboard = Dashboard()


@step(u"a new menu manage additional test results shows up")
def inManageAdditionalTestResults(step):
    assert variant.verifyManageAdditionalTestResults()


@step(u"I create a new \[(.*)\] variant")
def createNewVariant(step, variantName):
    variant.createVariant(variantName)


@step(u"the new variant is successfully created")
def verifyVariantCreated(step):
    variant.verifyVariantCreated()


@step(u'I check for the gene \[(.*)\] with variant \[(.*)\] to exist')
def checkForVariant(step, geneName, variantName):
    assert dashboard.verifyVariantList(geneName, variantName)

"""
@step(u'I click on the variant information bar of (?P<geneName>.+) with variant (?P<variantName>.+)')
def clickVariantInformationBar(step, geneName, variantName):
    variant.clickVariantInformationBar(geneName, variantName)

@step(u'I check the variant relevance details for \[(.*?)\], match \[(.*?)\] and value \[(.*?)\]')
def checkVariantRelevanceDetails(step, attributeName, match, value):
    assert variant.checkVariantRelevanceDetails(attributeName, match, value)


@step(u'I see that the \[(.*?)\] Variant count is \[(.*?)\]')
def checkVariantCount(step, name, value):
    if name == 'displayed':
        assert variant.getDisplayedVariantsCount(value)
"""