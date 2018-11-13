# -*- encoding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    loginButton = (By.ID, '__component0---loginView0--loginButton-content')
    userBox = (By.ID, '__component0---loginView0--userId-inner')
    passwordBox = (By.ID, '__component0---loginView0--password-inner')
    labelOfLogin = (By.ID, '__xmlview1--toolbarLoggedUser')


class DashboardLocators(object):

    @staticmethod
    def verifyCaseList(case):
        return By.XPATH, "//a[@role='link' and contains(text(), '{0}')]".format(case)



    @staticmethod

    @staticmethod
    def verifyVariantList(variant):
        return By.XPATH, "//label[contains(text(), '{0}')]".format(variant)

    @staticmethod
    def passSpecificCase(caseName):
        return By.XPATH, "//a[@role='link' and contains(text(), '{0}')]".format(caseName)

    createButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Create')]")
    addButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Add')]")
    okButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'OK')]")
    goToDashboard = (By.ID, '__xmlview1--toolbarDashboardButton')
    yesButton = (By.XPATH, "//span[text()='Yes']")

    @staticmethod
    def parseGoToTab(tabName):
        return By.XPATH, "//div[text()='{0}']".format(tabName)


    @staticmethod
    def clickArrowByCase(case):
        return By.XPATH,"(//a[@role='link' and contains(text(), '{0}')]/parent::div/parent::div/parent::div/parent::div)[1]/parent::td/preceding-sibling::td/child::button".format(case)

    @staticmethod
    def CaseDetailsOnExpandedArrow(details):
        return By.XPATH,"//label[contains(text(),'{0}')]//following::div[1]//child::span".format(details)

    goToVariantsTab = (By.XPATH, "//div[contains(text(), 'Variants')]")
    goToCviTab = (By.XPATH, "//div[contains(text(), 'CVIs')]")
    goToPrognosticDiagnosticTab = (By.XPATH, "//div[contains(text(), 'Prognostic & Diagnostic')]")
    saveButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Save')]")
    cancelButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Cancel')]")
    editButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Edit')]")
    expandDetailsButton = (By.XPATH, "//span[@role='presentation' and @style='font-family:'SAP-icons']")
    searchField = (By.XPATH, "//input[@type='search' and @class='sapMSFI']")
    verifierVariantsTab = (By.XPATH, "//input[@placeholder = 'Search for variant']")
    verifierCviTab = (By.XPATH, "//input[@placeholder = 'Search CVI variants']")
    verifierDashboard = (By.XPATH, "//span[text()='Dashboard']")
    localBusy = (By.XPATH, "//div[@role = 'progressbar']")
    nextButton = (By.XPATH, "//button/child::span/child::span[contains(text(), 'Next')]")
    confirmButton = (By.XPATH, "//span[contains(text(), 'Confirm')]")
    goToSettings = (By.XPATH, "//a[@id='__xmlview1--toolbarSettingsButton']")


