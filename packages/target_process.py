__author__ = 'sbedework'
import urllib2
import urllib
import ConfigParser
import json
from lettuce import world
import os.path as path


# theConf = testConf()
#################################################################################
# The Target process class contains the get_object functions which will         #
# connect to the Target process using the rest API url,and the given parameters #
#################################################################################
class Target_Process():
    config = ConfigParser.RawConfigParser()
    config.read(path.abspath(path.join(__file__, "../../Framework/common/config.ini")))

    def __init__(self, tp_name=config.get('data', 'tp_uri'), thetok=config.get('data', 'toke')):
        self.data = []
        self.tp_uri = tp_name
        self.token = thetok

    def get_object(self, type, id, param={}):
        auth = self.token
        request = urllib2.Request(
            self.tp_uri + type + '/' + str(id) + '/TestCases/' + '?' + urllib.urlencode(param) + ';&take=100')
        request.add_header("Authorization", "Basic %s" % auth)
        response = urllib2.urlopen(request)

        return response.read()

    def get_object_testcase(self, type, id, param={}):
        auth = self.token
        request = urllib2.Request(self.tp_uri + type + '/' + str(id) + '?' + urllib.urlencode(param))
        request.add_header("Authorization", "Basic %s" % auth)
        response = urllib2.urlopen(request)
        return response.read()

    def get_object_testplan(self, type, id, param={}):
        auth = self.token
        request = urllib2.Request(
            self.tp_uri + type + '/' + str(id) + '/' + '?' + urllib.urlencode(param) + ';&take=100')
        request.add_header("Authorization", "Basic %s" % auth)
        response = urllib2.urlopen(request)
        print ("\ntest plan id: \t" + str(id) + "\n")
        return response.read()

    def get_object_allTestplans(self, id):
        auth = self.token
        request = urllib2.Request(
            "https://mhdevelopment.tpondemand.com/api/v2" + '/testplanruns/' + str(id) + '?' +
            'select={testPlanRuns}')
        request.add_header("Authorization", "Basic %s" % auth)
        response = urllib2.urlopen(request)
        print("\nTest plan run ID with different test plans inside: \t" + str(id) + "\n")
        temp = response.read()
        testing = json.loads(temp, encoding='utf8')
        # print(testing['items'][0]['testPlanRuns']['items'])
        # print("\n")
        # print(testing['items'][0]['testPlanRuns']['items'])
        allTestPlanIDs = []
        for x in testing['items'][0]['testPlanRuns']['items']:
            print(("Collected test plan " + x['name'] + " with ID " + str(x['id'])).encode('utf-8'))
            allTestPlanIDs.append(x['id'])
        print("The complete list of test plan IDs: " + str(allTestPlanIDs))
        return allTestPlanIDs

    def get_object_testplanRun(self, type, id, param={}):
        auth = self.token
        request = urllib2.Request(
            self.tp_uri + type + '/' + str(id) + '?' + urllib.urlencode(param) + ';&take=100')
        request.add_header("Authorization", "Basic %s" % auth)
        response = urllib2.urlopen(request)
        print ("\ntest plan run id: \t" + str(id) + "\n")
        return response.read()

    def update_testPlan_runs(self, finalResult, type, id, param={}):
        auth = self.token
        print finalResult
        if finalResult == 0:
            postData = {"Status": "Passed", "Comment": "Passed"}  # "It is successfully tested."}
        elif finalResult == 1:
            postData = {"Status": "Failed", "Comment": "Failed steps: " + ", ".join(repr(e) for e in world.stepsfailed)}
        else:
            postData = {"Status": "OnHold", "Comment": "TestCase Not executed"}
        request = urllib2.Request(
            self.tp_uri + type + '/' + str(id))
        request.add_header("Authorization", "Basic %s" % auth)
        request.add_header('Content-Type', 'application/json')
        data = json.dumps(postData)
        urllib2.urlopen(request, data)
        print ("\ntest result: \t" + str(id) + "\n")

    def wsupdate_testPlan_runs(self, finalResult, type, id, theresponse, param={}):
        # auth = base64.encodestring("%s:%s" % (self.user, self.password)).strip()
        auth = self.token
        if finalResult == '1':
            print("Test case passed")
            postdata = {"Status": "Passed", "Comment": theresponse}  # "It is successfully tested."}
        elif finalResult == '0':
            print("Test case failed")
            postdata = {"Status": "Failed", "Comment": theresponse}  # "TestCase failed,bug shall be created"
        else:
            postdata = {"Status": "OnHold", "Comment": "TestCase Not executed"}
        request = urllib2.Request(
            self.tp_uri + type + '/' + str(id))
        request.add_header("Authorization", "Basic %s" % auth)
        request.add_header('Content-Type', 'application/json')
        data = json.dumps(postdata)
        # response = urllib2.urlopen(request)
        response = urllib2.urlopen(request, data)
        print ("\ntest result: \t" + str(id) + "\n")
        # response = requests.post(url, data=json.dumps(payload), headers=headers)
