#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sbedework'
###################################################################################################
# The File Manager class does all the operations, reading, the extracted file from target process #
# Replacing parameters with the user input
###################################################################################################
import json
import HTMLParser
import itertools
import re
from bs4 import BeautifulSoup
from packages.target_process import Target_Process
import os.path as path
from fileParser import FileExtract

TAG_RE = re.compile(r'<[^>]+>')
NEW_LINE_RE = re.compile(r'[\r\n]')
QUERY_RE = re.compile(r'<sql>(.*)</sql>')


class FileManager:
    def task_manager(self, testCaseID):
        tp = Target_Process()
        html_parser = HTMLParser.HTMLParser()
        # if the passed ID consists only of numbers, we assume it is solely one test plan with test cases inside
        if testCaseID.isdigit():
            print("The Small Test Plan ID is " + testCaseID)
            listOfTestplans = [int(testCaseID)]
        # passed ID is an ID with letters to it (e.g. 12345big), we assume it is big test plan with test plans inside
        else:
            testCaseID = filter(lambda x: x.isdigit(), testCaseID)
            print("The Big Test Plan ID is " + str(testCaseID))
            listOfTestplans = tp.get_object_allTestplans(testCaseID)
        for x in listOfTestplans:
            mainTestPlan = tp.get_object_testplanRun('TestPlanRuns', x,
                                                     {'include': '[Id,TestCaseRuns[Id,TestCase], TestPlan[Name]]',
                                                       'format': 'json'})
            '''
            target process returns an xml object and we parse it using BeautifulSoup4
            and get the test plan name, ID, etc.
            '''
            soupXML = BeautifulSoup(mainTestPlan, "html.parser")
            testCaseElements = soupXML.findAll('testcaserun')
            toElement2 = soupXML.findAll('testcase')
            test_results = {}
            for elements, elem2run in itertools.izip(testCaseElements, toElement2):
                theID = str(elem2run['id'])
                testCaseRunID = str(elements['id'])
                testCaseName = str(elem2run['name'])
                response_str = tp.get_object_testcase('TestCases', theID, {'format': 'json'})
                response_obj = json.loads(response_str, encoding='utf8')
                description = html_parser.unescape(TAG_RE.sub('', (response_obj['Description'])))
                description = description.replace(u'\xa0', u'').lstrip()
                """
                To avoid having manual test cases here, it checks for the description to be manual.
                It filters out all characters that are not part of the alphabet.
                In our case: #manual -> manual (and no spaces left)
                """
                desc2 = description.split('\n')[0]
                desc2 = ''.join([x for x in desc2 if x.isalpha()])
                if desc2 == u'manual':
                    print("Skipping the manual test case: " + testCaseName)
                    continue
                elif desc2 == u'predictor':
                    print("Skipping the predictor test case: " + testCaseName)
                    continue
                # creating the "untouched" feature file
                location = path.abspath(path.join(__file__, "../../features/" + str(testCaseRunID) + ".feature"))
                sqlLocationStart = path.abspath(path.join(__file__, "../../features/startSQL" + str(testCaseRunID) +
                                                          ".txt"))
                sqlLocationEnd = path.abspath(path.join(__file__, "../../features/endSQL" + str(testCaseRunID) +
                                                        ".txt"))
                infile = open(location, 'w')
                infile.write(description.encode("utf-8"))
                infile.close()
                featureOnly = FileExtract.getFeatureOnly(location)
                if featureOnly is None:
                    # means there is no FEATURESTART/FEATUREFINISH -> thus no SQL statement
                    pass
                else:
                    # there is FEATURESTART/FEATUREFINISH -> thus SQL statement(s)
                    sqlStartFile = FileExtract.getFirstSQL(location)
                    sqlEndFile = FileExtract.getLastSQL(location)
                    if sqlStartFile is None:
                        # means there is no SQL start statement
                        pass
                    else:
                        sqlFile = open(sqlLocationStart, 'w')
                        sqlFile.write(sqlStartFile.encode("utf-8"))
                        sqlFile.close()
                        print("Added start SQL statement of {0}".format(testCaseName))
                        # TBD: Make the start file run before feature run
                    if sqlEndFile is None:
                        # means there is no SQL end statement
                        pass
                    else:
                        sqlFile = open(sqlLocationEnd, 'w')
                        sqlFile.write(sqlEndFile.encode("utf-8"))
                        sqlFile.close()
                        print("Added end SQL statement of {0}".format(testCaseName))
                        # TBD: Make the end file run after feature run
                    infile = open(location, 'w')
                    infile.write(featureOnly.encode("utf-8"))
                print("Added test case: " + testCaseName)
                infile.close()

        return test_results