class SettingsLocators(object):
    globalSettingsTab = (By.XPATH, "//div[text()='Global settings']")
    verifierGlobalSettingsTab = (By.XPATH, "//span[contains(text(), 'APP_VERSION')]/parent::span")
    verifierGlobalSettingsTab1= (By.XPATH,"//span[contains(text(),'APP_VERSION']parent::span")
    verifierVariantFilterTab = (By.XPATH, "//div[@role='tab']/child::div[text()='SNV']")
    cviMatchQualityTab = (By.XPATH, "//div[text()='CVI match quality']")
    filtersRulesetsTab = (By.XPATH, "//div[text()='Filters and rulesets']")
    systemHistoryTab = (By.XPATH, "//div[text()='System history']")
    excludedVariantsTab = (By.XPATH, "//div[text()='Excluded variants']")
    accountSettingsTab = (By.XPATH, "//div[text()='Account settings']")
    customCvisTab = (By.XPATH, "//div[text()='Custom CVIs']")
    geneFiltersTab = (By.XPATH, "//div[text()='Gene filters']")
    lineageAndZygosityTab = (By.XPATH, "//div[text()='Lineage and zygosity']")
    backButtonUnderLogo = (By.XPATH,
                           "//a[@id='__xmlview1--toolbarLogoButton']/parent::div/parent::div/following-sibling::div[1]/child::div/child::section/child::div/child::div/child::button")
    scrollFiltersElement = (By.XPATH, "//tbody/child::tr")
    lineageFilterSliderFalse = (By.XPATH,
                                "//span[contains(text(), 'Lineage filter')]/parent::div/parent::div/following-sibling::div[1]/child::div/child::div/child::div[2]/child::div/child::div[@aria-checked='false']")
    lineageFilterSliderTrue = (By.XPATH,
                               "//span[contains(text(), 'Lineage filter')]/parent::div/parent::div/following-sibling::div[1]/child::div/child::div/child::div[2]/child::div/child::div[@aria-checked='true']")
    assignGermlineValue = (By.XPATH,
                           "//div[child::label[contains(text(), 'Assign Germline if a dbSNP entry is')]]/following-sibling::div[1]/child::div/child::div/child::div/child::label")
    assignGermlineBetweenLowerLimit = (By.XPATH,
                                       "//div[child::label[contains(text(), 'Assign Germline if the variant allele frequency in tumor [%] is within the following range')]]/following-sibling::div[3]/child::div/child::div/child::div/child::input")
    assignGermlineBetweenUpperLimit = (By.XPATH,
                                       "//div[child::label[contains(text(), 'Assign Germline if the variant allele frequency in tumor [%] is within the following range')]]/following-sibling::div[5]/child::div/child::div/child::div/child::input")
    lineageFilterVariantLineage = (By.XPATH,
                                   "//div[child::label[text()='Variant lineage']]/following-sibling::div[1]/child::span")
    considerForCVIMatching = (By.XPATH,
                              "//div[child::label[contains(text(), 'Consider for CVI matching')]]/following-sibling::div[1]/child::div/child::label")
    matchingCVIAvailable = (By.XPATH,
                            "//div[child::label[contains(text(), 'Matching CVI available')]]/following-sibling::div[1]/child::div/child::label")

    @staticmethod
    def verifierInSpecificTabOfVariantFilter(tabName):
        return (By.XPATH,
                "//div[@role='tab' and @class='sapMITBFilter sapMITBFilterDefault sapMITBItem sapMITBItemNoCount sapMITBVertical sapMITBSelected']/child::div[text()='{0}']"
                .format(tabName))

    @staticmethod
    def parseSpecificValueInVariantFilterLower(filterName):
        return (By.XPATH,
                "//h1[text()='{0}']/following-sibling::div/child::div/child::div[2]/child::div/child::input"
                .format(filterName))

    @staticmethod
    def parseSpecificValueInVariantFilterUpper(filterName):
        return (By.XPATH,
                "//h1[text()='{0}']/following-sibling::div/child::div/child::div[3]/child::div/child::input"
                .format(filterName))

    @staticmethod
    def parseSpecificValueInLabtestProperties(valueName):
        return (By.XPATH,
                "//div[child::label[contains(text(), '{0}')]]/following-sibling::div/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseSpecificValueInCVIMatchQuality(valueName):
        return (By.XPATH,
                "//div[child::label[contains(text(), '{0}')]]/following-sibling::div[1]/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseColourbarLineageFilter(valueName, colour):
        if colour == 'red':
            colourClass = 'sapMPIBar sapMPIBarNegative'
        elif colour == 'green':
            colourClass = 'sapMPIBar sapMPIBarPositive'
        else:
            return False, "Unknown colour"
        return (By.XPATH,
                "//label[text()='{0}']/parent::div/following-sibling::div[1]/child::div/child::div/child::div[@class='{1}']"
                .format(valueName, colourClass))

    @staticmethod
    def parseCheckboxStatus(valueName, status):
        if status == 'on':
            boxClass = 'sapMCbBg sapMCbHoverable sapMCbMark sapMCbMarkChecked'
        elif status == 'off':
            boxClass = 'sapMCbBg sapMCbHoverable sapMCbMark'
        else:
            print("Invalid status")
            return False
        return (By.XPATH,
                "//label[text()='{0}']/preceding-sibling::div[@class='{1}']".format(valueName, boxClass))

    @staticmethod
    def changeCheckbox(valueName, status):
        if status == 'on':
            boxClass = 'sapMCbBg sapMCbHoverable sapMCbMark'
        elif status == 'off':
            boxClass = 'sapMCbBg sapMCbHoverable sapMCbMark sapMCbMarkChecked'
        else:
            print("Invalid status")
            return False
        return (By.XPATH,
                "//label[text()='{0}']/preceding-sibling::div[@class='{1}']".format(valueName, boxClass))

    @staticmethod
    def parseSpecificValueInLineageAndZygosityFrequency(valueName):
        return (By.XPATH,
                "//div[child::label[contains(text(), '{0}')]]/following-sibling::div[1]/child::div/child::div/child::div/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseSpecificValueInFalsePositiveFilter(valueName):
        return (By.XPATH,
                "//div[parent::div[parent::div[parent::div[preceding-sibling::div[child::div[child::span[text()='False positive filter']]]]]] and child::label[contains(text(), '{0}')]]/following-sibling::div[1]/child::div/child::div/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseSpecificValueInPolymorphismFilter(valueName):
        return (By.XPATH,
                "//div[child::div[child::div[child::span[contains(text(), 'Polymorphism filter')]]]]/child::div/child::div/child::div/child::div/child::div/child::div[child::label[contains(text(), '{0}')]]/following-sibling::div[1]/child::div/child::div/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseSpecificValueInLineageAndZygosity(valueName):
        return (By.XPATH,
                "//div[child::label[contains(text(), '{0}')]]/following-sibling::div[1]/child::div/child::div/child::div/child::input"
                .format(valueName))

    @staticmethod
    def parseSpecificSettingsTab(settingsName):
        return By.XPATH, "//div[text()='{0}']".format(settingsName)

    @staticmethod
    def parseExpandArrowFiltersAndRulesets(orgUnit, labtestConfig):
        return (By.XPATH,
                "//span[contains(text(), '{0}')]/parent::td/following-sibling::td[1]/span[contains(text(), '{1}')]/parent::td/preceding-sibling::td[@class='xxAccordionRowButton sapMListTblCell']/child::button/child::span/child::span"
                .format(orgUnit, labtestConfig))

    @staticmethod
    def parseExplanationText(expText):
        return By.XPATH, "//span[text()='{0}']".format(expText)


class AdminportalLocators(object):
    verifierAddLabMenu = (By.XPATH, "//span[contains(text(), 'Create a new Lab')]")
    verifierLabEditorTab = (By.XPATH, "//input[@placeholder='Search for labs']")
    verifierLabtestEditorTab = (By.XPATH, "//input[@placeholder='Search Labtests']")
    verifierOrgUnitEditorTab = (By.XPATH, "//input[@placeholder='Search organizational units']")
    verifierUserEditorTab = (By.XPATH, "//input[@placeholder='Search for users]")
    labEditor = (By.XPATH, "//div[contains(text(), 'Lab Editor')]")
    labtestEditor = (By.XPATH, "//div[contains(text(), 'Labtest Editor')]")
    orgunitEditor = (By.XPATH, "//div[contains(text(), 'OrgUnit Editor')]")
    userEditor = (By.XPATH, "//div[contains(text(), 'User Editor')]")


class CreateLabLocators(object):
    verifierNewLabCreated = (By.XPATH, "//div[@role='alert' and contains(text(), 'New lab successfully created')]")
    browse = (By.XPATH, "//input[@type='file']")
    labName = (By.XPATH,
               "//label[contains(text(), 'Lab name')]/parent::div/following-sibling::div/child::div/child::div/child::div/child::input[@type='text']")
    city = (By.XPATH,
            "//label[contains(text(), 'City')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    state = (By.XPATH,
             "//label[contains(text(), 'State')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    zipcode = (By.XPATH,
               "//label[contains(text(), 'ZIP code')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    street = (By.XPATH,
              "//label[contains(text(), 'Street')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    number = (By.XPATH,
              "//label[contains(text(), 'Number')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    country = (By.XPATH,
               "//label[contains(text(), 'Country')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    email = (By.XPATH,
             "//label[contains(text(), 'Mail')]/parent::div/following-sibling::div/child::div/child::input[@type='email']")
    labEmail = (By.XPATH,
                "//label[contains(text(), 'Lab email for status mails')]/parent::div/following-sibling::div/child::div/child::input[@type='email']")
    website = (By.XPATH,
               "//label[contains(text(), 'Website')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    phone = (By.XPATH,
             "//label[contains(text(), 'Phone')]/parent::div/following-sibling::div/child::div/child::input[@type='tel']")
    fax = (By.XPATH,
           "//label[contains(text(), 'Fax')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")


class CreateVariantLocators(object):

    @staticmethod
    def parseGeneField(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::div/child::input[@placeholder='Enter gene...']"
                .format(biomarker))

    @staticmethod
    def parseVariantLineage(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Variant lineage')]/parent::div/following-sibling::div[1]/child::div/child::input[@type='text']"
                .format(biomarker))

    @staticmethod
    def parseAminoAcidPosition(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Amino acid position')]/parent::div/following-sibling::div/child::div/child::input[@type='number']"
                .format(biomarker))

    @staticmethod
    def parseAlternateAminoAcid(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Alternate amino acid')]/parent::div/following-sibling::div/child::div/child::input[@role='textbox']"
                .format(biomarker))

    @staticmethod
    def parseAlternateAminoAcidIns(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Alternate amino acid')]/parent::div/following-sibling::div/child::div/child::input"
                .format(biomarker))

    @staticmethod
    def parseHgvsVariantSymbol(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'HGVS variant symbol')]/parent::div/following-sibling::div/child::div/child::input[@type='text']"
                .format(biomarker))

    @staticmethod
    def parseCommentBox(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Enter a comment')]/parent::div/following-sibling::div/child::div/child::textarea[@rows='2']"
                .format(biomarker))

    @staticmethod
    def parseAssayType(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select an assay type')]/parent::div/following-sibling::div/child::div/child::input[@type='text']"
                .format(biomarker))

    @staticmethod
    def parseDetailedVariantType(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select the detailed variant type')]/parent::div/following-sibling::div/child::div/child::input[@type='text']"
                .format(biomarker))

    @staticmethod
    def parseFirstDeletedAminoAcid(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'First deleted amino acid')]/parent::div/following-sibling::div/child::div/child::input[@type='number']"
                .format(biomarker))

    @staticmethod
    def parseLastDeletedAminoAcid(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Last deleted amino acid')]/parent::div/following-sibling::div/child::div/child::input[@type='number']"
                .format(biomarker))

    @staticmethod
    def parsePrematureStopSlider(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Premature stop')]/parent::div/following-sibling::div/child::div/child::div"
                .format((biomarker)))

    @staticmethod
    def parseRearrangementOfGeneSlider(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Rearrangement of a gene')]/parent::div/following-sibling::div/child::div/child::div"
                .format(biomarker))

    @staticmethod
    def parseGeneFieldPartner(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::div/child::input[@placeholder='Enter fusion gene partner...']"
                .format(biomarker))

    @staticmethod
    def parseGeneFieldPartnerWild(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::div/child::input[@placeholder='Enter fusion partner gene...']"
                .format(biomarker))

    @staticmethod
    def parseDetailedTypeOfGeneExpression(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select the detailed type of gene expression')]/parent::div/following-sibling::div/child::div/child::input"
                .format(biomarker))

    @staticmethod
    def parseHgvsProteinVariant(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'HGVS protein variant')]/parent::div/following-sibling::div/child::div/child::input[@type='text']"
                .format(biomarker))

    @staticmethod
    def parseDetailedTypeOfMicrosatelliteInstability(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select the detailed type of microsatellite instability')]/parent::div/following-sibling::div/child::div/child::input"
                .format(biomarker))

    @staticmethod
    def parseDetailedTypeOfProteinExpression(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select the detailed type of protein expression')]/parent::div/following-sibling::div/child::div/child::input"
                .format(biomarker))

    @staticmethod
    def parseDetailedTypeOfTumorMutationalBurdern(biomarker):
        return (By.XPATH,
                "//h3[contains(@id, '{0}')]/following-sibling::div/child::div/child::div/child::div/child::label[contains(text(), 'Select the detailed type of tumor mutational burden')]/parent::div/following-sibling::div/child::div/child::input"
                .format(biomarker))

    verifierManageAdditionalTestResults = (By.XPATH, "//span[contains(text(), 'Manage additional test results')]")
    biomarkerType = (By.XPATH,
                     "//input[@class='sapMComboBoxInner sapMComboBoxTextFieldInner sapMComboBoxTextFieldInnerWidthExtraPadding sapMInputBaseInner' and @aria-autocomplete='both']")
    biomarkerTypeSelect = (By.XPATH,
                           "//label[containts(text(), 'Biomarker type')]/parent::div/following-sibling::div/child::div[@role='combobox']")
    verifierVariantCreated = (By.XPATH, "//div[contains(text(), 'Variant(s) successfully added') and @role='alert']")
    addAnotherBiomarker = (By.XPATH, "//span[contains(text(), 'Add another biomarker')]")


