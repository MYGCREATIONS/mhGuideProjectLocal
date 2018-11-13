from features.terrain import *
from Framework.pages.dashboardPage import Dashboard
from Framework.common.locators import CreateCviLocators, DashboardLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep


class CreateCvi:

    def __init__(self):
        self.cviL = CreateCviLocators
        self.dashboard = Dashboard()
        self.dashL = DashboardLocators

    def verifyCviCreated(self):
        explicitWaitVisibility(self.cviL.verifierCviCreated)

    def verifyCreateANewCvi(self):
        explicitWaitVisibility(self.cviL.verifierCreateANewCvi)

    def expandDetailsCvi(self, status):
        expandArrow = self.cviL.parseExpandDetailsCvi(status)
        x = explicitWaitClickable(expandArrow)
        x.click()

    def clickPlusIcon(self):
        sleep(10)
        x = explicitWaitClickable(self.cviL.cviPlusIcon)
        x.click()

    """
    Functions all belong to create CVI here //start
    """

    def createCvi(self):
        size = len(world.cvidata)
        for x in world.cvidata:
            self.addNameToCvi(x)
            self.addDiseasesToCvi(x)
            self.addVariantsToCvi(x)
            self.addTreatmentsToCvi(x)
            self.addReferencesToCvi(x)
            self.addImpactToCvi(x)
            self.addNarrativeToCvi(x)
            self.addCommentToCvi(x)
            self.dashboard.clickSaveButton()
            self.verifyCviCreated()
            if size != 1:
                self.dashboard.clickCreateButton()
            size -= 1
            bigSleep()

    def addNameToCvi(self, cvi=None, name=None):
        if name is None:
            name = world.cvidata[cvi]["cvi_name"]
        x = explicitWaitVisibility(self.cviL.cviName)
        x.send_keys(name)

    def clickCheckBox(self):
        x = explicitWaitClickable(self.cviL.checkBox)
        x.click()

    def addVariantsToCvi(self, cvi):
        for x in world.cvidata[cvi]["variants"]:
            addButton = explicitWaitClickable(self.cviL.variantsAddButton)
            addButton.click()
            self.dashboard.typeSearch(x)
            self.clickCheckBox()
            okButton = explicitWaitClickable(self.dashL.okButton)
            okButton.click()

    def addDiseasesToCvi(self, cvi):
        for x in world.cvidata[cvi]["diseases"]:
            addButton = explicitWaitClickable(self.cviL.diseasesAddButton)
            addButton.click()
            self.dashboard.typeSearch(x)
            find_elem = None
            waitingShortening()  # shorten the implicit waiting for faster scrolling
            while not find_elem:
                i = 0
                while i < 3:
                    scrollElement = explicitWaitVisibility(self.cviL.scrollElement)
                    scrollElement.send_keys(Keys.NULL)
                    scrollElement.send_keys(Keys.PAGE_DOWN)
                    i = i + 1
                i = 0
                try:
                    explicitWaitPresence(self.cviL.passCviDiseases(x))
                except TimeoutException:
                    pass
            tempDisease = explicitWaitClickable(self.cviL.passTempDisease(x))
            tempDisease.click()
            waiting()  # set back the implicit waiting for the other tasks

    def addTreatmentsToCvi(self, cvi):
        z = explicitWaitClickable(self.cviL.treatmentsAddButton)
        z.click()
        for x in world.cvidata[cvi]["drug"]:
            z = explicitWaitVisibility(self.cviL.drug)
            z.clear()
            tinySleep()
            z.send_keys(x)
            tinySleep()
            z.send_keys(Keys.ARROW_DOWN)
            z.send_keys(Keys.ARROW_DOWN)
            z.send_keys(Keys.ENTER)
            explicitWaitClickable(self.dashL.addButton).click()
        for x in world.cvidata[cvi]["drug_class"]:
            z = explicitWaitVisibility(self.cviL.drugClass)
            z.clear()
            tinySleep()
            z.send_keys(x)
            tinySleep()
            z.send_keys(Keys.ARROW_DOWN)
            z.send_keys(Keys.ARROW_DOWN)
            z.send_keys(Keys.ENTER)
            explicitWaitClickable(self.dashL.addButton).click()
        y = str(world.cvidata[cvi]["amp_score"])
        z = str(world.cvidata[cvi]["cvi_score"])
        explicitWaitClickable(self.cviL.ampScore).click()
        ampValue = explicitWaitVisibility(self.cviL.passAmpValue(y))
        ampValue.click()
        explicitWaitClickable(self.cviL.cviScore).click()
        explicitWaitClickable(self.cviL.passCviValue(z)).click()
        explicitWaitClickable(self.dashL.createButton).click()

    def addReferencesToCvi(self, cvi):
        for x in world.cvidata[cvi]["references"]:
            x = explicitWaitClickable(self.cviL.referencesAddButton)
            x.click()
            self.dashboard.typeSearch(x)
            listedResult = explicitWaitClickable(self.cviL.listedResult)
            tinySleep()
            listedResult.click()

    def addImpactToCvi(self, cvi=None, impact=None):
        if impact is None:
            impact = world.cvidata[cvi]["impact"]
        impact = explicitWaitClickable(self.cviL.impact)
        impact.click()
        impactValue = explicitWaitClickable(self.cviL.passCviValue(impact))
        impactValue.click()

    def addNarrativeToCvi(self, cvi):
        narrative = world.cvidata[cvi]["narrative"]
        explicitWaitVisibility(self.cviL.narrativeBox).send_keys(narrative)

    def addCommentToCvi(self, cvi):
        comment = world.cvidata[cvi]["comment"]
        explicitWaitVisibility(self.cviL.commentBox).send_keys(comment)

        """
        Functions end here //end
        """
