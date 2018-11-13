from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re
import os


def pdfToText(pdfName):
    # PDFMiner boilerplate
    resourceManager = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(resourceManager, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resourceManager, device)

    # Extract text
    fp = file(pdfName, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text


def convert_pdf_to_html(path):
    resourceManager = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = HTMLConverter(resourceManager, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(resourceManager, device)
    password = ""
    maxpages = 0  # is for all
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


def matchRegexSkipArrow(myRegexBase, myText):
    isArrow = True
    # print "myRegexBase: ", myRegexBase
    while isArrow:
        stringPattern = '([^#]*)'
        regexBuild = myRegexBase + stringPattern

        matched = re.search(regexBuild, myText)
        # print "matchRegexSkipArrow:",matched.group(1)
        if matched.group(1).decode("utf-8") != u'\u2192' or matched.group(1) == '':
            isArrow = False
        # print "matchRegexSkipArrow:",matched.group(1)
        # mydictParams['enrollmentNewlValue'] = matched.group(1)
        else:
            myRegexBase = myRegexBase + '[^#]*#*'

    myRegexBase = myRegexBase + '[^#]*#*'

    return myRegexBase, matched.group(1)


def getPDFFile(pdfName):
    pdfPath = os.path.abspath(os.path.join(__file__, "../../features/pdfFiles/{0}".format(pdfName)))
    return pdfPath


def getTrialProperties(pdfName):
    pdfNamePath = getPDFFile(pdfName)
    myText = pdfToText(pdfNamePath)
    myTextWoEol = re.sub('\n', '#', myText)
    myTextTrialProperties = re.search('(Model.*)Parameters', myTextWoEol)
    # Parameters
    paramtersText = re.search('Parameters(.*)Molecular\s+Health\s+GmbH', myTextWoEol)

    trialPropertiesRaw = myTextTrialProperties.group(1)
    myTextWoEolNoDouble1 = re.sub('\s+', ' ', trialPropertiesRaw)

    myTextWoEolNoDouble2 = re.sub('# #', '##', myTextWoEolNoDouble1)
    myTextWoEolNoDouble3 = re.sub('(##)+', '#', myTextWoEolNoDouble2)
    myTextWoEolNoDouble31 = re.sub('(::#)+', ':: ', myTextWoEolNoDouble3)
    print "myTextWoEolNoDouble3:: ", myTextWoEolNoDouble3

    myTextWoEolNoDouble4 = re.sub('Report date ', 'Report date#', myTextWoEolNoDouble31)
    myTextWoEolNoDouble5 = re.sub('Dataset version ', 'Dataset version#', myTextWoEolNoDouble4)

    trialPropDict = {}
    matched = re.search('Model version#([0-9]+\.[0-9]+\.[0-9]+)#', myTextWoEolNoDouble5)

    trialPropDict['Model version'] = matched.group(1)

    matched2 = re.search('#Dataset version#([0-9]+\.[0-9]+\.[0-9]+)#', myTextWoEolNoDouble5)

    trialPropDict['Dataset version'] = matched2.group(1)

    matched3 = re.search('#Report date#([A-z]+\s[0-9]+,\s+20[0-9]+)#', myTextWoEolNoDouble5)
    trialPropDict['Report date'] = matched3.group(1)

    # Creator#MHDEMO#
    matched4 = re.search('#Creator#([A-z]+)#', myTextWoEolNoDouble5)
    trialPropDict['Creator'] = matched4.group(1)

    # NCT01497366#
    matched5 = re.search('#(NCT[0-9]+)#', myTextWoEolNoDouble5)
    # print "NCT_ID:",matched.group(1)
    trialPropDict['NCT ID'] = matched5.group(1)

    # NCT01497366#Phase 3 Study of Sofosbuvir and Ribavirin#
    matched6 = re.search('#NCT[0-9]+#(.+)#Information#Phase#', myTextWoEolNoDouble5)
    trialPropDict['Title'] = re.sub('#', ' ', matched6.group(1))

    # Phase#Phase 3#
    matched7 = re.search('#Phase#([A-z]+\s[1-4]+)#', myTextWoEolNoDouble5)
    # print "Phase:", matched.group(1)
    trialPropDict['Phase'] = matched7.group(1)

    # Conditions#Hepatitis C#
    matched8 = re.search('#Conditions#([^#]+)#', myTextWoEolNoDouble5)
    trialPropDict['Conditions'] = matched8.group(1)

    # Interventions#PEG :: RBV :: Sofosbuvir#
    matched9 = re.search('#Interventions#([^#]+)#', myTextWoEolNoDouble5)
    trialPropDict['Interventions'] = matched9.group(1)

    # Study start date#December 1, 2011#
    matched10 = re.search('#Study start date#([A-z]+\s[0-9]+,\s+20[0-9]+)#', myTextWoEolNoDouble5)
    trialPropDict['Study start date'] = matched10.group(1)

    # Recruitment status#Completed#
    matched11 = re.search('#Recruitment\s+status#([^#]+)#', myTextWoEolNoDouble5)
    trialPropDict['Recruitment status'] = matched11.group(1)

    # Lead sponsor#Gilead Sciences#
    matched12 = re.search('#Lead sponsor#([^#]+)#', myTextWoEolNoDouble5)
    trialPropDict['Lead sponsor'] = matched12.group(1)

    # PREDICTION#SUCCESS#
    matched13 = re.search('Comment#([^#]+)#', myTextWoEolNoDouble5)
    if matched13.group(1) == '\xe2\x80\x94':
        trialPropDict['Comment'] = ""
    else:
        trialPropDict['Comment'] = matched13.group(1)

    # PREDICTION#SUCCESS#
    matched14 = re.search('Comment#[^#]+#Prediction#([^#]+)#Probability of success', myTextWoEolNoDouble5)
    trialPropDict['Prediction'] = matched14.group(1)

    # Calibrated probability 73.68%#
    matched15 = re.search('#Probability\s+of\s+success\s+([0-9]*\.*[0-9]*%)#', myTextWoEolNoDouble5)
    trialPropDict['Probability of success'] = matched15.group(1)
    print trialPropDict
    return trialPropDict


def getParametersTable(pdfName):
    pdfNamePath = getPDFFile(pdfName)
    myText = pdfToText(pdfNamePath)

    myTextWoEol = re.sub('\n', '#', myText)

    # Parameters
    paramtersText = re.search('Parameters(.*)Molecular\s+Health\s+GmbH', myTextWoEol)

    mydictParams = {}

    myTextWoEolDouble = re.sub('\s+', ' ', paramtersText.group(1))

    myTextWoEolDouble = re.sub('# #', '##', myTextWoEolDouble)

    # Enrollment#
    matched = re.search('#(Enrollment[^#]+)#', myTextWoEolDouble)

    mydictParams['Enrollment label'] = matched.group(1)

    # TrialDurationLabel#
    matched = re.search('#(Trial[^#]+)#', myTextWoEolDouble)

    mydictParams['Duration label'] = matched.group(1)

    # numberOfSitesLabel#
    matched = re.search('duration \[days\]#(Number[^#]+)#', myTextWoEolDouble)

    mydictParams['Number of sites label'] = matched.group(1)

    # useOfBiomarkerLabel#
    matched = re.search('sites#(Use of biomarker)#', myTextWoEolDouble)
    mydictParams['Use of biomarker label'] = matched.group(1)

    # useOfGeneticBiomarkerLabel#
    matched = re.search('biomarker#(Use of genetic biomarker)#', myTextWoEolDouble)
    mydictParams['Use of genetic biomarker label'] = matched.group(1)

    # minAgeOfInclusionLabel#
    matched = re.search('biomarker#(Min age [^#]+)#', myTextWoEolDouble)
    mydictParams['Min age inclusion label'] = matched.group(1)

    # maxAgeOfInclusionLabel#
    matched = re.search('#(Max age [^#]+)#', myTextWoEolDouble)
    mydictParams['Max age inclusion label'] = matched.group(1)

    # numberOfArmsLabel#
    matched = re.search('#(Number of arms)#Therapeutic', myTextWoEolDouble)
    mydictParams['Number of arms label'] = matched.group(1)

    # therapeuticAreaLabel#
    matched = re.search('arms#(Therapeutic[^#]+)#', myTextWoEolDouble)
    mydictParams['Therapeutic area label'] = matched.group(1)

    # trialIsNationalLabel#
    matched = re.search('#(Trial is national)#', myTextWoEolDouble)
    mydictParams['Trial is national label'] = matched.group(1)

    # enrollmentOriginalValue#
    matched = re.search('#Trial is national##([^#]*)#', myTextWoEolDouble)
    mydictParams['Enrollment original value'] = matched.group(1)

    # trialDurationOriginalValue#
    matched = re.search('#Trial is national##[^#]*#([^#]+)#', myTextWoEolDouble)
    mydictParams['Duration original value'] = matched.group(1)

    # numberOfSitesOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#([^#]*)#', myTextWoEolDouble)
    mydictParams['Number of sites original value'] = matched.group(1)
    matched.group(1)

    # useOfBiomarkerOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#([^#]*)#', myTextWoEolDouble)
    mydictParams['Use of biomarker original value'] = matched.group(1)

    # useOfGeneticBiomarkerOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#([^#]*)', myTextWoEolDouble)
    mydictParams['Use of genetic biomarker original value'] = matched.group(1)

    # minAgeOfInclusionOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*([^#]*)', myTextWoEolDouble)
    mydictParams['Min age inclusion original value'] = matched.group(1)

    # maxAgeOfInclusionOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*[^#]*#([^#]*)', myTextWoEolDouble)
    mydictParams['Max age inclusion original value'] = matched.group(1)

    # numberOfArmsOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*[^#]*#[^#]*#([^#]*)#',
                        myTextWoEolDouble)
    mydictParams['Number of arms original value'] = matched.group(1)

    # therapeuticAreaOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*[^#]*#[^#]*#[^#]*#([^#]*)#',
                        myTextWoEolDouble)
    mydictParams['Therapeutic area original value'] = matched.group(1)

    # trialIsNationalOriginalValue#
    matched = re.search('#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*[^#]*#[^#]*#[^#]*#[^#]*#([^#]*)#',
                        myTextWoEolDouble)
    mydictParams['Trial is national original value'] = matched.group(1)

    myRegexBase = '#Trial is national##[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#*[^#]*#[^#]*#[^#]*#[^#]*#[^#]*#+'

    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)

    mydictParams['Enrollment new value'] = matchedStr

    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Duration new value'] = matchedStr

    # numberOfSitesNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Number of sites new value'] = matchedStr

    # useOfBiomarkerNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Use of biomarker new value'] = matchedStr

    # useOfGeneticBiomarkerNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Use of genetic biomarker new value'] = matchedStr

    # minAgeOfInclusionNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Min age inclusion new value'] = matchedStr

    # maxAgeOfInclusionNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Max age inclusion new value'] = matchedStr

    # numberOfArmsNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Number of arms new value'] = matchedStr

    # therapeuticAreaNewlValue#
    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Therapeutic area new value'] = matchedStr

    (myRegexBase, matchedStr) = matchRegexSkipArrow(myRegexBase, myTextWoEolDouble)
    mydictParams['Trial is national new value'] = matchedStr

    return mydictParams