class VariantLocators(object):
    @staticmethod
    def parseVariantInformationBar(geneName, variantName):
        return (By.XPATH,
                "//div[child::a[contains(text(), '{0}')] and child::a[contains(text(), '{1}')]]//parent::div//parent::div/parent::td/following-sibling::td[2]//child::div[@role='progressbar']//child::div".format(
                    geneName, variantName))

    @staticmethod
    def checkRelevanceDetails(attributeName, match, value):
        if attributeName == 'None':
            attributeName = u''
        if match == 'positive' or match == 'negative':
            if match == 'positive':
                match = 'sapMPIBar sapMPIBarPositive'
            else:
                match = 'sapMPIBar sapMPIBarNegative'
            return (By.XPATH,
                    u"//tr[child::td/child::span[contains(text(), '{0}')] and child::td/child::div/child::div[@class='{1}'] and child::td/child::span[contains(text(), '{2}')]]".format(
                        attributeName, match, value))
        else:
            return (By.XPATH,
                    u"//tr[child::td/child::span[contains(text(), '{0}')] and child::td/span[contains(text(),'{1}')] and child::td/child::span[contains(text(), '{2}')]]".format(
                        attributeName, match, value))

    displayedVariantsCount = (By.XPATH, "//div[@role='toolbar']/child::span[3]")
    totalVariantsCount = (By.XPATH, "//div[@role='toolbar']/child::span[4]")


