__author__ = 'sbedework'
import glob
import shlex
import os
from lettuce.bin import main as lettuce
from packages.sqlExecuter import SqlExecuter
from packages.target_process import Target_Process

tp = Target_Process()


def run_lettuce(args):
    status = 1
    if type(args) == str:
        args = shlex.split(args)

        try:
            letRes = lettuce(args)
            # Lettuce always raises a SystemExit, so something bad
            # has happened.  Fail.
            print "Test"
            print str(letRes)
        except SystemExit as e:
            status = e.code
        finally:
            return status


'''
we can isolate the test case ID from the feature file name. eg: 58700.feature, and you get: 58700
'''
testCaseID = [os.path.basename(c).split('.')[0:1][0] for c in glob.glob('features/*.feature')]
'''
feature name:all .feature extensions in the /features directory
'''
featureName = [os.path.basename(c) for c in glob.glob('features/*.feature')]
sqlFiles = [os.path.basename(c) for c in glob.glob('features/*.txt')]
sqlStartFiles = [element for element in sqlFiles if element.startswith('start')]
sqlEndFiles = [element for element in sqlFiles if element.startswith('end')]
print featureName
os.chdir("features")

sql = SqlExecuter()
for feature in featureName:
    name = feature.split('.')
    testCaseID = name[0]
    print("testCaseID: ", testCaseID)
    sqlToStart = filter(lambda x: testCaseID in x, sqlStartFiles)
    print("Sql to start: ", sqlToStart)
    if len(sqlToStart) > 0:
        sql.executeSQLCommand(sqlToStart[0])
    status = run_lettuce(feature)
    sqlToEnd = filter(lambda x: testCaseID in x, sqlEndFiles)
    if len(sqlToEnd) > 0:
        sql.executeSQLCommand(sqlToEnd[0])
    tp.update_testPlan_runs(status, 'TestCaseRuns', testCaseID)
print("Finished testing and updating the run results")
