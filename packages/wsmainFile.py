from urllib2 import URLError

__author__ = 'sbedework'
###################################################################################################
# The File Manager class does all the operations, reading, the extracted file from target process #
# Replacing parameters with the user input
###################################################################################################
import json
import ConfigParser
import HTMLParser
import itertools
import requests
import re
import os.path as path

from bs4 import BeautifulSoup
from target_process import Target_Process
from fileParser import FileExtract

TAG_RE = re.compile(r'<[^>]+>')
NEW_LINE_RE = re.compile(r'[\r\n]')
QUERY_RE = re.compile(r'<sql>(.*)</sql>')


class WSFileManager:

    def build_uri_parameters(self, myinput):
        counter = 0
        uri = "?"
        data = json.loads(myinput)
        if 'parameters' not in data:
            return "?"
        for dest in data['parameters']:
            p_name = dest
            v_name = data['parameters'][dest]
            if counter > 0:
                uri = uri + "&" + p_name + "=" + str(v_name)
            else:
                uri = uri + p_name + "=" + str(v_name)
            counter = counter + 1
        return uri

    def wstask_manager(self, testCaseID):
        tp = Target_Process()
        html_parser = HTMLParser.HTMLParser()
        # if the passed ID consists only of numbers, we assume it is solely one test plan with test cases inside
        if testCaseID.isdigit():
            print("The small Test Plan ID is " + testCaseID)
            listOfTestPlans = [int(testCaseID)]
        # passed ID is an ID with letters to it (e.g. 12345big), we assume it is big test plan with test plans inside
        else:
            testCaseID = filter(lambda x: x.isdigit(), testCaseID)
            print("The Big Test Plan ID is " + str(testCaseID))
            listOfTestPlans = tp.get_object_allTestplans(testCaseID)
        for x in listOfTestPlans:
            mainTestPlan = tp.get_object_testplanRun('TestPlanRuns', x,
                                                     {'include': '[Id,TestCaseRuns[Id,TestCase], TestPlan[Name]]',
                                                      'format': 'json'})
            '''
            target process returns an xml object and we parse it using BeautifulSoup4
            and get the test plan name, ID, etc.
            '''
            soupXML = BeautifulSoup(mainTestPlan, "html.parser")
            testCaseElements = soupXML.findAll('testcaserun')
            tcElement2 = soupXML.findAll('testcase')
            test_results = {}
            for elements, elem2run in itertools.izip(testCaseElements, tcElement2):
                theID = str(elem2run['id'])
                testCaseRunID = str(elements['id'])
                testCaseName = str(elem2run['name'])
                response_str = tp.get_object_testcase('TestCases', theID, {'format': 'json'})
                response_obj = json.loads(response_str, encoding='utf8')
                description = html_parser.unescape(TAG_RE.sub('', (response_obj['Description'])))
                description = description.replace(u'\xa0', u' ').lstrip()
                """
                To avoid having non-predictor test cases here, it checks for the description to be manual.
                It filters out all characters that are not part of the alphabet.
                In our case: #manual -> manual (and no spaces left)
                """
                desc2 = description.split('\n')[0]
                desc2 = ''.join([x for x in desc2 if x.isalpha()])
                if desc2 == u'predictor':
                    print("Added the predictor test case: " + testCaseName)
                elif desc2 == u'manual':
                    print("Skipping the manual test case: " + testCaseName)
                    continue
                else:
                    print("Skipping the peUITest test case: " + testCaseName)
                    continue
                apiVersion = description.split('\n')[2]
                apiVersion = ''.join([x for x in apiVersion if x.isalpha()])
                if apiVersion not in ('parameters', 'prediction', 'graph'):
                    print("Invalid parameters detected")
                    continue
                configuration = ConfigParser.RawConfigParser()
                configuration.read(path.abspath(path.join(__file__, "../../Framework/common/config.ini")))
                infile = open(path.abspath(path.join(__file__, "../../features/" + str(testCaseRunID) + ".feature")),
                              'w')
                infile.write(description.encode("utf-8"))
                infile.close()
                infile = path.abspath(path.join(__file__, "../../features/"+ str(testCaseRunID) + ".feature"))
                lines = FileExtract.get_the_sql(infile)
                theTrial = FileExtract.get_the_NCT(infile.encode("utf-8"))
                jsonedTrial = json.loads(theTrial.encode("utf-8"))
                testCase = json.loads(lines.encode("utf-8"))
                data = {}
                try:
                    trial_id = jsonedTrial["nct_id"]
                    if apiVersion == "prediction":
                        '''
                        Trial Properties Web service Test prediction
                        '''
                        response = (requests.get(configuration.get('data', 'Predictweb_service_uri') + trial_id,
                                                 params=data)).json()
                    elif apiVersion == "graph":
                        '''
                        Reliability Graph ws
                        '''
                        uri_t = self.build_uri_parameters(theTrial)
                        if uri_t == "?":
                            response = (
                                requests.get(configuration.get('data', 'Predictweb_service_uri') + trial_id + '/reliability',
                                             params=data)).json()
                        else:
                            response = (
                                requests.get(
                                    configuration.get('data', 'Predictweb_service_uri') + trial_id + '/reliability' + uri_t,
                                    params=data)).json()

                    elif apiVersion == "parameters":
                        '''
                        Param ws
                        '''
                        uri_t = self.build_uri_parameters(theTrial)
                        if uri_t == "?":
                            response = (requests.get(configuration.get('data', 'param_service_uri') + trial_id +
                                                     '/parameters',
                                                     params=data)).json()
                        else:
                            response = (
                                requests.get(configuration.get('data', 'param_service_uri_pred') + trial_id + uri_t,
                                             params=data)).json()
                    else:
                        raise Exception("Given parameter for API version is unknown")
                except URLError as e:
                    if hasattr(e, 'reason'):
                        print('We failed to reach a server.')
                        print('Reason: ', e.reason)
                    elif hasattr(e, 'code'):
                        print('The server couldn\'t fulfill the request.')
                        print('Error code: ', e.code)
                    else:
                        pass
                responseData = response
                # check if the response contains the data in the testcase
                if testCase == responseData:
                    query_result = '1'
                    theResponse = str(responseData)
                    tp.wsupdate_testPlan_runs(query_result, 'TestCaseRuns', testCaseRunID, theResponse)
                else:
                    query_result = '0'
                    theResponse = str(responseData)
                    tp.wsupdate_testPlan_runs(query_result, 'TestCaseRuns', testCaseRunID, theResponse)
                testPLanName = 'testplan_name'
                test_results.update({theID: [query_result, testCaseName, testCaseRunID, testPLanName]})
        print("Finished testing API related test cases")
        return test_results