class CreateCviLocators(object):
    verifierCviCreated = (By.XPATH, "//div[contains(text(), 'The CVI was saved successfully')]")
    verifierCreateANewCvi = (By.XPATH, "//span[contains(text(), 'Create a new CVI')]")
    cviName = (By.XPATH, "//input[@placeholder='Enter the CVI name']")
    impact = (
        By.XPATH, "//label[contains(text(), 'Impact')]/parent::div/following-sibling::div/child::div/child::label")
    narrativeBox = (By.XPATH,
                    "//label[contains(text(), 'Narrative')]/parent::div/following-sibling::div/child::div/child::textarea[@rows='8']")
    commentBox = (By.XPATH,
                  "//label[contains(text(), 'Comment')]/parent::div/following-sibling::div/child::div/child::textarea[@rows='8']")
    variantsAddButton = (By.XPATH,
                         "//span[contains(text(), 'Variants')]/parent::div/following-sibling::button/child::span/child::span[@role='presentation']")
    diseasesAddButton = (By.XPATH,
                         "//span[contains(text(), 'Diseases')]/parent::div/following-sibling::button/child::span/child::span[@role='presentation']")
    treatmentsAddButton = (By.XPATH,
                           "//span[contains(text(), 'Treatments')]/parent::div/following-sibling::button/child::span/child::span[@role='presentation']")
    referencesAddButton = (By.XPATH,
                           "//span[contains(text(), 'References')]/parent::div/following-sibling::button/child::span/child::span[@role='presentation']")
    checkBox = (By.XPATH, "//input[@type='CheckBox']/parent::div")
    scrollElement = (By.XPATH, "//div[@data-sap-ui-fastnavgroup='true']")
    drug = (By.XPATH,
            "//label[contains(text(), 'Drug')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    drugClass = (By.XPATH,
                 "//label[contains(text(), 'Drug class')]/parent::div/following-sibling::div/child::div/child::input[@type='text']")
    ampScore = (By.XPATH,
                "//label[contains(text(), 'AMP score')]/parent::div/following-sibling::div/child::div/child::div")
    cviScore = (By.XPATH,
                "//label[contains(text(), 'CVI score')]/parent::div/following-sibling::div/child::div/child::div")
    listedResult = (By.XPATH, "//div[@class='sapMSLIDiv']/parent::div/parent::li")
    cviTabEffective = (By.XPATH, "//th[contains(text(),'Effective')]")
    cviTabIneffective = (By.XPATH, "//th[contains(text(), 'Ineffective')]")
    cviTabToxic = (By.XPATH, "//th[contains(text(),'Toxic')]")
    cviPlusIcon = (By.XPATH, "//button[@title='Add a custom CVI']/child::span/child::span")

    @staticmethod
    def passCviDiseases(disease):
        return By.XPATH, "//span[text()= '{0}']".format(disease)

    @staticmethod
    def passTempDisease(disease):
        return By.XPATH, "//span[text()='{0}']/parent::div/parent::div/parent::div/parent::td/parent::tr".format(
            disease)

    @staticmethod
    def parseExpandDetailsCvi(status):
        return (By.XPATH,
                "//th[contains(text(),'{0}')]/parent::tr/parent::thead/parent::table/parent::div/parent::td/preceding-sibling::td[@role='gridcell']"
                .format(status))

    @staticmethod
    def passAmpValue(value):
        return By.XPATH, "//li[starts-with(@id, '__item') and @role='option' and text()='{0}']".format(value)

    @staticmethod
    def passCviValue(value):
        return By.XPATH, "//li[starts-with(@id, '__item') and @role='option' and text()='{0}']".format(value)


class CreateLabtestLocators(object):
    pass


class CreateOrgUnitLocators(object):
    pass


class CreateUserLocators(object):
    pass


class OrderportalLocators(object):
    pass


class CreateOrderLocators(object):
    orgUnit = (By.XPATH, "//input[@placeholder='Select an organizational unit']")  # example ou-a
    invoice = (By.XPATH, "//input[@placeholder='Select an invoice']")  # example standard
    product = (By.XPATH,
               "//input[@placeholder='You can select a product for additional filtering']")  # example mh guide
    report = (By.XPATH, "//input[@placeholder='You can select a report for additional filtering']")  # example ivd
    createOrder = (By.XPATH, "//span[contains(text(), 'Create order')]")

    ###temporary locators start here
    @staticmethod
    def getCaseName():
        x = (By.ID, '__input0-inner')
        return str(x.__getattribute__('value'))

    @staticmethod
    def getOrgunit():
        x = (By.ID, '__input2-inner')
        return str(x.__getattribute__('value'))

    @staticmethod
    def getInvoice():
        x = (By.ID, '__input3-inner')
        return str(x.__getattribute__('value'))
    ###temporary locators end here