__author__ = 'sbedework'


# Parse the file

class myFileManuplator(object):
    @staticmethod
    def changeToList(theFile):
        with open(theFile) as f:
            theFirst = ("".join(line for line in f if not line.isspace())).splitlines()
        return theFirst

# ['Model\tversion', '02.07.18', 'Dataset\tversion 02.07.18', 'Report\tdate July\t26,\t2018', 'Creator', 'MHDEMO', 'NCT01497366', 'Phase\t3\tStudy\tof\tSofosbuvir\tand\tRibavirin', 'INFORMATION', 'Phase', 'Phase\t3', 'Conditions', 'Hepatitis\tC', 'Interventions', 'PEG\t::\tRBV\t::\tSofosbuvir', 'Study\tstart\tdate', 'December\t1,\t2011', 'Recruitement\tstatus', 'Completed', 'Lead\tsponsor', 'Gilead\tSciences', 'PREDICTION', 'SUCCESS', 'Calibrated\tprobability\t73.68%', 'Molecular\tHealth\tGmbH,\tKurfuersten-Anlage\t21,\t69115\tHeidelberg\t|\twww.molecularhealth.com\t|\t+49\t6221\t43851-150', 'Page\t1\tof\t1']