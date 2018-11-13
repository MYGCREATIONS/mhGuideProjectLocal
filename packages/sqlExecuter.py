import psycopg2
import re

"""
Plan: 
1. Have another "#sql" in 1st line (if not manual or predictor)
3. Modify the way of getting the test cases by having some seperation like "FEATURE-BEGIN" and "FEATURE-END"
This way we write only the feature into the .feature files and can have SQL statements at beginning and end of test case
2. Extract the SQL statement via BEGIN/FINISH in the test case similar to API test cases
3. Run the SQL statement with connection to database here
4. Continue testing as usual
5. Run the SQL statement to undo the changes from 3 to continue as usual
"""


class SqlExecuter(object):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname='predictive_engine',
                                               host='hddc-pe-pg-qa.v1018.molecularhealth.net', user='dev',
                                               password='dev')
        except psycopg2.Error:
            raise Exception("I am unable to connect")
        self.cursor = self.connection.cursor()

    def executeSQLCommand(self, filePath):
        with open(filePath, 'r') as f:
            command1 = f.read()
        command = re.sub('^\s+', '', command1)

        sqlCommands = command.split(";")
        for command in sqlCommands:
            command = re.sub('^\s+', '', command)
            if command.startswith('update') or command.startswith('insert') or command.startswith('delete'):
                self.cursor.execute(command)
                self.connection.commit()
                print("SQL command executed successfully")
            elif 'select' in command and 'password' in command:
                self.cursor.execute(command)
                rows=self.cursor.fetchone()
                filePathPass= filePath
                filePathPass = re.sub('startSQL\d+', 'password', filePathPass)
                with open(filePathPass, 'w') as f:
                    f.write(rows[0])

    def executePasswordReset(self, command):
        self.cursor.execute(command)
        self.connection.commit()

    def executeSQLfetchall(self, command):
        self.cursor.execute(command)
        self.connection.commit()
        rows = self.cursor.fetchall()
        print("SQL command executed successfully")
        myUserRolesDB = {}
        for i in range((len(rows))):
            myUserRolesDB[rows[i][0]] = rows[i][1]
        return myUserRolesDB

    def executeSQLfetchone(self, command):
        self.cursor.execute(command)
        self.connection.commit()
        return (self.cursor.fetchone())[0]



