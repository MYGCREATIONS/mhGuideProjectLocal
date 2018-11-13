# -*- encoding: utf-8 -*-
from lettuce import before, world, after
import os
import os.path as path
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import configparser
import traceback
from selenium import webdriver
import json


@before.all
def setupBrowser():
    loadConfig()
    #loadTestData()
    chromeOptions = webdriver.ChromeOptions()
    if os.name == 'nt':
        preferences = {"download.default_directory": os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                  'pdfFiles\\')}
        chromeOptions.add_experimental_option("prefs", preferences)
        chromeOptions.headless = False
        chromeOptions.add_argument("window-size=1920,1080")
        world.browser = webdriver.Chrome(chrome_options=chromeOptions)
        world.browser.maximize_window()
    elif os.name == 'posix':
        chromeOptions.add_argument('window-size=1920x1080')
        chromeOptions.headless = True
        chromeOptions.add_argument('start-maximized')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        # chromeOptions.add_argument("download.default_directory=~/Downloads/")
        chromeOptions.add_experimental_option(
            'prefs', {
                'download.default_directory': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdfFiles/'),
                # 'download.default_directory': '~/Downloads/',
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
        )
        world.browser = webdriver.Chrome(chrome_options=chromeOptions)
    else:
        raise Exception("Operation system is not supported")
    world.browser.set_page_load_timeout(20)
    waiting()
    world.stepsfailed = []


@after.all
def say_goodbye(total):
    print "Congratulations, {0} of {1} scenarios passed!".format(total.scenarios_passed, total.scenarios_ran)
    print "Name of failed steps: " + ", ".join(repr(e) for e in world.stepsfailed)
    print "Goodbye!"
    #world.browser.quit()


@after.each_step
def takeScreenshot(step):  # take screenshot on failure
    if step.failed:
        step_str = step.sentence + ".png"

        world.browser.save_screenshot(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screenshots/%s'
                                                   % step_str))
        print("Step failed, saving screenshot of {0}".format(step.sentence))
        if step.sentence not in world.stepsfailed:
            world.stepsfailed.append(step.sentence)


def waiting():
    world.driver.implicitly_wait(world.config['DEFAULT']['WAIT_TIME_CLICKABLE'])


def explicitWaitClickable(element):
    driver = world.browser
    waiting_time = int(world.config['DEFAULT']['WAIT_TIME_CLICKABLE'])
    try:
        world.tinySleep()
        x = WebDriverWait(driver, waiting_time).until(EC.element_to_be_clickable(element))
    except WebDriverException:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        raise Exception('An error occurred on line {} in statement {}'.format(line, text))
    return x


def explicitWaitVisibility(element):
    driver = world.browser
    waiting_time = int(world.config['DEFAULT']['WAIT_TIME_VISIBILITY'])
    try:
        x = WebDriverWait(driver, waiting_time).until(EC.visibility_of_element_located(element))
    except WebDriverException:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        raise Exception('An error occurred on line {} in statement {}'.format(line, text))
    return x




def explicitWaitPresence(element):
    driver = world.browser
    waiting_time = int(world.config['DEFAULT']['WAIT_TIME_PRESENCE'])
    try:
        x = WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located(element))
    except WebDriverException:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        raise Exception('An error occurred on line {} in statement {}'.format(line, text))
    return x


def verifyElementNotThere(element):
    driver = world.browser
    waiting_time = int(world.config['DEFAULT']['WAIT_TIME_NOT_VISIBLE'])
    try:
        x = WebDriverWait(driver, waiting_time).until(EC.visibility_of_element_located(element))
        raise Exception('Element is there unlike expected')
    except WebDriverException:
        pass


def getAllElements(element):
    driver = world.browser
    return driver.find_elements(*element)


def explicitWaitPresenceAll(element):
    driver = world.browser
    waiting_time = int(world.config['DEFAULT']['WAIT_TIME_PRESENCE_ALL'])
    try:
        x = WebDriverWait(driver, waiting_time).until(EC.presence_of_all_elements_located(element))
    except WebDriverException:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        raise Exception('An error occurred on line {} in statement {}'.format(line, text))
    return x


def loadConfig():  # loading .ini config file
    world.config = configparser.ConfigParser()
    world.config.read(path.abspath(path.join(__file__, "../../Framework/common/config.ini")))


def loadTestData():  # loading .json test data file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata\\testdata.json'), 'r') as f:
        world.data = json.load(f)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata\\variantdata.json'), 'r') as f:
        world.variantdata = json.load(f)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata\\cvidata.json'), 'r') as f:
        world.cvidata = json.load(f)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata\\settingsdata.json'), 'r') as f:
        world.settingsdata = json.load(f)


@world.absorb
def waiting():  # waiting webdriver
    driver = world.browser
    driver.implicitly_wait(world.config['DEFAULT']['WAIT_TIME'])


@world.absorb
def waitingShortening():
    driver = world.browser
    driver.implicitly_wait(world.config['DEFAULT']['WAIT_TIME_SHORTENING'])


@world.absorb
def waitingLess():
    driver = world.browser
    driver.implicitly_wait(3)


@world.absorb
def refresh():
    driver = world.browser# refresh webdriver
    driver.refresh()


@world.absorb
def tinySleep():
    time.sleep(1)


@world.absorb
def bigSleep():
    time.sleep(2)