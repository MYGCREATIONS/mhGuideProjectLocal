__author__ = 'sbedework'
#########################################################################
# The simple script accepts the query.txt file and searches all the sql #
# script between the start and of the query tag                         #
#########################################################################
import re
import sys
import os


class FileExtract:
    # The function extracts the SQL file based on the BEGIN, FINISH delimiter
    @staticmethod
    def get_the_sql(input_file):
        with open(input_file) as fp:
            for result in re.findall('BEGIN(.*?)FINISH', fp.read(), re.S):
                return result

    # The function accepts the file and replace the place holder with the new data set version.

    @staticmethod
    def get_the_NCT(input_file):
        with open(input_file) as fp:
            for result in re.findall('THEIDSTART(.*?)THEIDFINISH', fp.read(), re.S):
                return result

    @staticmethod
    def parameter_insert(input_file, dataset_placeholder, dataset_version):
        if not os.path.isfile(input_file):
            print ("Error replacing, it is not a regular file: " + input_file)
            sys.exit(1)
        f1 = open(input_file, 'r').read()
        f2 = open(input_file, 'w')
        m = f1.replace(dataset_placeholder, dataset_version)
        f2.write(m)
        for line in f1:
            if line.strip():
                f2.write(line)

    @staticmethod
    def getFirstSQL(inputFile):
        """
        text = open(inputFile, 'r').read()
        print("text: " + text)
        result = re.search('FIRSTSQLSTART(.`?)FIRSTSQLFINISH', text)
        print("Result: " + result)
        """
        with open(inputFile) as fp:
            for result in re.findall('FIRSTSQLSTART(.*)FIRSTSQLFINISH', fp.read(), re.S):
                return result

    @staticmethod
    def getLastSQL(inputFile):
        with open(inputFile) as fp:
            for result in re.findall('LASTSQLSTART(.*?)LASTSQLFINISH', fp.read(), re.S):
                return result

    @staticmethod
    def getFeatureOnly(inputFile):
        with open(inputFile) as fp:
            for result in re.findall('FEATURESTART(.*?)FEATUREFINISH', fp.read(), re.S):
                return result
