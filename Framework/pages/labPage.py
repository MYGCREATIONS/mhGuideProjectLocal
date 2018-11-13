# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:17:25 2018

@author: mdcayoglu
"""

from features.terrain import *
from Framework.common.locators import CreateLabLocators


class CreateLab:
    
    def __init__(self):
        self.cL = CreateLabLocators()

    def verifyNewLabCreated(self):
        explicitWaitVisibility(self.cL.verifierNewLabCreated)

    def createLab(self, i=0):
        explicitWaitVisibility(self.cL.labName).send_keys(world.data['labdata']['labname'])
        explicitWaitVisibility(self.cL.city).send_keys(world.data['labdata']['city'])
        explicitWaitVisibility(self.cL.state).send_keys(world.data['labdata']['state'])
        explicitWaitVisibility(self.cL.zipcode).send_keys(world.data['labdata']['zipcode'])
        explicitWaitVisibility(self.cL.street).send_keys(world.data['labdata']['street'])
        explicitWaitVisibility(self.cL.number).send_keys(world.data['labdata']['number'])
        explicitWaitVisibility(self.cL.country).send_keys(world.data['labdata']['country'])
        explicitWaitVisibility(self.cL.email).send_keys(world.data['labdata']['email'])
        explicitWaitVisibility(self.cL.labEmail).send_keys(world.data['labdata']['labemail'])
        explicitWaitVisibility(self.cL.website).send_keys(world.data['labdata']['website'])
        explicitWaitVisibility(self.cL.phone).send_keys(world.data['labdata']['phone'])
        explicitWaitVisibility(self.cL.fax).send_keys(world.data['labdata']['fax'])
        if i:
            explicitWaitVisibility(self.cL.browse).send_keys(world.data['labdata']['logo_path'])


