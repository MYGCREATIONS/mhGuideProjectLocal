# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:29:54 2018

@author: mdcayoglu
"""

from lettuce import step
from Framework.pages.labPage import CreateLab

lab = CreateLab()


@step('I type in example data \[(.*)\] a logo')
def typeDataForLabWithoutLogo(step, action):
    if action == "without":
        lab.createLab(0)
    if action == "with":
        lab.createLab(1)


@step('the new Lab is created')
def newLabCreated(step):
    lab.verifyNewLabCreated()
