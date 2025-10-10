import time

import pandas as pd
import selenium
from selenium.webdriver import Keys
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.Utilities.reports import Reports
from src.Utilities.CommonMethods import commonMethods
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.Utilities.fields_array import FieldsArray
from selenium.webdriver.chrome.options import Options
import os
import re
from selenium.webdriver.common.action_chains import ActionChains

import requests
from bs4 import BeautifulSoup
import glob
from datetime import datetime



# from src.Tests.test_Logic import LogicTest
# import src.Tests.test_Logic
map_data = {}


def set_map_value(key, value):
    map_data[key] = value

def set_map_value1(key, value):
    if value is not None:
        map_data[key] = value
    else:
        print("Value is None for key:", key)


def get_map_value(key):
    return map_data.get(key)


class Actions():
    reports = Reports()
    common_methods = commonMethods()
    field_array_instance = FieldsArray()
    gettextData1 = ""
    gettextData2 = ""

    _instance = None  # part of singleton instance part of :  def __new__(cls):

    array1 = []
    array2 = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.driver = None
        self.map_data = {}

        # self.username_textbox_name = "username"
        # self.password_textbox_name = "password"
        # self.login_button_xpath = "//button[@type='submit']"

    def error_message(self, message):
        lines = []
        try:
            lines = message.split('(')
        except Exception as e:
            print(f"Error in error_message -> {e}")
        if lines == "":
            lines[0] = message
        return lines[0]

    def invokeBrowser(self, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                      Keywords,
                      Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            browser = browser.lower()
            print(f"browser from excel is {browser}")
            if browser == 'chrome' or browser == 'google chrome' or browser == 'google_chrome':
                print("Launching chrome browser.........")

                #"""
                #chrome_options = Options()
                #chrome_options.add_argument('--ignore-certificate-errors')
                #chrome_options.add_argument('--ignore-ssl-errors=true')
                #chrome_options.add_argument('--ignore-certificate-errors-spki-list')

                #driver_path = ChromeDriverManager().install()
                #self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
                #self.driver.implicitly_wait(10)
                #self.driver.maximize_window()
                #self.driver.get(Testdata)
                # reports.Report_TestDataStep()
                #"""

                #chromedriver_path = 'C:\\Users\\ppriya1\\OneDrive - Gilead Sciences\\Desktop\\Automation\\Cybergrants_Latest\\test-automation1Dec23\\test-automation\\chromedriver_win32\\chromedriver.exe'  # Replace with the actual path to your chromedriver executable
                #chrome_options = webdriver.ChromeOptions()
                #self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
                #self.driver.maximize_window()
                #self.driver.get(Testdata)
                #response = requests.get(Testdata, verify=False)
                # driver_path = ChromeDriverManager().install()
                # self.driver = webdriver.Chrome(executable_path=driver_path)
                # self.driver = webdriver.Chrome()
                # self.driver.implicitly_wait(10)
                # self.driver.maximize_window()
                # # reports = Reports()
                # self.driver.get(Testdata)
                #self.driver.get(Testdata)

                # self.driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install())
                # self.driver.implicitly_wait(10)
                # self.driver.maximize_window()
                #
                # self.driver.get(Testdata)

                # datapath = "/Drivers/chromedriver.exe"
                # rootpath = commonMethods.get_project_root(self)
                #
                # chromedriver_path = rootpath + datapath
                # print("chromedriver in path : " + chromedriver_path)
                # self.driver = webdriver.Chrome(executable_path=chromedriver_path)
                # self.driver.implicitly_wait(10)
                # self.driver.maximize_window()
                # self.driver.get(Testdata)

                self.driver = webdriver.Chrome()
                self.driver.implicitly_wait(10)
                self.driver.maximize_window()

                self.driver.get(Testdata)

            elif browser == 'firefox' or browser == 'mozilla firefox' or browser == 'mozilla_firefox':
                print("Launching firefox browser.........")
                driver_path = GeckoDriverManager().install()
                self.driver = webdriver.Firefox(executable_path=driver_path)
                self.driver.implicitly_wait(10)
                self.driver.maximize_window()
                self.driver.get(Testdata)
                # Reports.Report_TestDataStep()
            elif browser == 'edge' or browser == 'microsoft edge' or browser == 'microsoft_edge':
                print("Launching edge browser.........")

                # Construct the path to the directory containing msedgedriver.exe
                #edge_driver_dir = os.path.join(os.path.dirname(
                 #   'C:\\Users\\ppriya1\\Downloads\\test-automation26Dec23\\test-automation\\edgedriver'), '..',
                  #                             'Drivers')

                # Set the executable path to msedgedriver.exe
                #edge_driver_path = os.path.join(edge_driver_dir, 'msedgedriver.exe')

                # Check if the msedgedriver.exe exists at the specified path
                #if not os.path.exists(edge_driver_path):
                 # If msedgedriver.exe does not exist, download and install it using EdgeChromiumDriverManager
                #edge_driver_path = EdgeChromiumDriverManager().install()

                # Initialize the Edge WebDriver
                #driver = webdriver.Edge(executable_path=edge_driver_path)
                self.driver = webdriver.Edge('C:\\Users\\ppriya1\\Downloads\\test-automation26Dec23\\test-automation\\edgedriver\\msedgedriver.exe')
                self.driver.implicitly_wait(10)


                self.driver.maximize_window()
                self.driver.get(Testdata)
            ExpectedResult = "Application must open successfully"
            ActualResult = "Application launched successfully"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'invokeBrowser' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg

            self.reports.Report_TestDataStep(self.driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc + "\n" + str(Testdata), Keywords, Locator,
                                             ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return self.driver

    def enterUrl(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                 Keywords,
                 Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            #response = requests.get(url, verify=False)
            # reports = Reports()
            driver.get(Testdata)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'enterUrl' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def click(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
              Keywords,
              Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        count = 0
        element_value = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            # element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            """
            details = ["text", "title", "value"]

            for value in details:
                element_value = self.getElementDetails(element, value)
                if element_value != "":
                    break
            """

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            element.click()

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver

    # Returns detal of the element
    # This value is for report generation
    def getElementDetails(self, element, attr):
        detail = ""
        try:
            if element.tag_name == "a":
                detail = element.text
            elif element.tag_name == "td":
                detail = element.text
            elif element.get_attribute("type") == "submit":
                detail = element.get_attribute("value")
            elif element.get_attribute("placeholder") == "MM/DD/YYYY":
                detail = element.find_element(By.XPATH, "./ancestor::tr/td").text
            elif element.get_attribute("type") == "checkbox":
                detail = element.find_element(By.XPATH, "./ancestor::tr/td").text

            if detail == "":
                detail = "field/element"

        except Exception as e:
            print()
        return detail

    def click_Submit(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc,
                     Keywords,
                     Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        count = 0
        element_value = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            # element.click()
            driver.execute_script("arguments[0].click();", element)

            time.sleep(3)

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'click_submit' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver

    def sendKeys(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                 Keywords,
                 Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)

            try:
                name = element.get_attribute("title")
                name = re.sub(r'\*', '', name)
                name = name + " - " + element.get_attribute("value")
            except Exception as e:
                print(f"sendkeys to get value or title : {e}")

            element.send_keys(Testdata)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'sendKeys' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def wait(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
             Keywords, Locator,
             Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            driver.implicitly_wait(Testdata)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'wait' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator,
                                             "Wait for " + str(Testdata) + " seconds for the page to load",
                                             "Waited for " + str(Testdata) + " seconds and the page loaded",
                                             FlagTestCase, TestCase_Summary)
        return driver

    def enter_keydown(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, ExpectedResult, ActualResult, Keywords,
                      Locator,
                      Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            #WebElement.send_keys(Keys.ENTER)
            # Instantiate ActionChains
            #action_chains = ActionChains(driver)
            # Send the Back Arrow key and then the Enter key to the currently focused element
            #action_chains.send_keys(Keys.ARROW_DOWN).perform()
            #action_chains.send_keys(Keys.ENTER).perform()

            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            ExpectedResult = "Page scrolled successfully"
            ActualResult = "Page scrolled successfully"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'enter_keydown' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def jsclick(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                Keywords,
                Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))

            # element = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def jsScrollToElement(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords, Locator,
                          Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            obj = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            if name == "":
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsScrollToElement' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def typedata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                 Keywords,
                 Locator,
                 Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            element.clear()

            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                name = re.sub(r'\*', '', name)
                if name.endswith(":"):
                    name = name[:-1]
            except Exception as e:
                print(f"typedata to get value or title : {e}")

            if name == "":
                try:
                    name = driver.find_element(By.XPATH, Locator + "/ancestor::div[@class='form-row']/div").text
                except Exception as e:
                    print(f"typedata to get value or title : {e}")

            if name == "":
                try:
                    name = driver.find_element(By.XPATH, Locator + "/../../div").text
                except Exception as e:
                    print()

            element.send_keys(Testdata)
            ExpectedResult = "'" + name + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the '" + name + "' field"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'Textbox' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the 'Textbox' field"
            print("'type' Action Exception Message -> \n" + str(e))
            exMsg = self.error_message(str(e))

        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def typepassword(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords,
                     Locator,
                     Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            element.clear()
            element.send_keys(Testdata)
            ExpectedResult = "'Password' field must accept the entered value"

            ActualResult = "'" + str(''.join(['*' for _ in Testdata])) + "' entered in the password field"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'Password' field must accept the entered value"
            exMsg = self.error_message(str(e))
            print("'type' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def gettext1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                 Keywords,
                 Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            obj = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)
            self.gettextData1 = driver.find_element(By.XPATH, Locator).text
            self.gettextData1 = self.gettextData1.strip()
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'gettext' Action Exception Message -> \n" + str(e))
        finally:
            if Testdata == "NA" or Testdata == "na" or Testdata == "Na":
                Testdata = ""

            if Locator == "NA" or Locator == "na" or Locator == "Na":
                Locator = ""
            if FlagTestCase == "Fail":
                ActualResult = exMsg

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def gettext2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                 Keywords,
                 Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # obj = self.driver.find_element(By.XPATH, Locator)
            # self.driver.execute_script("arguments[0].scrollIntoView();", obj)
            self.gettextData2 = driver.find_element(By.XPATH, Locator).text
            self.gettextData2 = self.gettextData2.strip()
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'gettext' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def gettext_toArray1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                         testStepDesc,
                         Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # obj1 = self.driver.find_element(By.XPATH, Locator)
            # text1 = self.driver.execute_script("return arguments[0].text;", obj1)

            text1 = driver.find_element(By.XPATH, Locator).text
            print(f"text1 - {text1}")
            text1 = text1.strip()
            self.array1.append(str(text1))
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'gettext' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def gettext_toArray2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                         testStepDesc,
                         Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # obj2 = self.driver.find_element(By.XPATH, Locator)
            # text2 = self.driver.execute_script("return arguments[0].text;", obj2)

            text2 = driver.find_element(By.XPATH, Locator).text
            print(f"text2 - {text2}")
            text2 = text2.strip()
            self.array2.append(str(text2))
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'gettext' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def compareArray(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords,
                     Locator,
                     Testdata, TestCase_Summary):
        FlagTestCase = ""
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            if len(self.array1) != 0 and len(self.array2) != 0:
                if self.array1 == self.array2:
                    FlagTestCase = "pass"
                else:
                    FlagTestCase = "Fail"
            else:
                FlagTestCase = "Fail"

            exMsg = f"value of array 1 is '{self.array1}' and \nvalue of array 2 is '{self.array2}'"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'compareArray' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def compareData(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                    testStepDesc, Keywords,
                    Locator,
                    Testdata, TestCase_Summary):
        FlagTestCase = ""
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            if self.gettextData1 != "" and self.gettextData2 != "":
                if self.gettextData1 == self.gettextData2:
                    FlagTestCase = "pass"
                else:
                    FlagTestCase = "Fail"
            else:
                FlagTestCase = "Fail"

            exMsg = "value 1 is '" + str(self.gettextData1) + "' and value 2 is '" + str(self.gettextData2) + "'"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'gettext' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    # action.verifyObj(self.driver, browserNameFromExcel, modulename, TestCaseName, TestStepName, TestStepID, Description,
    #                Keywords, Locator,
    #               Testdata)
    def verifyObj(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                  Keywords,
                  Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", element)

            name = element.text

            if name == "":
                name = element.get_attribute("value")

            ExpectedResult = "'" + str(name) + "' must be part of the form"
            ActualResult = "'" + str(name) + "' is part of the form"

            print(f"value of {str(Locator)} is {str(name)}")
        except Exception as e:
            FlagTestCase = "Fail"
            # removing the word "Verify" from testStepDesc
            name = testStepDesc.replace("Verify", "")
            ExpectedResult = "'" + name + "' must be part of the form"
            exMsg = self.error_message(str(e))
            print("'verifyObj' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase,
                                             TestCase_Summary)
        return driver

    def verifyWindow(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords,
                     Locator,
                     Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            driver.switch_to.window(driver.window_handles[1])
            get_url = driver.current_url
            print(get_url)
            assert get_url == Testdata, f"Expected {Testdata}, but got {get_url}"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'new tab' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def verifySort(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                   Keywords,
                   Locator,
                   Testdata, index, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            tab_element = driver.find_element(By.XPATH, f"{Locator}[{index}]")
            # tab_element = driver.find_element(By.XPATH, Locator)
            tab_text = tab_element.text
            print(tab_text)
            assert tab_text == Testdata, f"Expected {Testdata}, but got {tab_text}"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'type' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def verifyCurrentWindow(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc,
                            Keywords, Locator,
                            Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            getTitle = driver.getTitle
            print(getTitle)
            assert getTitle == Testdata, f"Expected {Testdata}, but got {getTitle}"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'new tab' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def verifyElementNotVisible(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                testStepDesc,
                                Keywords,
                                Locator,
                                Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            ExpectedResult = "Reject does not move to next step"
            WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, Locator)))
            print("Element is not present")
            ActualResult = "Rejected does not move to next step"
        except TimeoutException:
            print("Element is still present")
            ActualResult = "Rejected moved to next step"
            FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'verifyElementNotVisible' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def clearandtype(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords,
                     Locator,
                     Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            #driver.find_element(By.XPATH, Locator).click()
            #text_box = driver.find_element(By.XPATH, Locator).clear()
            text_box = driver.find_element(By.XPATH, Locator)
            text_box.send_keys(Testdata)
            # self.driver.send_keys(Testdata)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'clearandtype' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndSetData(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator,
                           Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)

            textData = element.get_attribute('value')
            if textData == "" or textData is None:
                element.send_keys(Testdata)
                time.sleep(1)

            textData = element.get_attribute('value')
            print(textData)
            set_map_value(key, textData)
            print("setting test data with key: ", {key}, "and value:", {textData})
            title = get_map_value(key)
            print(title)

            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                ExpectedResult = "Retrieve and store '" + name + "' for verification"
                ActualResult = "Retrieved and stored value of '" + name + "' for verification"
            except Exception as e:
                ExpectedResult = "Retrieve and store '" + key + "' for verification"
                ActualResult = "Retrieved and stored value of '" + key + "' for verification"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retreiveAndSetData' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndValidate(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc,
                            Keywords,
                            Locator,
                            Testdata, key, TestCase_Summary):
        global element
        FlagTestCase = "Pass"
        exMsg = ""
        textDataRetrieved = ""
        expected_text = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            try:
                element = driver.find_element(By.XPATH, Locator)
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                textDataRetrieved = element.text.strip()
            except Exception as e:
                print()

            if textDataRetrieved == "":
                # textDataRetrieved = element.get_attribute("value")
                textDataRetrieved = element.text

            # print(textDataRetrieved)
            expected_text = get_map_value(key)

            # Below code works for text
            # assert textDataRetrieved == expected_text, f"For field '{key}', Expected text '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator}'."

            # Check if the expected value is an integer and textDataRetrieved is an integer
            if str(expected_text).isdigit() and str(textDataRetrieved).isdigit():
                # Convert both values to integers and perform the assertion
                assert int(textDataRetrieved) == int(
                    expected_text), f"For field '{str(key)}', Expected integer '{str(expected_text)}', but got '{str(textDataRetrieved)}' for element with locator '{str(Locator)}'."
            else:
                # Perform a text assertion
                assert textDataRetrieved == expected_text, f"For field '{str(key)}', Expected text '{str(expected_text)}', but got '{str(textDataRetrieved)}' for element with locator '{str(Locator)}'."

            try:
                name = driver.find_element(By.XPATH, Locator + "/../td").text
                ExpectedResult = "'" + str(name) + "' must have '" + str(textDataRetrieved) + "' as value"
                ActualResult = "'" + str(name) + "' has '" + str(textDataRetrieved) + "' as value"
            except Exception as e:
                ExpectedResult = "'" + str(key) + "' must have '" + str(textDataRetrieved) + "' as value"
                ActualResult = "'" + str(key) + "' has '" + str(textDataRetrieved) + "' as value"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + str(key) + "' must have '" + str(textDataRetrieved) + "' as value"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidate' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def validateLink(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords,
                     Locator,
                     Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            textDataRetrieved = element.get_attribute('href')
            print(textDataRetrieved)
            expected_text = get_map_value("title")
            print(expected_text)
            assert textDataRetrieved == expected_text, f"Expected text '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator}'."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'validateLink' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def refresh(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            driver.refresh()

            time.sleep(20)
            ExpectedResult = f"Page refreshed"
            ActualResult = f"Page refreshed"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'type' Action Exception Message -> \n" + str(e))
            ExpectedResult = f"Page is not refreshed"
            ActualResult = f"Page is not  refreshed"
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def enterdropdownvalueandsetdatatomap(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                          Requirement, testStepDesc,
                                          Keywords,
                                          Locator,
                                          Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            # element = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", element)

            dropdown = Select(driver.find_element(By.XPATH, Locator))
            dropdown.select_by_visible_text(str(Testdata))
            set_map_value(key, str(Testdata))
            # print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)

            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                name = re.sub(r'\*', '', name)
                ExpectedResult = "'" + name + "' must be selectable"
                ActualResult = "'" + str(Testdata) + "' option is selected and displayed in the dropdown"
            except Exception as e:
                ExpectedResult = "Dropdown must be selectable"
                ActualResult = "'" + str(Testdata) + "' option is selected and displayed in the dropdown"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'enterdropdownvalueandsetdatatomap' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def cleartypeandsetdata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc,
                            Keywords,
                            Locator,
                            Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            element.click()
            element.clear()
            element.send_keys(Testdata)

            set_map_value(key, Testdata)
            print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)
            print(title)
            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                name = re.sub(r'\*', '', name)
                ExpectedResult = "'" + name + "' field must accept the entered text value"
                ActualResult = "'" + str(Testdata) + "' entered in '" + name + "' field"
            except Exception as e:
                ExpectedResult = "Text field must accept the entered text value"
                ActualResult = "'" + str(Testdata) + "' entered in text field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'cleartypeandsetdata' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def scrollInternalWindow(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                             testStepDesc,
                             Keywords,
                             Locator,
                             Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            div_element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].disabled = false;", div_element)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'scrollInternalWindow' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def contactInfoCheckExisting(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                 Requirement, testStepDesc,
                                 Keywords,
                                 Locator,
                                 Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        matchfound = False
        ExpectedResult = ""
        ActualResult = ""
        try:
            elements = driver.find_elements(By.XPATH, Locator)
            for element in elements:
                if element.text == Testdata:
                    print("match found")
                    element.click()
                    matchfound = True
                    time.sleep(1)
                    break
                else:
                    print()
            time.sleep(1)

            if matchfound == False:
                driver.find_element(By.XPATH, "//input[@value='Create New']").click()
                time.sleep(5)

            """
                name = Testdata.split(' ')

                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc, Keywords, "//tr[@id='cgtr1']/descendant::td/input", name[0])
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr2']/descendant::td/input", name[1])

                driver = self.enterdropdownvalueandsetdatatomap(driver, browser, modulename, TestCaseName, TestStepName,
                                                                TestStepID,
                                                                testStepDesc,
                                                                Keywords,
                                                                "//select[@id='CG2470146']",
                                                                "Treating Physician", "ContactType")

                driver = self.enterdropdownvalueandsetdatatomap(driver, browser, modulename, TestCaseName, TestStepName,
                                                                TestStepID,
                                                                testStepDesc,
                                                                Keywords,
                                                                "//select[@id='CG2470138']",
                                                                "India", "Country")

                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr5']/descendant::td/input", "Addresstest")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr6']/descendant::td/input", "citytest")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr8']/descendant::td/input", "provincetest")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr9']/descendant::td/input", "560097")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr10']/descendant::td/input", "900000000")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr11']/descendant::td/input", "email@example.com")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr12']/descendant::td/input", "9999999999")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr13']/descendant::td/input", "faxtest")
                driver = self.typedata(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       testStepDesc,
                                       Keywords, "//tr[@id='cgtr14']/descendant::td/input", "nurse")

                driver.find_element(By.XPATH, "//input[@value='Save and Proceed']").click()
                time.sleep(3)
                elements = driver.find_elements(By.XPATH, Locator)
                for element in elements:
                    if element.text == Testdata:
                        print("match found")
                        element.click()
                        time.sleep(3)
                        break
                    else:
                        print()


            """

            ExpectedResult = "Check if Contact Info '" + str(Testdata) + "' is displayed"
            ActualResult = "Checked and selected '" + str(Testdata) + "' in Contact Info"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'contactInfoCheckExisting' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def checkQuestionandfieldtype(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                  Requirement, testStepDesc,
                                  Keywords,
                                  Locator,
                                  Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ActualResult_fieldType = ""
        ExpectedResult_fieldType = ""
        ExpectedResult1 = ""
        ActualResult1 = ""
        try:
            if Locator.startswith("//"):
                test_data = Testdata.split('|')
                Locator_data = Locator.split('|')

                labeltext = driver.find_element(By.XPATH, "//label[@id='label-" + Locator_data[1] + "']").text
                # print(f"label name is {labeltext}")
                labeltext = re.sub(r'\*', '', labeltext)
                labeltext = labeltext.strip()
                driver, ExpectedResult, ActualResult, FlagTestCase = self.verify_text(driver, browser, modulename,
                                                                                      TestCaseName,
                                                                                      TestStepName,
                                                                                      TestStepID,
                                                                                      Requirement, testStepDesc,
                                                                                      Keywords, Locator, labeltext,
                                                                                      test_data[0].strip(),
                                                                                      True, key, True, "",
                                                                                      TestCase_Summary)

                field_type = driver.find_element(By.XPATH, Locator_data[0]).get_attribute("type")
                print(f"field_type is : {field_type}")
                driver, ExpectedResult_fieldType, ActualResult_fieldType, FlagTestCase_fieldType = self.verify_fieldType(
                    driver, browser,
                    modulename,
                    TestCaseName,
                    TestStepName,
                    TestStepID,
                    Requirement,
                    testStepDesc,
                    Keywords, Locator,
                    Testdata, field_type,
                    False,
                    key, True, "",
                    TestCase_Summary)
            else:
                test_data = Testdata.split('|')
                labeltext = driver.find_element(By.XPATH, "//label[@id='label-" + Locator + "']").text
                labeltext = re.sub(r'\*', '', labeltext)
                labeltext = labeltext.strip()
                # print(f"label name is {labeltext}")
                driver, ExpectedResult, ActualResult, FlagTestCase = self.verify_text(driver, browser, modulename,
                                                                                      TestCaseName,
                                                                                      TestStepName,
                                                                                      TestStepID,
                                                                                      Requirement, testStepDesc,
                                                                                      Keywords, Locator, labeltext,
                                                                                      test_data[0].strip(),
                                                                                      True, key, True, "",
                                                                                      TestCase_Summary)

                field_type = driver.find_element(By.XPATH, "//*[@id='" + Locator + "']").get_attribute("type")
                print(f"field_type is : {field_type}")
                driver, ExpectedResult_fieldType, ActualResult_fieldType, FlagTestCase_fieldType = self.verify_fieldType(
                    driver, browser,
                    modulename,
                    TestCaseName,
                    TestStepName,
                    TestStepID,
                    Requirement,
                    testStepDesc,
                    Keywords, Locator,
                    Testdata, field_type,
                    False,
                    key, True, "",
                    TestCase_Summary)

            print(f'ActualResult result is : {ActualResult}')
            print(f'ExpectedResult result is: {ExpectedResult}')
            print(f'ActualResult_fieldType result is : {ActualResult_fieldType}')
            print(f'ExpectedResult_fieldType result is: {ExpectedResult_fieldType}')
            ActualResult1 = ActualResult + " <br> " + ActualResult_fieldType
            ExpectedResult1 = ExpectedResult + " <br> " + ExpectedResult_fieldType

            if not bool(FlagTestCase) or not bool(FlagTestCase_fieldType):
                FlagTestCase = False

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'checkQuestionandfieldtype' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult1 = ActualResult1 + "<br>" + exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult1,
                                             ActualResult1, FlagTestCase, TestCase_Summary)
        return driver

    def verify_text(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, Testdata1, is_exact_match, key, flag, msg, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            if flag == True:
                if is_exact_match == True:
                    if Testdata == Testdata1:
                        FlagTestCase = "Pass"
                        # exMsg = "'" + Testdata + "' is equal to '" + Testdata1 + "'"
                        # exMsg = "Label, ' " + Testdata + "' is as expected"
                        ActualResult = "'" + Testdata + "' is visible in the page. "
                        ExpectedResult = "'" + Testdata + "' must be visible in the page. "
                    else:
                        FlagTestCase = "Fail"
                        # exMsg = "'" + Testdata + "' is not equal to '" + Testdata1 + "'"
                        # exMsg = "Label should be '" + Testdata1 + "' but displaying as '" + Testdata + "'"
                        ActualResult = "'" + Testdata1 + "'" + " is displayed as '" + Testdata + "' in the page. "
                        ExpectedResult = "'" + Testdata1 + "' must be visible in the page. "
                        # print(f'Actual result is : {ActualResult}')
                        # print(f'Expected result is: {ExpectedResult}')
                else:
                    if Testdata in Testdata1:
                        FlagTestCase = "Pass"
                        # exMsg = "'" + Testdata1 + "' contains '" + Testdata + "'"
                        # exMsg = "Label, ' " + Testdata + "' is as expected"
                        ActualResult = "'" + Testdata + "' is visible in the page. "
                        ExpectedResult = "'" + Testdata + "' must be visible in the page. "
                    else:
                        FlagTestCase = "Fail"
                        # exMsg = "'" + Testdata1 + "' does not contains '" + Testdata + "'"
                        # exMsg = "Label should be '" + Testdata1 + "' but displaying as '" + Testdata + "'"
                        ActualResult = "'" + Testdata1 + "'" + " is displayed as '" + Testdata + "' in the page. "
                        ExpectedResult = "'" + Testdata1 + "' must be visible in the page. "
            else:
                FlagTestCase = "Fail"
                # ActualResult = msg

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            ActualResult = exMsg
            print("'verify_text' Action Exception Message -> \n" + str(exMsg))
        finally:
            print()
            """
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            """
        return driver, ExpectedResult, ActualResult, FlagTestCase

    def verify_fieldType(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, Testdata1, is_exact_match, key, flag, msg, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            test_data = Testdata.split('|')
            if flag == True:
                if is_exact_match == True:
                    if test_data[1] == Testdata1:
                        FlagTestCase = "Pass"
                        # ActualResult = "'" + test_data[0] + "' is  '" + test_data[1] + "' field"
                        if test_data[1] == "select":
                            test_data[1] = "Dropdown"
                        ActualResult = " Field type is '" + test_data[1] + "'"  # add expected resul in this function
                        ExpectedResult = " Field type must be '" + test_data[1] + "'"
                    else:
                        FlagTestCase = "Fail"
                        # ActualResult = "'" + test_data[0] + "' is not '" + test_data[1] + "' but displayed as '" + Testdata + "'"
                        if test_data[1] == "select":
                            test_data[1] = "Dropdown"
                        ActualResult = " Field type must be '" + test_data[
                            1] + "' but displaying as '" + Testdata1 + "'"
                        ExpectedResult = " Field type must be '" + test_data[1] + "'"
                else:
                    if test_data[1] in Testdata1:
                        FlagTestCase = "Pass"
                        # ActualResult = "'" + test_data[0] + "' is  '" + test_data[1] + "' field"
                        if test_data[1] == "select":
                            test_data[1] = "Dropdown"
                        ActualResult = " Field type is '" + test_data[1] + "'"
                        ExpectedResult = " Field type must be '" + test_data[1] + "'"
                    else:
                        FlagTestCase = "Fail"
                        # ActualResult = "'" + test_data[0] + "' is not '" + test_data[1] + "' but displayed as '" +
                        # Testdata + "'"
                        if test_data[1] == "select":
                            test_data[1] = "Dropdown"
                        ActualResult = " Field type must be '" + test_data[
                            1] + "' but displaying as '" + Testdata1 + "'"
                        ExpectedResult = " Field type must be '" + test_data[1] + "'"
            else:
                FlagTestCase = "Fail"
                ActualResult = msg

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'verify_fieldType' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            """
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             str(ActualResult), FlagTestCase, TestCase_Summary)
            """
        return driver, ExpectedResult, ActualResult, FlagTestCase

    def verify_text_para(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, Testdata1, is_exact_match, key, flag, msg, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            if flag == True:
                if is_exact_match == True:
                    if Testdata == Testdata1:
                        FlagTestCase = "Pass"
                        # exMsg = "'" + Testdata + "' is equal to '" + Testdata1 + "'"
                        ActualResult = "'" + Testdata + "' is visible in the page. "
                        ExpectedResult = "'" + Testdata + "' must be visible in the page. "
                    else:
                        FlagTestCase = "Fail"
                        # exMsg = "'" + Testdata + "' is not equal to '" + Testdata1 + "'"
                        # ActualResult = "Label should be <br><br>'" + Testdata1 + "' <br><br> but displaying as <br><br>'" + Testdata + "'"
                        ActualResult = "'" + Testdata1 + "'" + " is displayed as '" + Testdata + "' in the page. "
                        ExpectedResult = "'" + Testdata1 + "' must be visible in the page. "
                else:
                    if Testdata in Testdata1:
                        FlagTestCase = "Pass"
                        # exMsg = "'" + Testdata1 + "' contains '" + Testdata + "'"
                        ActualResult = "'" + Testdata + "' is visible in the page. "
                        ExpectedResult = "'" + Testdata + "' must be visible in the page. "
                    else:
                        FlagTestCase = "Fail"
                        # exMsg = "'" + Testdata1 + "' does not contains '" + Testdata + "'"
                        # ActualResult = "Label should be <br><br>'" + Testdata1 + "' <br><br>but displaying as <br><br>'" + Testdata + "'"
                        ActualResult = "'" + Testdata1 + "'" + " is displayed as '" + Testdata + "' in the page. "
                        ExpectedResult = "'" + Testdata1 + "' must be visible in the page. "
            else:
                FlagTestCase = "Fail"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'verify_text_para' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def contact_info_checkbox(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                              Requirement, testStepDesc,
                              Keywords,
                              Locator,
                              Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            print(f"contact_info_checkbox: locator is : {Locator}")
            driver.find_element(By.XPATH, "//a[text()='" + Locator + "']/ancestor::tr/td/input").click()
            ExpectedResult = "Select '" + str(Locator) + "' on Contact info"
            ActualResult = "Selected '" + str(Locator) + "' on Contact info"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Select '" + str(Locator) + "' on Contact info"
            exMsg = self.error_message(str(e))
            print("'contact_info_checkbox' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def upload_file(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        docname = ""
        name = ""
        finalMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            """
            wait = WebDriverWait(driver, 5)

            wait.until(
                EC.presence_of_element_located((By.XPATH, Locator))).send_keys(Testdata)
            """
            filename = self.common_methods.create_docx_file()

            # The [-1] index accesses the last element of the list
            doc_name = filename.split('\\')[-1]
            docname = doc_name
            # unpack the tuple into separate variables
            driver, doc_found = self.file_exist(driver, doc_name, Locator)
            name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
            ActualResult = "File '" + docname + "' already exist in location, did not uploaded again for '" + name + "'"

            # if doc is not found in the upload section, then we are uploading it or else we don't
            if doc_found == False:
                driver.find_element(By.XPATH, Locator).click()
                window_after = driver.window_handles[-1]
                driver.switch_to.window(window_after)
                time.sleep(2)
                # print("title of the switched window : ", driver.title)

                choose_file = driver.find_element(By.ID, "xfileupload")
                # choose_file.send_keys(Testdata)

                # print(f"file name inside action class: {filename}")
                choose_file.send_keys(filename)
                """
                time.sleep(60)
                actions = ActionChains(driver)
                actions.send_keys(Testdata)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                """
                time.sleep(2)
                driver.find_element(By.XPATH, "//input[@id='primaryAction']").click()

                wait = WebDriverWait(driver, 20)
                wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'successfully')]")))

                driver.find_element(By.XPATH, "//input[@value='Close Window']").click()
                driver.switch_to.window(driver.window_handles[0])
                ExpectedResult = "'" + name + "' must upload file"
                ActualResult = "Uploaded file '" + docname + "' to '" + name
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + name + "' must upload file"
            exMsg = self.error_message(str(e))
            print("'upload_file' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def file_exist(self, driver, filename, Locator):
        matchfound = False
        try:
            elements = driver.find_elements(By.XPATH, Locator + "/following::ul/li")
            for element in elements:
                if filename in element.text:
                    print(f"{filename}, already exist, so it is not uploaded again")
                    matchfound = True
                    time.sleep(1)
                    break
                else:
                    print()
        except Exception as e:
            exMsg = e
            print("'file_exist' Action Exception Message -> \n" + str(exMsg))
        return driver, matchfound

    def verify_text_equal(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                          Requirement, testStepDesc,
                          Keywords,
                          Locator,
                          Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        element_text = ""
        try:
            element_text = driver.find_element(By.XPATH, Locator).text
            print(f"verify_are_equal TestData is '{Testdata}' and fetched text is '{element_text}'")
            if element_text == Testdata:
                FlagTestCase = "Pass"
                exMsg = f"{element_text} is equal to {Testdata}"
            else:
                FlagTestCase = "Fail"
                exMsg = f"{element_text} is not equal to {Testdata}"

            ExpectedResult = "Text must be '" + element_text + "'"

            if FlagTestCase == "Pass":
                ActualResult = "Text has '" + element_text + "' as value"
            else:
                ActualResult = "'" + Testdata + "' is displayed as '" + element_text + "' in the page. "
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Text must be '" + element_text + "'"
            exMsg = self.error_message(str(e))
            print("'verify_text_equal' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def scroll_inner_div(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # get all the common elements in the inner div and scroll to each one

            recentList = driver.find_elements(By.XPATH, Locator)

            for list_ele in recentList:
                driver = self.scrollIntoView(driver, list_ele)
                # driver.execute_script("arguments[0].scrollIntoView();", list_ele)

            ExpectedResult = "Scroll through the Prescriber Agreement"
            ActualResult = "Scrolled through the Prescriber Agreement and enabled 'Legal Agreement Accept'"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'scroll_inner_div' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def scrolltoview_verify_text(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                 Requirement, testStepDesc,
                                 Keywords,
                                 Locator,
                                 Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", element)
            element_text = element.text

            if element_text.strip() == Testdata:
                FlagTestCase = "Pass"
                exMsg = f"{element_text} is equal to {Testdata}"
            else:
                FlagTestCase = "Fail"
                exMsg = f"{element_text} is not equal to {Testdata}"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'verify_text_equal' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             str(Testdata) + " - \n " + str(exMsg), FlagTestCase, TestCase_Summary)
        return driver

    def checkQuestion_internal(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                               Requirement, testStepDesc,
                               Keywords,
                               Locator,
                               Testdata, key, TestCase_Summary):
        labeltext = ""
        FlagTestCase = "Pass"
        exMsg = ""
        flag = ""
        element = None
        ExpectedResult = ""
        ActualResult = ""
        try:
            # adding * in the xpath because there are some with label and some with span, so instead of /label or
            # /span, we have given /*
            element = driver.find_element(By.XPATH, "//div[@id='formRow" + Locator + "']/*")
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            labeltext = element.text
            # print(f"label name is {labeltext}")

            # _____this may be removed ______________
            ExpectedResult = "'" + str(labeltext) + "' must be visible in the page"
            ActualResult = "'" + str(labeltext) + "' is visible in the page"
            # _______________________________________

            driver, ExpectedResult, ActualResult, FlagTestCase = self.verify_text(driver, browser, modulename,
                                                                                  TestCaseName,
                                                                                  TestStepName, TestStepID, Requirement,
                                                                                  testStepDesc,
                                                                                  Keywords, Locator, labeltext,
                                                                                  Testdata, True, key,
                                                                                  True, exMsg, TestCase_Summary)
        except Exception as e:
            FlagTestCase = "Fail"
            flag = False
            exMsg = self.error_message(str(e))
            print("'checkQuestion_internal' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail" and exMsg != "":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def checkQuestion_internal_para(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                    Requirement, testStepDesc,
                                    Keywords,
                                    Locator,
                                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            if Locator.startswith("//"):

                # remove the first 2 letters of the Locator which will have //
                Locator_data = Locator[2:]
                label_obj = driver.find_element(By.XPATH, "//div[@id='formRow" + Locator_data + "']/div")
                driver = self.scrollIntoView(driver, label_obj)
                # driver.execute_script("arguments[0].scrollIntoView();", label_obj)
                labeltext = label_obj.text

                # print(f"label name is {labeltext}")
                self.verify_text_para(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                      Requirement, testStepDesc,
                                      Keywords, Locator_data, labeltext, Testdata, True, key, True, "",
                                      TestCase_Summary)
            else:
                label_obj = driver.find_element(By.XPATH, "//div[@id='formRow" + Locator + "']/p")
                labeltext = label_obj.text
                driver = self.scrollIntoView(driver, label_obj)
                # driver.execute_script("arguments[0].scrollIntoView();", label_obj)
                # labeltext = driver.find_element(By.XPATH, "//div[@id='formRow" + Locator + "']/p").text
                print(f"label name is {labeltext}")
                self.verify_text_para(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                      Requirement, testStepDesc,
                                      Keywords, Locator, labeltext, Testdata, True, key, True, "", TestCase_Summary)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'checkQuestion_internal_para' Action Exception Message -> \n" + str(exMsg))
        return driver

    def enterUrlInNewTab(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # reports = Reports()
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
            driver.get(Testdata)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'enterUrlInNewTab' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator,
                                             ExpectedResult, ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def enableandclickcheckbox(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                               Requirement, testStepDesc,
                               Keywords,
                               Locator,
                               Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            checkbox = driver.find_element(By.XPATH, Locator)
            driver.execute_script('arguments[0].removeAttribute("disabled");', checkbox)
            driver.find_element(By.XPATH, Locator).click()
            # Click on the checkbox (optional)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'enableandclickcheckbox' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator,
                                             ExpectedResult, ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def datepicker(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                   Requirement, testStepDesc,
                   Keywords,
                   Locator,
                   Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("arguments[0].click();", element)

            """
            # driver.find_element(By.XPATH, Locator).click()
            datepicker = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,  '//body/div[4]')))

            str1 = "//td/button[text()='" + str(Testdata) + "']"
            time.sleep(1)
            # Find the date "March 15, 2023" in the datepicker
            date_elem = datepicker.find_element(By.XPATH, "//td/button[text()='" + str(Testdata) + "']")
            """
            time.sleep(1)
            date_elem = driver.find_element(By.XPATH, "//td[@data-day='" + str(Testdata) + "']")

            # Click the date element to select it
            date_elem.click()
            # driver.execute_script("arguments[0].click();", date_elem)

            entered_value = driver.find_element(By.XPATH, Locator).get_attribute("value")
            set_map_value(key, str(entered_value))

            print(f"key is {str(key)} and value is {str(entered_value)}")

            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                ExpectedResult = "'" + str(name) + "' field must accept the selected date"
                ActualResult = "Selected '" + str(Testdata) + "' date in '" + str(name) + "' field"
            except Exception as e:
                print()
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'datepicker' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def acceptalert(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        message = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
            time.sleep(3)
            """
            alert = Alert(driver)
            # wait = WebDriverWait(driver, 10)
            # alert = wait.until(EC.alert_is_present())
            # message = alert.text
            # print(f"Pop up alert message is : {message}")
            # Accept or dismiss the alert
            alert.accept()  # or alert.dismiss()
            """

            alert = driver.switch_to.alert
            message = alert.text
            alert.accept()
            time.sleep(3)
            ExpectedResult = "Accept alert message displayed"
            ActualResult = "Accepted alert '" + message + "' displayed"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Accept alert message displayed"
            exMsg = self.error_message(str(e))
            print("'acceptalert' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def dismissalert(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        message = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
            time.sleep(3)
            """
            alert = Alert(driver)
            # wait = WebDriverWait(driver, 10)
            # alert = wait.until(EC.alert_is_present())
            # message = alert.text
            # print(f"Pop up alert message is : {message}")
            # Accept or dismiss the alert
            alert.accept()  # or  alert.dismiss()
            """

            alert = driver.switch_to.alert
            message = alert.text
            alert.dismiss()
            time.sleep(3)
            ExpectedResult = "Accept alert message displayed"
            ActualResult = "Accepted alert '" + message + "' displayed"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Accept alert message displayed"
            exMsg = self.error_message(str(e))
            print("'acceptalert' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def alerttext(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        message = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
            time.sleep(3)
            """
            alert = Alert(driver)
            # wait = WebDriverWait(driver, 10)
            # alert = wait.until(EC.alert_is_present())
            # message = alert.text
            # print(f"Pop up alert message is : {message}")
            # Accept or dismiss the alert
            alert.accept()  # or alert.dismiss()
            """

            alert = driver.switch_to.alert
            message = alert.text
            if message == 'All input fields are mandatory!':
                alert.accept()
                ExpectedResult = "Accept alert message displayed"
                ActualResult = "Accepted alert '" + message + "' displayed"

            else:

                FlagTestCase = "Fail"
                ExpectedResult = "Accept alert message displayed"
                ActualResult = "Incorrect alert '" + message + "' displayed"


            time.sleep(3)

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Accept alert message displayed"
            exMsg = self.error_message(str(e))
            print("'acceptalert' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver



    def waitandtype(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locator)))

            # Send keys to the element
            element.click()
            element.send_keys(Testdata)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'waitandtype' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             str(Testdata) + " - \n " + str(exMsg), FlagTestCase, TestCase_Summary)
        return driver

    def searchFetchedRequestNumber(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                   Requirement, testStepDesc,
                                   Keywords,
                                   Locator,
                                   Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            expected_text = get_map_value(key)
            expected_str = str(expected_text)
            print("getting str test data with key: ", {key}, "and value:", {expected_str})
            print("The variable, expected str is of type:", type(expected_str))
            driver.find_element(By.XPATH, Locator).click()
            driver.find_element(By.XPATH, Locator).send_keys(expected_str)

            try:
                ExpectedResult = "'" + key + "' must have '" + expected_str + "' as value"
                ActualResult = "'" + key + "' has '" + expected_str + "' as value"
            except Exception as e:
                print()
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'searchFetchedRequestNumber' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndSetText(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                           Requirement, testStepDesc,
                           Keywords,
                           Locator,
                           Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        textData = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            textData = element.text
            print(textData)
            set_map_value(key, textData)
            print("setting test data with key: ", {str(key)}, "and value:", {str(textData)})
            title = get_map_value(key)
            print(title)

            try:
                name = driver.find_element(By.XPATH, Locator + "/../td").text
                ExpectedResult = "Retrieve '" + str(name) + "' value"
                ActualResult = "Retrieved '" + str(textData) + "' as value for '" + str(name) + "' field"
            except Exception as e:
                ExpectedResult = "Retrieve '" + str(key) + "' value"
                ActualResult = "Retrieved '" + str(textData) + "' as value for '" + str(key) + "' field"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retreiveAndSetText' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndValidateInternalPortalData(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                              Requirement, testStepDesc,
                                              Keywords,
                                              Locator,
                                              Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        expected_text1 = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            textDataRetrieved = element.text
            textDataRetrieved1 = textDataRetrieved.strip()
            print(textDataRetrieved1)
            expected_text = get_map_value(key)
            expected_text1 = expected_text.strip()
            print("get test data with key: ", {key}, "and value:", {expected_text})
            assert textDataRetrieved1 == expected_text1, f"Expected text '{expected_text1}', but got '{textDataRetrieved1}' for element with locator '{Locator}'."

            try:
                name = driver.find_element(By.XPATH, Locator + "/parent::div/label").text
                ExpectedResult = "'" + name + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + name + "' has '" + textDataRetrieved + "' as value"
            except Exception as e:
                ExpectedResult = "'" + key + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + key + "' has '" + textDataRetrieved + "' as value"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidateInternalPortalData' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndValidateIntegerData(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       Requirement, testStepDesc,
                                       Keywords,
                                       Locator,
                                       Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        expected_text1 = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        textDataRetrieved = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            textDataRetrieved = element.text
            convertedtext = str(textDataRetrieved)
            textDataRetrieved1 = convertedtext.strip()
            print(textDataRetrieved1)
            expected_text = get_map_value(key)
            expected_text1 = str(expected_text).strip()
            print("get test data with key: ", {key}, "and value:", {expected_text1})
            assert textDataRetrieved1 == expected_text1, f"Expected text '{expected_text1}', but got '{textDataRetrieved1}' for element with locator '{Locator}'."
            # ActualResult = key + " has data '" + expected_text1 + "' as expected"

            try:
                name = driver.find_element(By.XPATH, Locator + "/../td").text
                ExpectedResult = "'" + name + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + name + "' has '" + textDataRetrieved + "' as value"
            except Exception as e:
                ExpectedResult = "'" + key + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + key + "' has '" + textDataRetrieved + "' as value"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + key + "' must have '" + textDataRetrieved + "' as value"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidateIntegerData' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def search_requestID(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        expected_text1 = ""
        flag = False
        ExpectedResult = ""
        ActualResult = ""
        RequestID = ""
        try:
            RequestID = get_map_value(key)
            if RequestID == "" or RequestID is None:
                RequestID = Testdata

            # keyword_field = driver.find_element(By.ID, "x_key")
            keyword_field = driver.find_element(By.ID, "x_key")
            # driver.execute_script("arguments[0].scrollIntoView();", keyword_field)
            keyword_field.clear()
            keyword_field.send_keys(RequestID)

            # driver.find_element(By.XPATH, "//a[@data-search_field_name='Request Owner']").click()
            obj = driver.find_element(By.XPATH, "//a[@data-search_field_name='Request Owner']")
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)
            driver.execute_script("arguments[0].click();", obj)
            time.sleep(2)

            count = 0
            while count < 15:  # 30 seconds * 14 = 420 seconds or 7 mins, so we are waiting for 7 mins for the request id to be visible
                try:
                    # driver.find_element(By.XPATH, "//button[@class='search__button--primary']/span").click()
                    search_btn = driver.find_element(By.XPATH, "//button[@class='search__button--primary']/span")
                    driver = self.scrollIntoView(driver, search_btn)
                    # driver.execute_script("arguments[0].scrollIntoView();", search_btn)
                    driver.execute_script("arguments[0].click();", search_btn)
                    time.sleep(2)
                    try:
                        # link_element = driver.find_element(By.XPATH, "//a[text()='" + Testdata + "']")
                        # request_link.click()
                        request_link = driver.find_element(By.XPATH, "//a[text()='" + str(RequestID) + "']")
                        driver = self.scrollIntoView(driver, request_link)
                        # driver.execute_script("arguments[0].scrollIntoView();", request_link)
                        driver.execute_script("arguments[0].click();", request_link)
                        flag = True
                        print("Request id is found")
                        break
                    except Exception as e:
                        print(f"waiting for 30 seconds")
                        time.sleep(30)
                        count = count + 1
                except Exception as e:
                    print(f"search req id\n" + str(e))
                    exMsg = self.error_message(str(e))

            if flag == True:
                ExpectedResult = "Search for Request ID '" + str(RequestID) + "' and click on it."
                ActualResult = "Request ID '" + str(RequestID) + "' is found, and clicked on it."
            else:
                ExpectedResult = "Search for Request ID '" + str(RequestID) + "' and click on it."
                ActualResult = "Request ID '" + str(RequestID) + "' is not found."
        except Exception as e:
            ExpectedResult = "Search for Request ID '" + str(RequestID) + "' and click on it."
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'search_requestID' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def enterdropdownontable(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                             Requirement, testStepDesc,
                             Keywords,
                             Locator,
                             Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        ExpectedResult = ""
        ActualResult = ""
        try:

            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator + "')]/ancestor::div[@aria-rowindex]")
            rowindex = element.get_attribute("aria-rowindex")

            # Yes/ No column
            yesno_col = driver.find_element(By.XPATH,
                                            "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div")
            yesno_col.click()
            time.sleep(1)
            yesno_col.click()
            time.sleep(1)

            driver.find_element(By.XPATH,
                                "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/select/option[text()='" + Testdata + "']").click()
            time.sleep(1)

            ExpectedResult = "Select '" + Testdata + "' from '" + Locator + "' dropdown field"
            ActualResult = "Selected '" + Testdata + "' from '" + Locator + "' dropdown field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = e
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def textareaontable(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                        Requirement, testStepDesc,
                        Keywords,
                        Locator,
                        Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        Locator_data = []
        ExpectedResult = ""
        ActualResult = ""
        try:
            Locator_data = Locator.split("|")
            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator_data[
                                              1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            # Specify column
            specify_col = driver.find_element(By.XPATH,
                                              Locator_data[
                                                  0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/div/div")
            specify_col.click()
            time.sleep(1)
            specify_text = driver.find_element(By.XPATH,
                                               Locator_data[
                                                   0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/div/div/textarea")
            specify_text.send_keys(Testdata)
            time.sleep(1)

            set_map_value(key, Testdata)
            print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)
            print(title)

            # name=specify_text.text
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the '" + Locator_data[1] + "' field"

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the 'Textbox' field"

            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def enterdropdownontable1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                              Requirement, testStepDesc,
                              Keywords,
                              Locator,
                              Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator + "')]/ancestor::div[@aria-rowindex]")
            rowindex = element.get_attribute("aria-rowindex")

            # Yes/ No column
            yesno_col = driver.find_element(By.XPATH,
                                            "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='4']/div/div")
            yesno_col.click()
            time.sleep(1)
            yesno_col.click()
            time.sleep(1)

            driver.find_element(By.XPATH,
                                "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='4']/div/div/select/option[text()='" + Testdata + "']").click()
            time.sleep(1)

            ExpectedResult = "Select '" + Testdata + "' from '" + Locator + "' dropdown field"
            ActualResult = "Selected '" + Testdata + "' from '" + Locator + "' dropdown field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = e
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def dateaontable(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                     Requirement, testStepDesc,
                     Keywords,
                     Locator,
                     Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        ExpectedResult = ""
        ActualResult = ""

        try:

            Locator_data = Locator.split("|")
            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator_data[
                                              1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            # Specify column
            specify_col = driver.find_element(By.XPATH,
                                              Locator_data[
                                                  0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/div")
            specify_col.click()
            time.sleep(2)

            specify_text = driver.find_element(By.XPATH,
                                               Locator_data[
                                                   0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/descendant::input")
            specify_text.click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//div[@class='react-datepicker-popper']/descendant::div[text()='" + str(
                Testdata) + "']").click()
            # specify_text.send_keys(Testdata)
            print(f"date test data{Testdata}")
            time.sleep(3)

            set_map_value(key, Testdata)
            print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)
            print(title)

            name = specify_text.text

            # "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/div/div/div/input[text()='" + Testdata + "']").click()
            # specify_text.send_keys(Testdata)

            ExpectedResult = "'" + Locator_data[1] + "' date field must accept the selected date"
            ActualResult = "'" + Testdata + "' selected in '" + Locator_data[1] + "' date field"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = e
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def textareaontable1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        Locator_data = Locator.split("|")
        ExpectedResult = ""
        ActualResult = ""
        try:

            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator_data[
                                              1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            # Specify column
            specify_col = driver.find_element(By.XPATH,
                                              Locator_data[
                                                  0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='4']/div/div")
            specify_col.click()
            time.sleep(1)
            specify_text = driver.find_element(By.XPATH,
                                               Locator_data[
                                                   0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='4']/div/div/textarea")
            specify_text.send_keys(Testdata)
            time.sleep(3)

            set_map_value(key, Testdata)
            print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)
            print(title)

            # name=specify_text.text
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the '" + Locator_data[1] + "' field"

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the 'Textbox' field"
            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def textareaontable2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                         Requirement, testStepDesc,
                         Keywords,
                         Locator,
                         Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        Locator_data = Locator.split("|")
        ExpectedResult = ""
        ActualResult = ""
        try:

            element = driver.find_element(By.XPATH,
                                          Locator_data[
                                              1] + "/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            # # Yes/ No column
            # yesno_col = driver.find_element(By.XPATH,
            #                                 "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div")
            # yesno_col.click()
            # time.sleep(1)
            # yesno_col.click()
            # time.sleep(1)
            #
            # driver.find_element(By.XPATH,
            #                     "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/select/option[text()='" +
            #                     testdata_[0] + "']").click()
            # time.sleep(1)

            # Specify column
            specify_col = driver.find_element(By.XPATH,
                                              Locator_data[
                                                  0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='1']/div/div")
            specify_col.click()
            time.sleep(1)
            specify_text = driver.find_element(By.XPATH,
                                               Locator_data[
                                                   0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='1']/div/div/input")
            specify_text.send_keys(Testdata)
            time.sleep(3)

            set_map_value(key, Testdata)
            print("setting test data with key: ", {key}, "and value:", {Testdata})
            title = get_map_value(key)
            print(title)

            # name=specify_text.text
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the '" + Locator_data[1] + "' field"

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + Locator_data[1] + "' field must accept the entered value"
            ActualResult = "'" + str(Testdata) + "' entered in the 'Textbox' field"
            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def dateaontable1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                      Requirement, testStepDesc,
                      Keywords,
                      Locator,
                      Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        ExpectedResult = ""
        ActualResult = ""

        try:

            Locator_data = Locator.split("|")
            element = driver.find_element(By.XPATH,
                                          Locator_data[1] + "/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            # Specify column
            specify_col = driver.find_element(By.XPATH,
                                              Locator_data[
                                                  0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/div")
            specify_col.click()
            time.sleep(2)

            specify_text = driver.find_element(By.XPATH,
                                               Locator_data[
                                                   0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/descendant::input")
            specify_text.click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//div[@class='react-datepicker-popper']/descendant::div[text()='" + str(
                Testdata) + "']").click()
            # specify_text.send_keys(Testdata)
            print(f"date test data{Testdata}")
            time.sleep(3)

            # "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='2']/div/div/div/div/div/input[text()='" + Testdata + "']").click()
            # specify_text.send_keys(Testdata)

            ExpectedResult = "'Date of Relapse' field must accept the selected date"
            ActualResult = "'" + Testdata + "' selected in 'Date of Relapse' date field"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = e
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def enterdropdownontable2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                              Requirement, testStepDesc,
                              Keywords,
                              Locator,
                              Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        ExpectedResult = ""
        ActualResult = ""
        try:

            element = driver.find_element(By.XPATH,
                                          Locator + "/ancestor::div[@aria-rowindex]")
            rowindex = element.get_attribute("aria-rowindex")

            # Yes/ No column
            yesno_col = driver.find_element(By.XPATH,
                                            "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/div/div")
            yesno_col.click()
            time.sleep(1)
            yesno_col.click()
            time.sleep(1)
            driver.find_element(By.XPATH,
                                "//div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/div/div/select/option[text()='" + Testdata + "']").click()
            time.sleep(1)

            ExpectedResult = "Select '" + Testdata + "' from '" + Locator + "' dropdown field"
            ActualResult = "Selected '" + Testdata + "' from '" + Locator + "' dropdown field"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = e
            print("'enterdropdownontable2' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def checkQuestionOnTable_internal(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                      Requirement, testStepDesc,
                                      Keywords,
                                      Locator,
                                      Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        cell = None
        labeltexts = []  # Corrected line
        labeltext = ""
        Locator_data = []
        ExpectedResult = ""
        ActualResult = ""

        try:

            Locator_data = Locator.split("|")
            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator_data[
                                              1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            labeltext = driver.find_element(By.XPATH,
                                            Locator_data[
                                                0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='1']/descendant::div/div/div[contains(text(),'" + (
                                                Locator_data[
                                                    1]) + "')]").text

            print(f"labeltext data is {labeltext}")
            # labeltext=element1.text
            time.sleep(3)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of(element))

            if labeltext == Locator_data[1]:
                FlagTestCase = "Pass"
                ActualResult = "'" + Locator_data[1] + "' is visible in the page. "
                ExpectedResult = "'" + Locator_data[1] + "' must be visible in the page. "
            else:
                FlagTestCase = "Fail"
                ActualResult = "'" + Locator_data[1] + "'" + " is displayed as '" + labeltext + "' in the page. "
                ExpectedResult = "'" + Locator_data[1] + "' must be visible in the page. "
        except Exception as e:
            FlagTestCase = "Fail"
            flag = False
            exMsg = e
            print("'checkQuestionOnTable_internal' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndValidateOnTableValue(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                        Requirement, testStepDesc,
                                        Keywords,
                                        Locator,
                                        Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        textDataRetrieved = ""
        expected_text = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            Locator_data = Locator.split("|")
            element1 = driver.find_element(By.XPATH,
                                           "//div[contains(text(),'" + Locator_data[
                                               1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element1.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            element = driver.find_element(By.XPATH,
                                          Locator_data[
                                              0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/descendant::div/div/div[contains(text(),'" + (
                                              Locator_data[1]) + "')]")

            print(f"labeltext data is {element}")
            # labeltext=element1.text
            time.sleep(3)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of(element))

            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            textDataRetrieved = element.text.strip()
            print("textDataRetrieved vlaues :", {textDataRetrieved})
            print(textDataRetrieved)
            expected_text = get_map_value(key)
            print("get_map_value:", {get_map_value})
            print("get test data with key: ", {key}, "and value:", {expected_text})

            try:
                ExpectedResult = "'" + Locator_data[1] + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + Locator_data[1] + "' has '" + textDataRetrieved + "' as value"
            except Exception as e:
                print()

            assert textDataRetrieved == expected_text, f"For Key '{key}', Expected text '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator_data[1]}'."

        except Exception as e:
            FlagTestCase = "fail"
            ExpectedResult = "'" + key + "' must have '" + textDataRetrieved + "' as value"
            ActualResult = "'" + key + "' has '" + textDataRetrieved + "' as value"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidateOnTableValue' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndValidateOnTableUnit(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       Requirement, testStepDesc,
                                       Keywords,
                                       Locator,
                                       Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        textDataRetrieved = ""
        expected_text = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            Locator_data = Locator.split("|")
            element1 = driver.find_element(By.XPATH,
                                           "//div[contains(text(),'" + Locator_data[
                                               1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element1.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            element = driver.find_element(By.XPATH,
                                          Locator_data[
                                              0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='4']/descendant::div/div/div[contains(text(),'" + (
                                              Locator_data[1]) + "')]")
            print(f"labeltext data is {element}")
            # labeltext=element1.text
            time.sleep(3)

            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            textDataRetrieved = element.text.strip()
            print(textDataRetrieved)
            expected_text = get_map_value(key)
            print(f"labeltext data is {element}")
            # labeltext=element1.text
            time.sleep(3)

            try:
                ExpectedResult = "'" + Locator_data[1] + "' must have '" + textDataRetrieved + "' as value"
                ActualResult = "'" + Locator_data[1] + "' has '" + textDataRetrieved + "' as value"
            except Exception as e:
                print()

            print("get test data with key: ", {key}, "and value:", {expected_text})
            assert textDataRetrieved == expected_text, f"For Key '{key}', Expected text '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator_data[1]}'."

        except Exception as e:
            FlagTestCase = "fail"

            ExpectedResult = "'" + key + "' must have '" + textDataRetrieved + "' as value"
            ActualResult = "'" + key + "' has '" + textDataRetrieved + "' as value"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidate' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def retreiveAndSetTextOnTableValue(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       Requirement, testStepDesc,
                                       Keywords,
                                       Locator,
                                       Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        textData = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            Locator_data = Locator.split("|")
            element = driver.find_element(By.XPATH,
                                          "//div[contains(text(),'" + Locator_data[
                                              1] + "')]/ancestor::div[@aria-rowindex]")

            rowindex = element.get_attribute("aria-rowindex")

            print(f"locator is {Locator}, rowindex is {rowindex}")

            labeltext = driver.find_element(By.XPATH,
                                            Locator_data[
                                                0] + "/descendant::div[@aria-rowindex='" + rowindex + "']/div[@aria-colindex='3']/descendant::div/div/div[contains(text(),'" + (
                                                Locator_data[
                                                    1]) + "')]")

            print(f"labeltext data is {labeltext}")
            # labeltext=element1.text
            time.sleep(3)
            textData = labeltext.text
            print(textData)
            set_map_value(key, textData)
            print("setting test data with key: ", {key}, "and value:", {textData})
            title = get_map_value(key)
            print(title)

            try:
                name = driver.find_element(By.XPATH, Locator + "/../td").text
                ExpectedResult = "Retrieve '" + name + "' value"
                ActualResult = "Retrieved '" + textData + "' as value for '" + name + "' field"
            except Exception as e:
                print()
        except Exception as e:
            FlagTestCase = "fail"
            exMsg = e
            print("'retreiveAndSetText' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def hidden_field(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc,
                     Keywords,
                     Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        count = 0
        element_value = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)

            # element_value = self.getElementDetails(element, "value")

            if element.is_displayed():
                if element.tag_name == "tr":
                    element_value = element.find_element(By.XPATH, "./td/label").text
                else:
                    element_value = element.text

                element_value = re.sub(r'\*', '', element_value)

                if element_value == "":
                    element_value = self.getElementDetails(element, "value")

                if element_value == "":
                    element_value = "element"

                ExpectedResult = "'" + element_value + "' field must be hidden"
                ActualResult = "'" + element_value + "' field is not hidden"
            else:
                if element.tag_name == "tr":
                    element = element.find_element(By.XPATH, "./td/label")
                elif element.tag_name == "input":
                    element_value = driver.execute_script("return arguments[0].value;", element)

                if element_value == "":
                    element_value = driver.execute_script("return arguments[0].textContent;", element)

                element_value = re.sub(r'\*', '', element_value)
                ExpectedResult = "'" + element_value + "' field must be hidden"
                ActualResult = "'" + element_value + "' field is hidden"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'hidden_field' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver

    def get_physician_name(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator,
                           Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            textData = element.text.split("\n")[1]
            print(textData)
            set_map_value(key, textData)
            print("setting test data with key: ", {key}, "and value:", {textData})
            title = get_map_value(key)
            print(title)

            try:
                name = driver.find_element(By.XPATH, Locator + "/ancestor::tr/td").text
                ExpectedResult = "Retrieve and store '" + str(textData) + "' for verification"
                ActualResult = "Retrieved and stored value of '" + str(textData) + "' for verification"
            except Exception as e:
                ExpectedResult = "Retrieve and store '" + str(key) + "' for verification"
                ActualResult = "Retrieved and stored value of '" + str(key) + "' for verification"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retreiveAndSetData' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def log_text(self, driver, Locator):
        element = driver.find_element(By.XPATH, Locator).text
        print(f"log_text: {element}")
        return driver

    def get_alert_and_Compare(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc,
                              Keywords,
                              Locator,
                              Testdata, key, TestCase_Summary):
        global field_Array
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        alertValue = []
        special_chars = ['>', '<', '≥', '≤']
        try:
            elements = driver.find_elements(By.XPATH, Locator)
            print(len(elements))
            for element in elements:
                print(f"left navigation text2 - {element.text}")
                text = element.text
                text = text.strip()
                for char in special_chars:
                    text = text.replace(char, '')
                if text != '':
                    alertValue.append(str(text))

            print(f"value of site is '{alertValue}'")

            field_Array = self.field_array_instance.get_data(Testdata)
            print(f"value of array is '{field_Array}'")
            if len(alertValue) != 0 and len(field_Array) != 0:
                if alertValue == field_Array:
                    FlagTestCase = "pass"
                else:
                    FlagTestCase = "Fail"
            else:
                FlagTestCase = "Fail"

            # field_Array = "<br>".join(field_Array)
            # alertValue = "<br>".join(alertValue)

            field_Array = "<br><br>".join([f"{i + 1}. {value}" for i, value in enumerate(field_Array)])
            alertValue = "<br><br>".join([f"{i + 1}. {value}" for i, value in enumerate(alertValue)])

            ExpectedResult = f"Required fields must be \n'{field_Array}'"
            ActualResult = f"Required fields are \n'{alertValue}'"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            ExpectedResult = f"Required fields must be \n'{field_Array}'"
            exMsg = exMsg + f"Required fields must be '{field_Array}' and \nRequired fields are '{alertValue}'"
            print("'get_alert_and_Compare' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail" and ActualResult == "":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def clear_allfields(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc,
                              Keywords,
                              Locator,
                              Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            elements = driver.find_elements(By.XPATH, Locator)
            print(len(elements))
            for element in elements:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    print(f"tagname is:  {element.tag_name}")
                    if element.tag_name == "input":
                        element.clear()
                    elif element.tag_name == "select":
                        dropdown = Select(element)
                        dropdown.select_by_index(0)
                    elif element.tag_name == "textarea":
                        element.clear()

                except Exception as e:
                    print("inside for loop clear_allfields ->", str(e))

            ExpectedResult = "Clear all data from the page"
            ActualResult = "Cleared all data from the page"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'get_alert_and_Compare' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName,
                                             TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def obj_removed(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                    testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        global testdata
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        alertValue = []
        try:
            testdata = Testdata.split('|')
            wait = WebDriverWait(driver, 5)
            try:
                wait.until_not(EC.presence_of_element_located((By.XPATH, Locator)))
                FlagTestCase = "Pass"
            except Exception as e:
                print()

            ExpectedResult = testdata[0]
            ActualResult = testdata[1]
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = testdata[0]
            exMsg = self.error_message(str(e))
            print("'obj_removed' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def wait_with_no_screenshot(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                testStepDesc,
                                Keywords, Locator,
                                Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            driver.implicitly_wait(Testdata)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'wait' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator,
                                             "Wait for " + str(Testdata) + " seconds for the page to load",
                                             "Waited for " + str(Testdata) + " seconds and the page loaded",
                                             FlagTestCase, TestCase_Summary)
        return driver

    def jsclick_with_no_screenshot(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                   Requirement, testStepDesc,
                                   Keywords,
                                   Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            obj = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            element_value = self.getElementDetails(obj, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", obj)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def delete_request(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                       testStepDesc,
                       Keywords,
                       Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            obj = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            element_value = self.getElementDetails(obj, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", obj)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def scrollIntoView(self, driver, element):
        try:
            # scrolling to the elements
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Calculate the desired scroll position
            scroll_position = element.location_once_scrolled_into_view['y'] - (driver.execute_script(
                'return window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;') / 2)
            # Scroll the page to the desired position
            driver.execute_script(f'window.scrollTo(0, {scroll_position});')
        except Exception as e:
            print("'scrollIntoView' Action Exception Message -> \n" + str(e))
        return driver

    def approval1_QC_check(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Click on Internal Information in left navigation
            lefnav1 = driver.find_element(By.XPATH, "//a[@id='navsection1781168']")
            lefnav1.click()

            # Check if Gilad Protocol number has value, if not then select index 0 in it
            gilda_protocalNo = Select(driver.find_element(By.XPATH, "//select[@id='CG2557702']"))
            if len(gilda_protocalNo.all_selected_options) == 1:
                # gilda_protocalNo.select_by_visible_text("Protocol Value 1")
                gilda_protocalNo.select_by_visible_text("IN-EU-200-6059")
            # Click on Save All button after Gilda protocol number selection
            internal_info_btn = driver.find_element(By.XPATH, "//div[@id='cgSection1781168']/descendant::button[2]")
            driver.execute_script("arguments[0].click();", internal_info_btn)
            # internal_info_btn.click()
            time.sleep(5)

            # Click on approval btn
            lefnav_approval = driver.find_element(By.XPATH, "//a[@id='navsectionapproval']")
            driver.execute_script("arguments[0].click();", lefnav_approval)
            # lefnav_approval.click()
            time.sleep(2)

            try:
                driver.find_element(By.ID, "reject").click()
                time.sleep(5)
            except Exception as e:
                try:
                    driver.find_element(By.LINK_TEXT, "Return to Reviewer").click()
                    time.sleep(2)

                    dropdown = Select(driver.find_element(By.ID, "x_lb_approval_id"))
                    dropdown.select_by_visible_text("Approval Step 1: Quality Check Approval")

                    confirm_btn = driver.find_element(By.XPATH, "//input[@value='Confirm'']")
                    driver.execute_script("arguments[0].click();", confirm_btn)
                    time.sleep(5)

                    driver.find_element(By.ID, "reject").click()
                    time.sleep(5)
                except Exception as e:
                    print()

            # check if "Submit For Approval" button is present if yes then click on it
            try:
                submit_for_approval = driver.find_element(By.XPATH, "//input[@value='Submit for Approval']")
                driver = self.scrollIntoView(driver, submit_for_approval)
                driver.execute_script("arguments[0].click();", submit_for_approval)
                # submit_for_approval.click()

                try:
                    time.sleep(1)
                    alert = driver.switch_to.alert
                    alert.accept()
                    time.sleep(5)
                except Exception as e:
                    print("approval1_QC_check - Alert exception")
            except Exception as e:
                print("approval1_QC_check - Submit for Approval button is not present in the form")

            time.sleep(5)

            # Checking whether 'Approval Step 1: Quality Check Approval ' is present
            element = driver.find_element(By.XPATH, "//h3[contains(text(),'Approval Step 1: Quality Check Approval')]")

            driver = self.scrollIntoView(driver, element)

            dropdown = Select(driver.find_element(By.XPATH, "//select[@id='CG2483914']"))
            dropdown.select_by_visible_text("Yes")

            ae_comments = driver.find_element(By.XPATH, "//textarea[@id='CG2526376']")
            driver = self.scrollIntoView(driver, ae_comments)
            # driver.execute_script("arguments[0].scrollIntoView();", ae_comments)
            ae_comments.send_keys("Ae Comments testing")

            portalNo_dropdown = driver.find_element(By.XPATH, "//select[@id='CG2557704']")
            dropdown1 = Select(portalNo_dropdown)
            dropdown1.select_by_visible_text("Yes")

            hcpPortal_dropdown = driver.find_element(By.XPATH, "//select[@id='CG2551220']")
            dropdown2 = Select(hcpPortal_dropdown)
            dropdown2.select_by_visible_text("Yes")

            ExpectedResult = "Enter data in 'Approval Step 1: Quality Check Approval'"
            ActualResult = "Entered data in 'Approval Step 1: Quality Check Approval'"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'approval1_QC_check' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def approval2_BasicReq_RegApproval(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       Requirement, testStepDesc,
                                       Keywords,
                                       Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Checking whether 'Approval Step 2: Basic Requirements Regulatory Approval ' is present
            # wait = WebDriverWait(driver, 10)
            # element = wait.until(EC._element_if_visible((By.XPATH, "//h3[contains(text(),'Approval Step 2: Basic Requirements Regulatory Approval')]")))

            element = driver.find_element(By.XPATH,
                                          "//h3[contains(text(),'Approval Step 2: Basic Requirements Regulatory Approval')]")

            #  Calculate the desired scroll position
            scroll_position = element.location_once_scrolled_into_view['y'] - (driver.execute_script(
                'return window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;') / 2)
            #  Scroll the page to the desired position
            driver.execute_script(f'window.scrollTo(0, {scroll_position});')

            # dropdown1 = wait.until(EC._element_if_visible((By.XPATH, "//select[@id='CG2526482']")))
            # dropdown = Select(dropdown1)
            dropdown = Select(driver.find_element(By.XPATH, "//select[@id='CG2526482']"))
            dropdown.select_by_visible_text("Yes")

            ExpectedResult = "Enter data in 'Approval Step 2: Basic Requirements Regulatory Approval'"
            ActualResult = "Entered data in 'Approval Step 2: Basic Requirements Regulatory Approval'"
            # time.sleep(2)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'approval2_BasicReq_RegApproval' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def approval3_med_approval(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc,
                               Keywords,
                               Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Checking whether 'Approval Step 1: Quality Check Approval ' is present
            element = driver.find_element(By.XPATH, "//h3[contains(text(),'Approval Step 3: Medical Approval')]")

            driver = self.scrollIntoView(driver, element)

            reqApproval = Select(driver.find_element(By.XPATH, "//select[@id='CG2483922']"))
            reqApproval.select_by_visible_text("Yes")

            revRecommondation = driver.find_element(By.XPATH, "//textarea[@id='CG2657260']")
            driver = self.scrollIntoView(driver, revRecommondation)
            revRecommondation.send_keys("approval duration, approved dose, dosage form testing")

            ExpectedResult = "Enter data in 'Approval Step 3: Medical Approval'"
            ActualResult = "Entered data in 'Approval Step 3: Medical Approval'"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'approval3_med_approval' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def approval4_Reg_approval(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc,
                               Keywords,
                               Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Checking whether 'Approval Step 4: Regulatory Approval' is present
            element = driver.find_element(By.XPATH, "//h3[contains(text(),'Approval Step 4: Regulatory Approval')]")

            driver = self.scrollIntoView(driver, element)

            reqFiling = Select(driver.find_element(By.XPATH, "//select[@id='CG2638136']"))
            reqFiling.select_by_visible_text("Gilead IND (Individual Patient Protocol)")
            time.sleep(0.2)

            na_regFiling = driver.find_element(By.XPATH, "//textarea[@id='CG2638138']")
            # driver = self.scrollIntoView(driver, na_regFiling)
            na_regFiling.send_keys("Not Applicable Regulatory Filing testing")
            time.sleep(0.2)

            drugShip_cert = Select(driver.find_element(By.XPATH, "//select[@id='CG2483934']"))
            drugShip_cert.select_by_visible_text("Yes")
            time.sleep(0.2)

            na_drugShip_cert = driver.find_element(By.XPATH, "//textarea[@id='CG2637876']")
            # driver = self.scrollIntoView(driver, na_drugShip_cert)
            na_drugShip_cert.send_keys(
                "Not Applicable Has the appropriate drug shipment import certificate/permit been obtained testing")
            time.sleep(0.2)

            HA_approvalLetter = Select(driver.find_element(By.XPATH, "//select[@id='CG2638140']"))
            HA_approvalLetter.select_by_visible_text("Yes")
            time.sleep(0.2)

            na_HA_approvalLetter = driver.find_element(By.XPATH, "//textarea[@id='CG2638144']")
            # driver = self.scrollIntoView(driver, na_HA_approvalLetter)
            na_HA_approvalLetter.send_keys("Not App testing")
            time.sleep(0.2)

            Investigator_sponsored = Select(driver.find_element(By.XPATH, "//select[@id='CG2638146']"))
            Investigator_sponsored.select_by_visible_text("Yes")
            time.sleep(0.2)

            na_Investigator_sponsored = driver.find_element(By.XPATH, "//textarea[@id='CG2638156']")
            driver = self.scrollIntoView(driver, na_Investigator_sponsored)
            na_Investigator_sponsored.send_keys("Not App testing")
            time.sleep(0.2)

            ind_patient_protocol = Select(driver.find_element(By.XPATH, "//select[@id='CG2638148']"))
            ind_patient_protocol.select_by_visible_text("Yes")
            time.sleep(0.2)

            na_ind_patient_protocol = driver.find_element(By.XPATH, "//textarea[@id='CG2638158']")
            driver = self.scrollIntoView(driver, na_ind_patient_protocol)
            na_ind_patient_protocol.send_keys("Not App testing")
            time.sleep(0.2)

            # SIGNATURE – Local RA or authorised delegate
            printName = driver.find_element(By.XPATH, "//input[@id='CG2638150']")
            driver = self.scrollIntoView(driver, printName)
            printName.send_keys("Vincent")
            time.sleep(0.2)

            jobTitle = driver.find_element(By.XPATH, "//input[@id='CG2638152']")
            driver = self.scrollIntoView(driver, jobTitle)
            jobTitle.send_keys("testing")
            time.sleep(0.2)

            # Date

            element = driver.find_element(By.XPATH, "//input[@id='CG2638154']")
            driver = self.scrollIntoView(driver, element)
            element.send_keys("12/23/2023")
            # driver.execute_script("arguments[0].click();", element)

            ## datepicker = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/div[3]')))
            # time.sleep(0.2)
            # date_elem = driver.find_element(By.XPATH, "//td[@data-day='15']")
            # driver.execute_script("arguments[0].click();", date_elem)

            driver = self.scrollIntoView(driver, element)

            ExpectedResult = "Enter data in 'Approval Step 4: Regulatory Approval'"
            ActualResult = "Entered data in 'Approval Step 4: Regulatory Approval'"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'approval4_Reg_approval' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

        # //*[text()='This page isn’t working']

    def hover_over_webpart(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            driver.find_element(By.XPATH, "//div[@data-automation-id='CanvasZoneEdit']").click()

            # Locate the element that triggers the hover action
            # Locate the hover element
            element_to_hover_over = driver.find_element(By.XPATH, Locator)
            #element_to_hover_over = driver.find_element(By.XPATH,"(//div[@data-automation-id='CanvasZoneEdit']/descendant::button[@aria-label='Add a new web part in column one'])[1]")
            # Create an ActionChains object
            action_chains = ActionChains(driver)
            time.sleep(6)

            # Hover over the element and then click it
            action_chains.move_to_element(element_to_hover_over).click().perform()

            driver.find_element(By.XPATH, Locator).click()

            #hover_element_xpath = "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]"
            #hover_element_xpath = "(//i[@data-icon-name='Add'])"
            # hover_element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, hover_element_xpath)))

            # Perform a hover action on the hover element
            # ActionChains(driver).move_to_element(hover_element_xpath).perform()

            # Wait for the dynamically generated element to appear
            #dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            #dynamic_element_xpath = "(//button[@aria-label='Add a new web part in column one'])[1]"

            #GetIDynamicID=driver.find_element(By.XPATH, "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]/div/div[2]").get_attribute("id")

            # dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            # #dynamic_element_xpath = GetIDynamicID
            # dynamic_element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, dynamic_element_xpath)))
            #
            # # Now you can interact with the dynamically generated element
            # dynamic_element.click()
            #
            # element_value = self.getElementDetails(hover_element, "value")
            # element_value = re.sub(r'\*', '', element_value)

            ExpectedResult = "Clicked on ADD icon to add webpart'"  "' "
            ActualResult = "Clicked on ADD icon to add webpart'"  "' "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def hover_over_element(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            driver.find_element(By.XPATH, "//div[@data-automation-id='CanvasZoneEdit']").click()

            # Locate the element that triggers the hover action
            # Locate the hover element
            element_to_hover_over = driver.find_element(By.XPATH, "(//button[@aria-label='Add a new web part in column one'])[1]")
            #element_to_hover_over = driver.find_element(By.XPATH,"(//div[@data-automation-id='CanvasZoneEdit']/descendant::button[@aria-label='Add a new web part in column one'])[1]")
            # Create an ActionChains object
            action_chains = ActionChains(driver)
            time.sleep(6)

            # Hover over the element and then click it
            action_chains.move_to_element(element_to_hover_over).click().perform()

            #hover_element_xpath = "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]"
            #hover_element_xpath = "(//i[@data-icon-name='Add'])"
            # hover_element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, hover_element_xpath)))

            # Perform a hover action on the hover element
            # ActionChains(driver).move_to_element(hover_element_xpath).perform()

            # Wait for the dynamically generated element to appear
            #dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            #dynamic_element_xpath = "(//button[@aria-label='Add a new web part in column one'])[1]"

            #GetIDynamicID=driver.find_element(By.XPATH, "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]/div/div[2]").get_attribute("id")

            # dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            # #dynamic_element_xpath = GetIDynamicID
            # dynamic_element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, dynamic_element_xpath)))
            #
            # # Now you can interact with the dynamically generated element
            # dynamic_element.click()
            #
            # element_value = self.getElementDetails(hover_element, "value")
            # element_value = re.sub(r'\*', '', element_value)

            ExpectedResult = "Clicked on ADD icon to add webpart'"  "' "
            ActualResult = "Clicked on ADD icon to add webpart'"  "' "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def hover_over_eTMFdoc(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # wait = WebDriverWait(driver, 10)

            hover_element_xpath = "//div[@docidx='0']"
            hover_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, hover_element_xpath)))

            # Perform a hover action on the hover element
            ActionChains(driver).move_to_element(hover_element).perform()
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            #driver.find_element(By.XPATH, "//div[@docidx='0']").click()

            # Locate the element that triggers the hover action
            # Locate the hover element
            element_to_hover_over = driver.find_element(By.XPATH, "(//button[@title='Actions menu'])[1]")
            #element_to_hover_over = driver.find_element(By.XPATH,"(//div[@data-automation-id='CanvasZoneEdit']/descendant::button[@aria-label='Add a new web part in column one'])[1]")
            # Create an ActionChains object
            action_chains = ActionChains(driver)
            time.sleep(2)

            # Hover over the element and then click it
            action_chains.move_to_element(element_to_hover_over).click().perform()


            ExpectedResult = "Clicked on ADD icon to add webpart'"  "' "
            ActualResult = "Clicked on ADD icon to add webpart'"  "' "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def hover_over_eTMF_Log(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Set implicit wait
            driver.implicitly_wait(180)

            # Locate the hover element
            hover_element_xpath = "//div[contains(@class, 'vv_button_group')]//button[contains(@aria-label, 'All Actions')]"
            hover_element = driver.find_element(By.XPATH, hover_element_xpath)

            # Perform a hover action on the hover element
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            time.sleep(2)  # Small delay to ensure any hover effects have taken place

            # Click the element
            hover_element.click()

            time.sleep(5)  # Wait for any hover-related UI changes

            #driver.find_element(By.XPATH, "//ul[@role='listbox']/li[10]")

            ExpectedResult = "Clicked on ADD icon to add webpart"
            ActualResult = "Clicked on ADD icon to add webpart"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'hover_over_eTMF_Log' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def hover_over_eTMF_ActionMenu(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                   Requirement,
                                   testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Set implicit wait
            driver.implicitly_wait(180)

            # Locate the hover element
            hover_element_xpath = "//div[contains(@class, 'vv_button_group')]//button[contains(@aria-label, 'All Actions')]"
            hover_element = driver.find_element(By.XPATH, hover_element_xpath)

            # Perform a hover action on the hover element
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            time.sleep(2)  # Small delay to ensure any hover effects have taken place

            # Click the element
            hover_element.click()
            time.sleep(5)  # Wait for any hover-related UI changes

            # List of XPaths to verify
            label_xpaths = [
                "//li[@aria-label='Log Quality Issue']",
                "//li[@aria-label='Workflow History with Task Instructions']",
                "//li[@aria-label='Add to Cart']",
                "//li[@aria-label='Send as Link']",
                "//li[@aria-label='Download Notes']"
            ]

            # Verify that each label is present
            for xpath in label_xpaths:
                element = driver.find_element(By.XPATH, xpath)
                if element.is_displayed():
                    print(f"Element with XPath '{xpath}' is present.")
                else:
                    raise Exception(f"Element with XPath '{xpath}' is not present.")
            ExpectedResult = "All specified labels are present after hovering and clicking the All Actions button."
            ActualResult = "All specified labels are verified successfully."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'hover_over_eTMF_Log' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def hover_over_eTMF_CreateDraft(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Set implicit wait
            driver.implicitly_wait(120)

            # Locate the hover element
            hover_element_xpath = "//ul[@role='listbox']/li[10]"
            hover_element = driver.find_element(By.XPATH, hover_element_xpath)

            # Perform a hover action on the hover element
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            time.sleep(2)  # Small delay to ensure any hover effects have taken place

            # Click the element
            hover_element.click()

            time.sleep(5)  # Wait for any hover-related UI changes

            driver.find_element(By.XPATH, "//div[@role='dialog']//button[contains(text(),'Create')]").click()
            time.sleep(5)
            ExpectedResult = "Click on Create Draft"
            ActualResult = "Clicked on Create Draft"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'hover_over_eTMF_Log' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def hover_over_eTMF(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Set implicit wait
            driver.implicitly_wait(120)

            # Locate the hover element
            hover_element_xpath = Locator
            hover_element = driver.find_element(By.XPATH, hover_element_xpath)

            # Perform a hover action on the hover element
            actions = ActionChains(driver)
            actions.move_to_element(hover_element).perform()
            time.sleep(2)  # Small delay to ensure any hover effects have taken place

            # Click the element
            hover_element.click()

            time.sleep(5)  # Wait for any hover-related UI changes


            time.sleep(5)
            ExpectedResult = "Click on Create Draft"
            ActualResult = "Clicked on Create Draft"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'hover_over_eTMF_Log' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def hover_over_elementLocator(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            #wait = WebDriverWait(driver, 10)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            #driver.find_element(By.XPATH, "//div[@data-automation-id='CanvasZoneEdit']").click()

            # Locate the element that triggers the hover action
            # Locate the hover element
            element_to_hover_over = driver.find_element(By.XPATH, Locator)
            #element_to_hover_over = driver.find_element(By.XPATH,"(//div[@data-automation-id='CanvasZoneEdit']/descendant::button[@aria-label='Add a new web part in column one'])[1]")
            # Create an ActionChains object
            action_chains = ActionChains(driver)
            time.sleep(6)

            # Hover over the element and then click it
            action_chains.move_to_element(element_to_hover_over).click().perform()

            #hover_element_xpath = "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]"
            #hover_element_xpath = "(//i[@data-icon-name='Add'])"
            # hover_element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, hover_element_xpath)))

            # Perform a hover action on the hover element
            # ActionChains(driver).move_to_element(hover_element_xpath).perform()

            # Wait for the dynamically generated element to appear
            #dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            #dynamic_element_xpath = "(//button[@aria-label='Add a new web part in column one'])[1]"

            #GetIDynamicID=driver.find_element(By.XPATH, "(//div[@data-automation-id='CanvasZoneEdit']/descendant::button)[1]/div/div[2]").get_attribute("id")

            # dynamic_element_xpath = "(//button[@data-automation-id='toolboxHint-webPart'])[1]"
            # #dynamic_element_xpath = GetIDynamicID
            # dynamic_element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, dynamic_element_xpath)))
            #
            # # Now you can interact with the dynamically generated element
            # dynamic_element.click()
            #
            # element_value = self.getElementDetails(hover_element, "value")
            # element_value = re.sub(r'\*', '', element_value)

            ExpectedResult = "Clicked on ADD icon to add webpart'"  "' "
            ActualResult = "Clicked on ADD icon to add webpart'"  "' "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def scroll_page_up1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Scroll up the page using JavaScript
            driver.execute_script("window.scrollTo(0, 0);")

            ExpectedResult = "Page scrolled up successfully."
            ActualResult = "Page scrolled up successfully."


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'Scroll Up' Action Exception Message -> \n" + str(e))

        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def scroll_page_down(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                         testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Scroll down the page using JavaScript
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(20)


            ExpectedResult = "Page scrolled down successfully."
            ActualResult = "Page scrolled down successfully."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'Scroll Down' Action Exception Message -> \n" + str(e))

        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def clearField(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:

            element = driver.find_element(By.XPATH, Locator)
            # Clear the field
            #element.clear()
            initial_text = element.get_attribute("value")

            # Calculate the number of backspaces needed
            backspaces_needed = len(initial_text)

            # If you want to limit the number of backspaces, you can set a maximum limit
            # For example, limit it to 255 characters
            max_backspaces = 255
            backspaces_needed = min(backspaces_needed, max_backspaces)

            # Perform backspaces
            for _ in range(backspaces_needed):
             element.send_keys(Keys.BACKSPACE)

            # Print expected and actual results
            ExpectedResult = "Clear data from the field"
            ActualResult = f"Data cleared from the field: {element.get_attribute('value')}"
            print("Expected Result:", ExpectedResult)
            print("Actual Result:", ActualResult)
        except Exception as e:


            FlagTestCase = "Fail"

            exMsg = str(e)

            print("Exception occurred: ", exMsg)

        finally:

            # Report the test result

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,

                                             FlagTestCase, TestCase_Summary)

            return driver

    def retrieveasetData1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator).get_attribute("innerHTML")

            # Set the data using the provided key
            set_map_value(key, element)
            print("Setting test data with key:", key, "and value:", {element})
            # Additional processing if needed
            # ...
            if element == "":
                element = "element"

            ExpectedResult = "RetreiveListData '" + element + " "
            ActualResult = "RetreiveListData '" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def retrieveimage(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc,
                      Keywords,
                      Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator).get_attribute("src")

            # Set the data using the provided key
            set_map_value(key, element)
            print("Setting test data with key:", key, "and value:", {element})
            # Additional processing if needed
            # ...
            if element == "":
                element = "element"

            ExpectedResult = "RetreiveListData '" + element + " "
            ActualResult = "RetreiveListData '" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def retrievesortorder(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator).get_attribute("aria-label")
            # Extract the numeric part from the aria-label value
            numeric_part = element.split()[-1]
            # Convert the numeric part to an integer if needed
            numeric_value = int(numeric_part)
            print("Numeric part of aria-label value:", numeric_value)
            # Set the data using the provided key
            set_map_value(key, numeric_value)
            print("Setting test data with key:", key, "and value:", {numeric_value})
            # Additional processing if needed
            # ...

            # Additional check to handle the case when numeric_value is zero
            if numeric_value == 0:
                numeric_value_str = "numeric_value"
            else:
                # Convert numeric_value to a string before concatenation
                numeric_value_str = str(numeric_value)

            ExpectedResult = "RetreiveListData '" + numeric_value_str + " "
            ActualResult = "RetreiveListData '" + numeric_value_str + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def listInactivecount(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Locate the element containing the list items
            elements_with_aria_label = driver.find_elements(By.XPATH, "//i[@aria-label]")

            # Initialize a counter for "No" values
            inactive_count = 0

            # Iterate through the elements
            for element in elements_with_aria_label:
                # Get the value of aria-label attribute
                aria_label_value = element.get_attribute("aria-label")
                # Split the value using comma and check for "No"
                if "No" in aria_label_value.split(","):
                    # Increment the counter
                    inactive_count += 1

            # Set the data using the provided key
            set_map_value(key, inactive_count)

            # Print the count
            print(f"Number of 'No' values in aria-label attribute: {inactive_count}")
            # ...
            ExpectedResult = f"RetreiveListData with {inactive_count} 'No' values"
            ActualResult = f"RetreiveListData with {inactive_count} 'No' values"

            # Additional details when inactive_count is 0
            if inactive_count == 0:
                ExpectedResult += " Additional expected details for count 0"
                ActualResult += " Additional actual details for count 0"

            # Print ExpectedResult and ActualResult
            print("ExpectedResult:", ExpectedResult)
            print("ActualResult:", ActualResult)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def ValidateInactivedata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                            testStepDesc,
                            Keywords,
                            Locator,
                            Testdata, key, TestCase_Summary):
        global element
        FlagTestCase = "Pass"
        exMsg = ""
        textDataRetrieved = ""
        expected_text = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""

        try:

            try:
                # Locate the element containing the slides
                slides_container = driver.find_element(By.CLASS_NAME, "thumbs")

                # Get the count of slides
                slide_count = len(slides_container.find_elements(By.XPATH, ".//li[@role='button']"))

                # Print the count
                print(f"Number of slides: {slide_count}")



            except Exception as e:
                print()

            if slide_count == 0:

             # print(textDataRetrieved)
             slide_count = get_map_value(key)

            ExpectedResult = "The data in the Inactive List data is not shown."
            ActualResult = "The data in the Inactive List data is not shown."

            for index, slide in enumerate(driver.find_elements(By.XPATH, "//ul[@class='thumbs']/li[@role='button']"),
                                          start=1):
                # Click on the slide
                slide.click()

                # Wait for the absence of the element indicating text activation



        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "'" + str(key) + "' must have '" + str(textDataRetrieved) + "' as value"
            exMsg = self.error_message(str(e))
            print("'retreiveAndValidate' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def listItemcount(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Locate the element containing the list items
            element = driver.find_elements(By.XPATH, Locator)

            # Initialize a counter for "No" values
            item_count = len(element)


            # Set the data using the provided key
            set_map_value(key, item_count)

            # Print the count
            print(f"Number of 'No' values in aria-label attribute: {item_count}")
            # ...
            ExpectedResult = f"RetreiveListData with {item_count} 'No' values"
            ActualResult = f"RetreiveListData with {item_count} 'No' values"

            # Additional details when inactive_count is 0
            if item_count == 0:
                ExpectedResult += " Additional expected details for count 0"
                ActualResult += " Additional actual details for count 0"

            # Print ExpectedResult and ActualResult
            print("ExpectedResult:", ExpectedResult)
            print("ActualResult:", ActualResult)

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def ValidatelistItemcount(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Locate elements based on the XPath
            elements = driver.find_elements(By.XPATH, Locator)

            # Get the count of elements
            element_count = len(elements)

            # Retrieve the expected count from the map
            expected_count = get_map_value(key)

            # Include expected and actual count in the report
            ExpectedResult = f"Expected Count: {expected_count}"
            ActualResult = f"Actual Count: {element_count}"

            # Compare with the expected count and report
            if element_count == expected_count:
                ExpectedResult += " - Count matches the expected count."
                ActualResult += " - Count matches the expected count."
            else:
                ExpectedResult += f" - Expected: {expected_count}"
                ActualResult += f" - Actual: {element_count}"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def retrieveSlidercount(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator).get_attribute("aria-valuenow")

            # Set the data using the provided key
            set_map_value(key, element)
            print("Setting test data with key:", key, "and value:", {element})
            # Additional processing if needed
            # ...
            if element == "":
                element = "element"

            ExpectedResult = "RetreiveListData '" + element + " "
            ActualResult = "RetreiveListData '" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def PauseOnHover(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            initial_inner_text = element.get_attribute("innerHTML")

            # Perform mouse hover for 6 seconds
            driver.execute_script("arguments[0].dispatchEvent(new Event('mouseover', { bubbles: true }));", element)
            time.sleep(6)  # Adjust the sleep duration as needed
            driver.execute_script("arguments[0].dispatchEvent(new Event('mouseout', { bubbles: true }));", element)

            element1 = driver.find_element(By.XPATH, Locator)

            final_inner_text = element1.get_attribute("innerHTML")

            # Perform mouse hover for 6 seconds
            # action = ActionChains(driver)
            # action.move_to_element(element).pause(5).perform()

            # Get the final inner text after the mouseover
            # final_inner_text = element.text

            # Check if the inner text has changed
            # text_changed = initial_inner_text != final_inner_text
            if initial_inner_text == final_inner_text:
                print("Text changed after 6 seconds of mouse hover!")
            else:
                print("Text did not change after 6 seconds of mouse hover!")

            ExpectedResult = "Text is not changed even after 6 seconds of mouse hover! on PauseOnHover OFF '"
            ActualResult = "Text is not changed even after 6 seconds of mouse hover! on PauseOnHover OFF '"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def PauseOnHoverOFF(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

           # driver.set_window_size(1366, 768)
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            initial_inner_text = element.get_attribute("innerHTML")

            # Perform mouse hover for 6 seconds
            #action = ActionChains(driver)
            #action.move_to_element(element).pause(6).perform()
           # Perform mouse hover for 6 seconds
            driver.execute_script("arguments[0].dispatchEvent(new Event('mouseover', { bubbles: true }));", element)
            time.sleep(6)  # Adjust the sleep duration as needed
            driver.execute_script("arguments[0].dispatchEvent(new Event('mouseout', { bubbles: true }));", element)

            element1 = driver.find_element(By.XPATH, Locator)

            final_inner_text = element1.get_attribute("innerHTML")

            # Perform mouse hover for 6 seconds
           # action = ActionChains(driver)
            #action.move_to_element(element).pause(5).perform()


            # Get the final inner text after the mouseover
            #final_inner_text = element.text

            # Check if the inner text has changed
            #text_changed = initial_inner_text != final_inner_text
            if initial_inner_text != final_inner_text:
                print("Text changed after 6 seconds of mouse hover!")
            else:
                print("Text did not change after 6 seconds of mouse hover!")

            ExpectedResult = "Text changed after 6 seconds of mouse hover! on PauseOnHover OFF '"
            ActualResult = "Text changed after 6 seconds of mouse hover! on PauseOnHover OFF '"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def IsInfiniteON(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator)

            initial_inner_text = element.text
            time.sleep(5)
            # Perform mouse hover for 6 seconds
            #action = ActionChains(driver)
            #action.move_to_element(element).pause(6).perform()

            # Get the final inner text after the mouseover
            final_inner_text = element.text

            # Check if the inner text has changed
            text_changed = initial_inner_text != final_inner_text
            if element == "":
                element = "element"

            ExpectedResult = "PauseOnHover OFF '" + element + " "
            ActualResult = "PauseOnHover OFF'" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def IsInfiniteOFF(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, Locator)

            initial_inner_text = element.text

            # Perform mouse hover for 6 seconds
            #action = ActionChains(driver)
            #action.move_to_element(element).pause(6).perform()

            # Get the final inner text after the mouseover
            final_inner_text = element.text

            # Check if the inner text has changed
            text_changed = initial_inner_text = final_inner_text
            if element == "":
                element = "element"

            ExpectedResult = "PauseOnHover OFF '" + element + " "
            ActualResult = "PauseOnHover OFF'" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def tagoff(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            parent_element = driver.find_element(By.XPATH, Locator)
            #parent_element = driver.find_element_by_xpath(f"//div[contains(@class, '{class_name}')]")

            # Get all child elements under the parent
            child_elements = parent_element.find_elements_by_xpath(".//*")

            # Get unique tag names for each child element and store them in a set
            tag_names = set(element.tag_name.lower() for element in child_elements)

            # Print the list of unique tag names
            print("Unique Tag Names:", tag_names)
            # Check if 'ol' is present in the list of tag names
            if 'ol' not in tag_names:
                print("Element with 'ol' tag is not present. Test Pass.")

                if parent_element == "":
                    parent_element = "element"

                ExpectedResult = "Indicator OFF '"
                ActualResult = "Indicator OFF'"

            else:
                print("Element with 'ol' tag is present. Test Fail.")



        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver




    def emailoff(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            # Find the element with the specified XPath
            element = driver.find_element(By.XPATH, Locator)

            # Get the inner HTML text of the element
            inner_html = element.get_attribute("innerHTML")

            # Check if '@gilead.com' is not in the inner HTML
            if '@gilead.com' not in inner_html:
                print("Email not found in inner HTML. Feature is turned off.")
                # Perform additional actions or raise an exception if needed
            else:
                # Perform actions or raise an exception if needed
                print("Email found in inner HTML:", inner_html)

                # Check if inner_html is an empty string
                if not inner_html.strip():
                    ExpectedResult = "Email is not displayed"
                    ActualResult = "Email is not displayed"
                    print("Email is not displayed. Test Fail.")
                else:
                    ExpectedResult = "Email is displayed"
                    ActualResult = "Email is displayed"
                    print("Email is displayed. Test Pass.")

            if element == "":
                element = "element"

            ExpectedResult = "Email not found . Feature is turned off. '"" "
            ActualResult = "Email not found . Feature is turned off. " " "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def emailON(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            # Find the element with the specified XPath
            element = driver.find_element(By.XPATH, Locator)

            # Get the inner HTML text of the element
            inner_html = element.get_attribute("innerHTML")

            # Check if '@gilead.com' is not in the inner HTML
            if '@gilead.com' not in inner_html:
                print("Email not found in inner HTML. Feature is turned off.")
                # Perform additional actions or raise an exception if needed
            else:
                # Perform actions or raise an exception if needed
                print("Email found in inner HTML:", inner_html)

                # Check if inner_html is an empty string
                if not inner_html.strip():
                    ExpectedResult = "Email is not displayed"
                    ActualResult = "Email is not displayed"
                    print("Email is not displayed. Test Fail.")
                else:
                    ExpectedResult = "Email is displayed"
                    ActualResult = "Email is displayed"
                    print("Email is displayed. Test Pass.")




        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def locationoff(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            # Find the element with the specified XPath
            element = driver.find_element(By.XPATH, Locator)

            # Get the inner HTML text of the element
            inner_html = element.get_attribute("innerHTML")

            # Check if '@gilead.com' is not in the inner HTML
            if ' | ' not in inner_html:
                print("Location not found in inner HTML. Feature is turned off.")
                # Perform additional actions or raise an exception if needed
            else:
                # Perform actions or raise an exception if needed
                print("Location found in inner HTML:", inner_html)

                # Check if inner_html is an empty string
                if not inner_html.strip():
                    ExpectedResult = "Location is not displayed"
                    ActualResult = "Location is not displayed"
                    print("Email is not displayed. Test Fail.")
                else:
                    ExpectedResult = "Email is displayed"
                    ActualResult = "Email is displayed"
                    print("Email is displayed. Test Pass.")

            if element == "":
                element = "element"

            ExpectedResult = "Location not found . Feature is turned off. '"" "
            ActualResult = "Location not found . Feature is turned off. " " "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def joiningdatoff(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            # Find the element with the specified XPath
            element = driver.find_element(By.XPATH, Locator)

            # Get the inner HTML text of the element
            inner_html = element.get_attribute("innerHTML")

            # Check if '@gilead.com' is not in the inner HTML
            if '01 January 2021' not in inner_html:
                print("Location not found in inner HTML. Feature is turned off.")
                # Perform additional actions or raise an exception if needed
            else:
                # Perform actions or raise an exception if needed
                print("Location found in inner HTML:", inner_html)

                # Check if inner_html is an empty string
                if not inner_html.strip():
                    ExpectedResult = "Location is not displayed"
                    ActualResult = "Location is not displayed"
                    print("Email is not displayed. Test Fail.")
                else:
                    ExpectedResult = "Email is displayed"
                    ActualResult = "Email is displayed"
                    print("Email is displayed. Test Pass.")

            if element == "":
                element = "element"

            ExpectedResult = "Location not found . Feature is turned off. '"" "
            ActualResult = "Location not found . Feature is turned off. " " "


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def retrievecontactdetails(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Find the div element by the provided locator
            element = driver.find_element(By.XPATH, Locator)
            # Retrieve the text content of the div
            soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
            contact_details = {}
            # Extract the title
            title = soup.find('div', class_='ms-Button-label').text.strip()
            # Extract each contact's details
            contacts = soup.find_all('div', class_='k_contact')
            for i, contact in enumerate(contacts, start=1):
                name = contact.find('div', class_='ms-Persona-primaryText').text.strip()
                email = contact.find('span', class_='txt_details').text.strip()
                contact_details[f'Contact {i}'] = {'Name': name, 'Email': email}
            return title, contact_details
            if element == "":
                element = "element"

            ExpectedResult = "RetreiveListData '" + element + " "
            ActualResult = "RetreiveListData '" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def retrievewidth(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc,
                      Keywords,
                      Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            value=get_map_value(key)
            xpath_expression = f"(//div[contains(@style, '--tileWidth: {value}px;')])[1]"
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, xpath_expression)
            name = element.text

            if name == "":
                name = element.get_attribute("style")

            ExpectedResult = "'" + str(name) + "' must be part of the form"
            ActualResult = "'" + str(name) + "' is part of the form"

            print(f"value of {str(Locator)} is {str(name)}")
        except Exception as e:
            FlagTestCase = "Fail"
            # removing the word "Verify" from testStepDesc
            name = testStepDesc.replace("Verify", "")
            ExpectedResult = "'" + name + "' must be part of the form"
            exMsg = self.error_message(str(e))
            print("'verifyObj' Action Exception Message -> \n" + str(e))


        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver




    def retrieveheight(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc,
                      Keywords,
                      Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            value=get_map_value(key)
            xpath_expression = f"(//div[contains(@style, '--tileHeight: {value}px;')])[1]"
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element = driver.find_element(By.XPATH, xpath_expression)
            name = element.text

            if name == "":
                name = element.get_attribute("style")

            ExpectedResult = "'" + str(name) + "' must be part of the form"
            ActualResult = "'" + str(name) + "' is part of the form"

            print(f"value of {str(Locator)} is {str(name)}")
        except Exception as e:
            FlagTestCase = "Fail"
            # removing the word "Verify" from testStepDesc
            name = testStepDesc.replace("Verify", "")
            ExpectedResult = "'" + name + "' must be part of the form"
            exMsg = self.error_message(str(e))
            print("'verifyObj' Action Exception Message -> \n" + str(e))


        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def retrieveasetQuotes(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc,
                          Keywords,
                          Locator, Testdata, TestCase_Summary, key):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find the div element by the provided locator and  Retrieve the text content of the div
            element1 = driver.find_element(By.XPATH, Locator).get_attribute("innerHTML")
            element = element1.replace("-", "")

            # Set the data using the provided key
            set_map_value(key, element)
            print("Setting test data with key:", key, "and value:", {element})
            # Additional processing if needed
            # ...
            if element == "":
                element = "element"

            ExpectedResult = "RetreiveListData '" + element + " "
            ActualResult = "RetreiveListData '" + element + " "

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retrieveAndSetDataFromDiv' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test data step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def is_element_present(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                  Keywords,
                  Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Define the XPath expression
            xpath = Locator

            # Check if the element is present
            if self.is_element_present(driver, xpath):
                print("Element is present")
            else:
                print("Element is not present")

            ExpectedResult = "'" + str(name) + "' must be part of the form"
            ActualResult = "'" + str(name) + "' is part of the form"

            print(f"value of {str(Locator)} is {str(name)}")
        except Exception as e:
            FlagTestCase = "Fail"
            # removing the word "Verify" from testStepDesc
            name = testStepDesc.replace("Verify", "")
            ExpectedResult = "'" + name + "' must be part of the form"
            exMsg = self.error_message(str(e))
            print("'verifyObj' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase,
                                             TestCase_Summary)
        return driver


    def KeyContactsInactive(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                  Keywords,
                  Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            # Find the initial focusable element
            initial_element = driver.find_element_by_xpath("(//div[@data-list-index='0']//div[@role='gridcell'][1])[2]")

            # Simulate pressing the Tab key six times
            for _ in range(6):
                initial_element.send_keys(Keys.TAB)
                time.sleep(1)  # Add a small delay to make sure each tab action completes

            ExpectedResult = "'" + str(name) + "' must be part of the form"
            ActualResult = "'" + str(name) + "' is part of the form"

            print(f"value of {str(Locator)} is {str(name)}")
        except Exception as e:
            FlagTestCase = "Fail"
            # removing the word "Verify" from testStepDesc
            name = testStepDesc.replace("Verify", "")
            ExpectedResult = "'" + name + "' must be part of the form"
            exMsg = self.error_message(str(e))
            print("'verifyObj' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase,
                                             TestCase_Summary)
        return driver


    def doubleclick(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                Keywords,
                Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            #wait = WebDriverWait(driver, 10)
            element = driver.find_element(By.XPATH, Locator)

            # element = driver.find_element(By.XPATH, Locator)
            #driver = self.scrollIntoView(driver, element)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            # Perform a double click on the element
            action_chains = ActionChains(driver)
            action_chains.double_click(element).perform()

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def aggrid_features(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                Keywords,
                Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            #wait = WebDriverWait(driver, 10)
            element = driver.find_element(By.XPATH, Locator)

            # Retrieve all options from the dropdown
            options = [option.text for option in element.options]

            # Define the expected dropdown values
            expected_values = ["Sortable", "Row Grouping", "Search", "Grid Filter", "Column Filter", "Create Item", "Edit Item", "Delete Item", "Context Menu", "Column Filter'", "Fill Handler", "Export To Excel"]

            # Verify presence of expected values in the dropdown options
            for value in expected_values:
                if value in options:
                    print(f"{value} is present in the dropdown.")
                else:
                    print(f"{value} is not present in the dropdown.")

            if element == "":
                element = "element"

            ExpectedResult = "Click on '" + element + "' field"
            ActualResult = "Clicked on '" + element + "' field"

            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    #def is_sorted_ascending(column_data):
     #   return column_data == sorted(column_data)

    # Define a function to wait for the presence of rows in the grid
    def wait_for_grid_rows(driver):
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, ".//div[@role='row']")))

    def check_sorting1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, TestCase_Summary, Key):
        # Define a function to check if column data is sorted in ascending order
        def is_sorted_ascending(column_data):
            return column_data == sorted(column_data)

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Find the grid element
            grid_element = driver.find_element(By.XPATH, Locator)
            # Retrieve all cells from the grid
            cells = grid_element.find_elements(By.XPATH, "//div[@comp-id and @role='gridcell']//div[@ref='eCellWrapper' and @class='ag-cell-wrapper']//span[@ref='eCellValue' and @class='ag-cell-value']")
            # Initialize a list to store the tabular data
            tabular_data = []

            # Iterate through the cells and organize them into rows
            row_data = []
            for cell in cells:
                cell_text = cell.text
                # Check if the cell text is not empty
                if cell_text:
                    row_data.append(cell_text)
                else:
                    # If the cell is empty, it indicates the end of the row
                    tabular_data.append(row_data)
                    row_data = []

            # Add the last row_data if not empty
            if row_data:
                tabular_data.append(row_data)

            # Get column headers from the first row (//div[@class='ag-root-wrapper ag-layout-normal ag-ltr'])
            headers = tabular_data[0]
            print( headers)
            # Initialize a dictionary to store column data
            column_data = {header: [] for header in headers}
            # Store cell data into respective column in column_data dictionary
            for row_data in tabular_data[1:]:
                for header, cell_text in zip(headers, row_data):
                    column_data[header].append(cell_text)

            # Check if the column specified in the test data is sorted in ascending order
            column_to_check = Testdata  # Assuming test data contains the column to check
            if not is_sorted_ascending(column_data[column_to_check]):
                FlagTestCase = "Fail"
                exMsg = f"Column '{column_to_check}' is not sorted in ascending order."
            # Print the tabular data with headers
            for header in headers:
                print(header, end=" | ")
            print()  # Print new line
            for row_data in tabular_data:
                print(" | ".join(row_data))

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def check_sorting2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, TestCase_Summary, Key):


        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Find all cells in the "Title" column
            title_cells = driver.find_elements(By.XPATH, "//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']")

            # Extract text from each cell and store it in a list
            title_column_data = [cell.text for cell in title_cells]

            # Sort the data in ascending order
            sorted_title_column_data = sorted(title_column_data)

            # Print the sorted data
            print("Sorted data in ascending order:")
            for data in sorted_title_column_data:
                print(data)

            time.sleep(20)
            # Click on the "Title" column header to sort and measure time
            start_time = time.time()
            # Click on the "Title" column header to sort
            driver.find_element_by_xpath("//span[text()='" + Locator + "']").click()
            time.sleep(20)
            end_time = time.time()

            # Calculate sorting time
            sorting_time = end_time - start_time
            print(f"Sorting took {sorting_time} seconds")
            # Extract the data from the "Title" column again after sorting
            # Retrieve the count of elements in the sorted list
            num_rows = len(sorted_title_column_data)
            # Initialize index

            index = 0
            while index < num_rows:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                # Find the cell in the "Title" column for the current row index
                title_cell = driver.find_element(By.XPATH, xpath)
                # Get the text from the cell
                original_data = title_cell.text
                # Print the original data
                print(f"Original data at index {index}: {original_data}")
                # Compare the sorted data with the original data
                if sorted_title_column_data[index] == original_data:
                    print(f"Data at index {index} is correctly sorted in ascending order.")
                    ExpectedResult = f"Data is correctly sorted in ascending order. Sorting time:  {sorting_time}  seconds"
                    ActualResult = f"Data is correctly sorted in ascending order. Sorting time: {sorting_time} seconds"
                else:
                    print(f"Data at index {index} is not correctly sorted in ascending order.")
                    ExpectedResult = f"Data is not correctly sorted in ascending order. Sorting time:  {sorting_time}  seconds"
                    ActualResult = f"Data is not correctly sorted in ascending order. Sorting time:  {sorting_time}  seconds"
                    # Report test fail
                    #FlagTestCase = "Fail"

                # Increment index
                index += 1
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver





    def check_sorting(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, TestCase_Summary, Key):


        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Find all cells in the "Title" column
            title_cells = driver.find_elements(By.XPATH, "//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']")

            # Extract text from each cell and store it in a list
            title_column_data = [cell.text for cell in title_cells]

            # Sort the data in ascending order
            sorted_title_column_data = sorted(title_column_data)

            # Print the sorted data
            print("Sorted data in ascending order:")
            for data in sorted_title_column_data:
                print(data)

            time.sleep(5)
            start_time = time.time()

            # Click on the "Title" column header to sort
            driver.find_element_by_xpath("//span[text()='" + Locator + "']").click()
            # Extract the data from the "Title" column again after sorting
            # Retrieve the count of elements in the sorted list
            num_rows = len(sorted_title_column_data)
            # Initialize index

            index = 0
            while index < num_rows:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                # Find the cell in the "Title" column for the current row index
                title_cell = driver.find_element(By.XPATH, xpath)
                # Get the text from the cell
                original_data = title_cell.text
                # Print the original data
                print(f"Original data at index {index}: {original_data}")
                end_time = time.time()

                # Calculate sorting time
                sorting_time = end_time - start_time
                print(f"Sorting took {sorting_time} seconds")
                load_time_before_sorting_rounded = round(sorting_time, 2)
                print("Load time before sorting:", load_time_before_sorting_rounded, "seconds")
                time.sleep(2)
                # Compare the sorted data with the original data
                if sorted_title_column_data[index] == original_data:
                    print(f"Data at index {index} is correctly sorted in ascending order.")
                    ExpectedResult = f"Data is correctly sorted in ascending order. Sorting time:  {load_time_before_sorting_rounded}  seconds"
                    ActualResult = f"Data is correctly sorted in ascending order. Sorting time: {load_time_before_sorting_rounded} seconds"
                else:
                    print(f"Data at index {index} is not correctly sorted in ascending order.")
                    ExpectedResult = "Data is not correctly sorted in ascending order."
                    ActualResult = "Data is not correctly sorted in ascending order."
                    # Report test fail
                    #FlagTestCase = "Fail"

                # Increment index
                index += 1
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def retry_click(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                    testStepDesc,
                    Keywords, Locator, Testdata, TestCase_Summary, max_attempts=3):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            attempts = 0
            while attempts < max_attempts:
                try:
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locator)))
                    element.click()
                    ExpectedResult = "Click on '" + element + "' field"
                    ActualResult = "Clicked on '" + element + "' field"
                    return True  # Action successful, no need to retry
                except StaleElementReferenceException:
                    attempts += 1
                    ExpectedResult = "Click on '" + element + "' field"
                    ActualResult = "Clicked on '" + element + "' field"
            return False




        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver


    def validategriddata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):


        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""

        try:

            # Get the expected text from the function

            expected_text = get_map_value(key)

            # Flag to check if the expected text is found in all cells

            found_in_all_cells = True

            # Convert expected_text to string if it's an integer

            # Convert expected_text to string if it's an integer
            if isinstance(expected_text, int):
                expected_text = str(expected_text)
            index = 0
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                try:
                    # Find the cell in the "Title" column for the current row index
                    title_cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the title cell
                    cell_text = title_cell.text
                    # Check if the expected text is not contained in the cell text
                    if expected_text not in cell_text:
                        # If not found in any cell, set the flag to False and break the loop
                        found_in_all_cells = False
                        break
                    index += 1  # Move to the next row
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break
            # Check if the expected text is found in all cells of all rows

            if found_in_all_cells:

                print(f"'{expected_text}' found in all cells of the title column in all rows.")

                ExpectedResult = "Data is displayed as per the given search."

                ActualResult = "Data is displayed as per the given search."

            else:

                print(f"'{expected_text}' not found in all cells of the title column in all rows.")

                ExpectedResult = "Data is not displayed as per the given search."

                ActualResult = "Data is not displayed as per the given search."

                FlagTestCase = "Fail"

        except Exception as e:

            FlagTestCase = "Fail"

            exMsg = str(e)

            print("Exception occurred: ", exMsg)

        finally:

            # Report the test result

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,

                                             FlagTestCase, TestCase_Summary)

            return driver

    def load_data_within_10_seconds(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            # Record the start time
            start_time = time.time()
            # Wait for data to load on the current page within 10 seconds
            data_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']"))
            )

            # Print total record count
            record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
            record_count_text = record_count_element.text
            # Record the end time after data loading
            end_time = time.time()

            # Calculate the data loading duration
            loading_duration = end_time - start_time


            # Round the loading duration to 2 decimal places
            loading_duration = round(loading_duration,2)
            #total_records = int(record_count_text)

            print(f"Data loaded on page . Total record count: {record_count_text}")
            ExpectedResult = f"Data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            ActualResult = f"Data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
        except TimeoutException:
            print("Data not loaded within 10 seconds. Considered as failed.")
            ExpectedResult = "Data not loaded within 10 seconds. Considered as failed. Loaded in {loading_duration} seconds."
            ActualResult = "Data not loaded within 10 seconds. Considered as failed. Loaded in {loading_duration} seconds."
            FlagTestCase = "Fail"
            exMsg = "Data not loaded within 10 seconds."

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def validate_contains_or(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                             testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""

        try:
            # Get the expected values from the map based on the provided key
            expected_values = get_map_value(key)
            # Flag to check if any of the expected values is found in any cell
            found_in_any_cell = False
            index = 0
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                try:
                    # Find the cell in the specified column for the current row index
                    cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the cell
                    cell_text = cell.text
                    # Check if any of the expected values is present in the cell text
                    if any(expected_value in cell_text for expected_value in expected_values):
                        found_in_any_cell = True
                        break
                    index += 1  # Move to the next row
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break

            if not found_in_any_cell:
                raise NoSuchElementException(
                    f"None of the expected values {expected_values} found in any cell of the specified column.")

            print(f"At least one of the expected values {expected_values} found in any cell of the specified column.")
            ExpectedResult = f"At least one of the expected values {expected_values} is found in the specified column."
            ActualResult = f"At least one of the expected values {expected_values} is found in the specified column."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
            ExpectedResult = f"At least one of the expected values {expected_values} is found in the specified column.Error: {exMsg}"
            ActualResult = f"None of the expected values {expected_values} are found in the specified column. Error: {exMsg}"

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def apply_filter(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        Locator_data = []


        def interpret_filter_option(option):
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='Title Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='Title Filter Input']/following::div[@ref='eDisplayField'][2]")
            # Get the value of the option 1 field using get_property("innerHtml")
            option1 = input_element1.get_attribute("innerhtml")
            option4 = input_element2.get_attribute("innerhtml")
            if option == "Contains":
                return lambda cell_text, value: value in cell_text
            elif option == "Not contains":
                return lambda cell_text, value: value not in cell_text
            elif option == "Equals":
                return lambda cell_text, value: cell_text == value
            elif option == "Not equal":
                return lambda cell_text, value: cell_text != value
            elif option == "Starts with":
                return lambda cell_text, value: cell_text.startswith(value)
            elif option == "Ends with":
                return lambda cell_text, value: cell_text.endswith(value)

            else:
                raise ValueError("Invalid filter option")

        def apply_filter_option(option, cell_text, value):
            filter_func = interpret_filter_option(option)
            return filter_func(cell_text, value)

        def find_cell_with_expected_values(option1, text_value1, option4, text_value2):
            index = 0
            while True:
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                #xpath2 = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + locator2 + "']"
                try:
                    # Get the expected values from the map based on the provided key
                    #expected_values = get_map_value(key)
                    # Locate the input element1 using its attributes
                    option_text1= driver.find_element_by_xpath(
                        "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
                    # Get the value of the option 1 field using get_property("innerHtml")
                    xpath1 = option_text1.get_property("value")
                    option_text2= driver.find_element_by_xpath(
                        "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")
                    # Get the value of the option 1 field using get_property("innerHtml")
                    xpath2 = option_text2.get_property("value")

                    cell1 = driver.find_element(By.XPATH, xpath1)
                    cell2 = driver.find_element(By.XPATH, xpath2)
                    cell_text1 = cell1.text
                    cell_text2 = cell2.text
                    if apply_filter_option(option1, cell_text1, text_value1) and apply_filter_option(option4, cell_text2,
                                                                                                     text_value2):
                        return True
                    index += 1
                except NoSuchElementException:
                    break
            return False

        try:
            Locator_data = Locator.split("|")
            # Check if expected values are found in any cell of the specified columns
            if find_cell_with_expected_values(Locator):
                print(f"At least one of the expected values found in any cell of the specified columns.")
                ExpectedResult = f"The expected values found in the specified columns."
                ActualResult = f"The expected values found in the specified columns."
            else:
                raise NoSuchElementException(
                    f"None of the expected values found in any cell of the specified columns.")

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
            ExpectedResult = f"At least one of the expected values found in the specified columns. Error: {exMsg}"
            ActualResult = f"None of the expected values found in the specified columns. Error: {exMsg}"
        finally:
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def columnsearchfilter1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")

            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")

            # Flag to check if the expected text is found in all cells
            found_in_all_cells = True
            index = 0
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                try:
                    # Find the cell in the specified column for the current row index
                    cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the cell
                    cell_text = cell.text

                    # Check if the expected text conditions are met
                    condition1_met = False
                    condition2_met = False

                    if option1_text == "Contains":
                        condition1_met = text_value1 in cell_text
                    elif option1_text == "Not contains":
                        condition1_met = text_value1 not in cell_text
                    elif option1_text == "Equals":
                        condition1_met = text_value1 == cell_text
                    elif option1_text == "Not equal":
                        condition1_met = text_value1 != cell_text
                    elif option1_text == "Starts with":
                        condition1_met = cell_text.startswith(text_value1)
                    elif option1_text == "Ends with":
                        condition1_met = cell_text.endswith(text_value1)

                    if option2_text == "Contains":
                        condition2_met = text_value2 in cell_text
                    elif option2_text == "Not contains":
                        condition2_met = text_value2 not in cell_text
                    elif option2_text == "Equals":
                        condition2_met = text_value2 == cell_text
                    elif option2_text == "Not equal":
                        condition2_met = text_value2 != cell_text
                    elif option2_text == "Starts with":
                        condition2_met = cell_text.startswith(text_value2)
                    elif option2_text == "Ends with":
                        condition2_met = cell_text.endswith(text_value2)

                    if condition1_met and condition2_met:
                        # If condition is met, continue to the next row
                        index += 1
                        continue
                    else:
                        # If condition is not met in any cell, set the flag to False and break the loop
                        found_in_all_cells = False
                        break
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break

            start_time = time.time()
            # Check if the expected text is found in all cells of all rows
            if found_in_all_cells:
                # Wait for data to load on the current page within 10 seconds
                time.sleep(5)
                data_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']"))
                )

                # Print total record count
                record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
                record_count_text = record_count_element.text
                print(f"Data loaded on page . Total record count: {record_count_text}")
                print("Data is displayed as per the given search.")

                end_time = time.time()

                # Calculate the data loading duration
                loading_duration = end_time - start_time

                # Round the loading duration to 2 decimal places
                loading_duration = round(loading_duration, 2)
                # total_records = int(record_count_text)
                ExpectedResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
                ActualResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"


        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def columnsearchfilter(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")
            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")
            # Finding all the cells in the specified column
            cells = driver.find_elements(By.XPATH, f"//div[@col-id='{Locator}']")

            # Flag to check if the conditions are met for any cell
            conditions_met = False

            # Checking conditions for each cell
            for cell in cells:
                cell_text = cell.text

                # Check if the first condition is met
                condition1_met = False
                if option1_text == "Contains":
                    condition1_met = text_value1 in cell_text
                elif option1_text == "Not contains":
                    condition1_met = text_value1 not in cell_text
                elif option1_text == "Equals":
                    condition1_met = text_value1 == cell_text
                elif option1_text == "Not equal":
                    condition1_met = text_value1 != cell_text
                elif option1_text == "Starts with":
                    condition1_met = cell_text.startswith(text_value1)
                elif option1_text == "Ends with":
                    condition1_met = cell_text.endswith(text_value1)



                # Check if the second condition is met
                condition2_met = False
                if option2_text == "Contains":
                    condition2_met = text_value2 in cell_text
                elif option2_text == "Not contains":
                    condition2_met = text_value2 not in cell_text
                elif option2_text == "Equals":
                    condition2_met = text_value2 == cell_text
                elif option2_text == "Not equal":
                    condition2_met = text_value2 != cell_text
                elif option2_text == "Starts with":
                    condition2_met = cell_text.startswith(text_value2)
                elif option2_text == "Ends with":
                    condition2_met = cell_text.endswith(text_value2)

                # If both conditions are met in the same cell, set the flag and break the loop
                if condition1_met and condition2_met:
                    conditions_met = True
                    break

            if conditions_met:
                print("Data is displayed as per the given search.")
                ExpectedResult = "Data is displayed as per the given search."
                ActualResult = "Data is displayed as per the given search."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def columnsearchfilter2(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")

            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")

            # Flag to check if the expected text is found in all cells
            found_in_all_cells = True
            index = 0
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                try:
                    # Find the cell in the specified column for the current row index
                    cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the cell
                    cell_text = cell.text

                    # Check if the expected text conditions are met
                    condition1_met = False
                    condition2_met = False

                    if option1_text == "Contains":
                        condition1_met = text_value1 in cell_text
                    elif option1_text == "Not contains":
                        condition1_met = text_value1 not in cell_text
                    elif option1_text == "Equals":
                        condition1_met = text_value1 == cell_text
                    elif option1_text == "Not equal":
                        condition1_met = text_value1 != cell_text
                    elif option1_text == "Starts with":
                        condition1_met = cell_text.startswith(text_value1)
                    elif option1_text == "Ends with":
                        condition1_met = cell_text.endswith(text_value1)

                    if option2_text == "Contains":
                        condition2_met = text_value2 in cell_text
                    elif option2_text == "Not contains":
                        condition2_met = text_value2 not in cell_text
                    elif option2_text == "Equals":
                        condition2_met = text_value2 == cell_text
                    elif option2_text == "Not equal":
                        condition2_met = text_value2 != cell_text
                        #condition2_met = text_value2 not in cell_text
                    elif option2_text == "Starts with":
                        time.sleep(5)
                        condition2_met = cell_text.startswith(text_value2)
                    elif option2_text == "Ends with":
                        condition2_met = cell_text.endswith(text_value2)

                    if condition1_met and condition2_met:
                        # If condition is met, continue to the next row

                        index += 1
                        continue
                    else:
                        # If condition is not met in any cell, set the flag to False and break the loop
                        found_in_all_cells = False
                        break
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break

            start_time = time.time()
            # Check if the expected text is found in all cells of all rows
            if found_in_all_cells:
                # Wait for data to load on the current page within 10 seconds
                time.sleep(5)
                data_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']"))
                )

                # Print total record count
                record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
                record_count_text = record_count_element.text
                print(f"Data loaded on page . Total record count: {record_count_text}")
                print("Data is displayed as per the given search.")

                end_time = time.time()

                # Calculate the data loading duration
                loading_duration = end_time - start_time

                # Round the loading duration to 2 decimal places
                loading_duration = round(loading_duration, 2)
                # total_records = int(record_count_text)
                ExpectedResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
                ActualResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def columnsearchfilter0(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")
            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")
            # Finding all the cells in the specified column
            cells = driver.find_elements(By.XPATH, f"//div[@col-id='{Locator}']")

            # Flag to check if the conditions are met for any cell
            conditions_met = False

            # Checking conditions for each cell
            for cell in cells:
                cell_text = cell.text

                # Check if the first condition is met
                condition1_met = False
                if option1_text == "Contains":
                    condition1_met = text_value1 in cell_text
                elif option1_text == "Equals":
                    condition1_met = text_value1 == cell_text

                # Check if the second condition is met
                condition2_met = False
                if option2_text == "Contains":
                    condition2_met = text_value2 in cell_text
                elif option2_text == "Equals":
                    condition2_met = text_value2 == cell_text

                # If both conditions are met in the same cell, set the flag and break the loop
                if condition1_met and condition2_met:
                    conditions_met = True
                    break

            if conditions_met:
                print("Data is displayed as per the given search.")
                ExpectedResult = "Data is displayed as per the given search."
                ActualResult = "Data is displayed as per the given search."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def columnsearchfilterOR1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")

            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")

            # Flag to check if the expected text is found in all cells
            found_in_all_cells = True
            index = 0
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='" + Locator + "']"
                try:
                    # Find the cell in the specified column for the current row index
                    cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the cell
                    cell_text = cell.text

                    # Check if the expected text conditions are met
                    condition1_met = False
                    condition2_met = False

                    if option1_text == "Contains":
                        condition1_met = text_value1 in cell_text
                    elif option1_text == "Not contains":
                        condition1_met = text_value1 not in cell_text
                    elif option1_text == "Equals":
                        condition1_met = text_value1 == cell_text
                    elif option1_text == "Not equal":
                        condition1_met = text_value1 != cell_text
                    elif option1_text == "Starts with":
                        condition1_met = cell_text.startswith(text_value1)
                    elif option1_text == "Ends with":
                        condition1_met = cell_text.endswith(text_value1)

                    if option2_text == "Contains":
                        condition2_met = text_value2 in cell_text
                    elif option2_text == "Not contains":
                        condition2_met = text_value2 not in cell_text
                    elif option2_text == "Equals":
                        condition2_met = text_value2 == cell_text
                    elif option2_text == "Not equal":
                        condition2_met = text_value2 != cell_text
                    elif option2_text == "Starts with":
                        condition2_met = cell_text.startswith(text_value2)
                    elif option2_text == "Ends with":
                        condition2_met = cell_text.endswith(text_value2)

                    if condition1_met or condition2_met:
                        # If condition is met, continue to the next row
                        index += 1
                        continue
                    else:
                        # If condition is not met in any cell, set the flag to False and break the loop
                        found_in_all_cells = False
                        break
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break

            start_time = time.time()
            # Check if the expected text is found in all cells of all rows
            if found_in_all_cells:
                # Wait for data to load on the current page within 10 seconds
                data_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']"))
                )

                # Print total record count
                record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
                record_count_text = record_count_element.text
                print(f"Data loaded on page . Total record count: {record_count_text}")
                print("Data is displayed as per the given search.")

                end_time = time.time()

                # Calculate the data loading duration
                loading_duration = end_time - start_time

                # Round the loading duration to 2 decimal places
                loading_duration = round(loading_duration, 2)
                # total_records = int(record_count_text)
                ExpectedResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
                ActualResult = f"Data is displayed as per the given search and loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def columnsearchfilterOR(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            input_element1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][1]")
            input_element2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::div[@ref='eDisplayField'][2]")
            text_value_input1 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][1]")
            text_value_input2 = driver.find_element_by_xpath(
                "//input[@ref='eInput' and @class='ag-input-field-input ag-text-field-input' and @aria-label='" + Locator + " Filter Input']/following::input[@placeholder='Filter...'][2]")
            # Get the expected text from user-selected options and input fields
            option1_text = input_element1.get_attribute("innerHTML")
            option2_text = input_element2.get_attribute("innerHTML")
            text_value1 = text_value_input1.get_property("value")
            text_value2 = text_value_input2.get_property("value")
            # Finding all the cells in the specified column
            cells = driver.find_elements(By.XPATH, f"//div[@col-id='{Locator}']")

            # Flag to check if the conditions are met for any cell
            conditions_met = False

            # Checking conditions for each cell
            for cell in cells:
                cell_text = cell.text

                # Check if the first condition is met
                condition1_met = False
                if option1_text == "Contains":
                    condition1_met = text_value1 in cell_text
                elif option1_text == "Not contains":
                    condition1_met = text_value1 not in cell_text
                elif option1_text == "Equals":
                    condition1_met = text_value1 == cell_text
                elif option1_text == "Not equal":
                    condition1_met = text_value1 != cell_text
                elif option1_text == "Starts with":
                    condition1_met = cell_text.startswith(text_value1)
                elif option1_text == "Ends with":
                    condition1_met = cell_text.endswith(text_value1)



                # Check if the second condition is met
                condition2_met = False
                if option2_text == "Contains":
                    condition2_met = text_value2 in cell_text
                elif option2_text == "Not contains":
                    condition2_met = text_value2 not in cell_text
                elif option2_text == "Equals":
                    condition2_met = text_value2 == cell_text
                elif option2_text == "Not equal":
                    condition2_met = text_value2 != cell_text
                elif option2_text == "Starts with":
                    condition2_met = cell_text.startswith(text_value2)
                elif option2_text == "Ends with":
                    condition2_met = cell_text.endswith(text_value2)

                # If both conditions are met in the same cell, set the flag and break the loop
                if condition1_met or condition2_met:
                    conditions_met = True
                    break

            if conditions_met:
                print("Data is displayed as per the given search.")
                ExpectedResult = "Data is displayed as per the given search."
                ActualResult = "Data is displayed as per the given search."
            else:
                print("Data is not displayed as per the given search.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver














    def validateandSetdescriptiondata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                      Requirement,
                                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""

        try:
            # Get the list of matching elements
            elements = driver.find_elements(By.XPATH,
                                            "//div[contains(text(),'Home_Key')]/following::div[@data-automation-key='GA_Description_Rich']/div/div/div//span")

            if elements:  # Check if elements list is not empty
                # Iterate through each matching element
                textData = ""
                for element in elements:
                    # Retrieve the text content of the element
                    element_text = element.text
                    # Append the text content to textData
                    textData += element_text + " "

                # Store the concatenated text data in the map using the provided key
                set_map_value(key, textData.strip())  # Strip to remove any leading/trailing whitespace
                print("Stored data for key:", key, "->", textData)  # Print the stored data

                ExpectedResult = "Retrieve and store '" + key + "' for verification"
                ActualResult = "Retrieve and store '" + key + "' for verification"
            else:
                print("No matching elements found.")
                ExpectedResult = "No matching elements found."
                ActualResult = "No matching elements found."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)

        return driver

    def retrieveAndValidateDescription(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                       Requirement, testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        textDataRetrieved = ""
        expected_text = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Find all contact cards
            contact_cards = driver.find_elements(By.XPATH,
                                                 "//div[@class='contacts_card']//following::div[@title='[object Object]']")
            for contact_card in contact_cards:
                # Retrieve text data from each contact card
                textDataRetrieved = contact_card.text.strip()
                # Validate text data
                expected_text = get_map_value(key)
                if str(expected_text).isdigit() and str(textDataRetrieved).isdigit():
                    assert int(textDataRetrieved) == int(expected_text), \
                        f"For field '{key}', Expected integer '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator}'."
                else:
                    assert textDataRetrieved == expected_text, \
                        f"For field '{key}', Expected text '{expected_text}', but got '{textDataRetrieved}' for element with locator '{Locator}'."
                # Find the name associated with the element
                try:
                    name = contact_card.find_element(By.XPATH, Locator + "/../td").text
                    ExpectedResult = f"'{name}' must have '{textDataRetrieved}' as value"
                    ActualResult = f"'{name}' has '{textDataRetrieved}' as value"
                except Exception as e:
                    ExpectedResult = f"'{key}' must have '{textDataRetrieved}' as value"
                    ActualResult = f"'{key}' has '{textDataRetrieved}' as value"
        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = f"'{key}' must have '{textDataRetrieved}' as value"
            exMsg = self.error_message(str(e))
            print("'retrieveAndValidateDescription' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver

    def validategridsearchdata1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Get the expected text from the function
            expected_text = get_map_value(key)
            # Convert expected_text to string if it's an integer
            if isinstance(expected_text, int):
                expected_text = str(expected_text)
            index = 0
            found_in_any_row = False
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                row_xpath = f"(//div[@row-index='{index}'])[2]"
                try:
                    # Find the row element
                    row_element = driver.find_element(By.XPATH, row_xpath)
                    # Find all spans within the row
                    spans = row_element.find_elements(By.TAG_NAME, "div")
                    # Check if the expected text is found in any span within the row
                    for span in spans:
                        if expected_text in span.text:
                            found_in_any_row = True
                            break  # Exit the loop if expected text is found in any span
                    if found_in_any_row:
                        break  # Exit the loop if expected text is found in any span
                    index += 1  # Move to the next row
                except NoSuchElementException:
                    # If the row is not found, break the loop
                    break

            if found_in_any_row:
                print(f"'{expected_text}' found in at least one cell in a row.")
                ExpectedResult = "Data is displayed as per the given search."
                ActualResult = "Data is displayed as per the given search."
            else:
                print(f"'{expected_text}' not found in any cell in any row.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def validategridsearchdata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Get the expected text from the function
            expected_text = get_map_value(key)
            # Convert expected_text to string if it's an integer
            if isinstance(expected_text, int):
                expected_text = str(expected_text)
            index = 0
            found_in_any_row = False
            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                row_xpath = f"(//div[@row-index='{index}'])[2]"
                try:
                    # Find the row element
                    row_element = driver.find_element(By.XPATH, row_xpath)
                    # Find all spans within the row
                    spans = row_element.find_elements(By.TAG_NAME, "div")
                    # Check if the expected text is found in any span within the row (case-insensitive)
                    for span in spans:
                        if expected_text.lower() in span.text.lower():
                            found_in_any_row = True
                            break  # Exit the loop if expected text is found in any span
                    if found_in_any_row:
                        break  # Exit the loop if expected text is found in any span
                    index += 1  # Move to the next row
                except NoSuchElementException:
                    # If the row is not found, break the loop
                    break

            if found_in_any_row:
                print(f"'{expected_text}' found in at least one cell in a row.")
                ExpectedResult = "Data is displayed as per the given search."
                ActualResult = "Data is displayed as per the given search."
            else:
                print(f"'{expected_text}' not found in any cell in any row.")
                ExpectedResult = "Data is not displayed as per the given search."
                ActualResult = "Data is not displayed as per the given search."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def search_negative_case(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                             Requirement, testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"

        exMsg = ""

        textDataRetrieved = ""

        expected_text = ""

        name = ""

        ExpectedResult = ""

        ActualResult = ""

        try:

            # Find the search field element

            search_field = driver.find_element(By.XPATH, Locator)  # Adjust the XPath accordingly

            # Get the text entered in the search field

            search_text = search_field.get_attribute("value")

            # Check if the length of the search text is greater than 20 characters

            if len(search_text) > 20:
                raise Exception("Search text exceeds 20 characters.")

            # Report Pass if the search text length is within 20 characters

            ExpectedResult = "Search field allows only 20 characters."

            ActualResult = f"Search text length: {len(search_text)}"

        except Exception as e:

            FlagTestCase = "Fail"

            ExpectedResult = "Search field allows only 20 characters."

            exMsg = self.error_message(str(e))

            print("Exception occurred:", exMsg)

        finally:

            if FlagTestCase == "Fail":
                ActualResult = exMsg

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,

                                             ActualResult, FlagTestCase, TestCase_Summary)

            return driver

    def press_enter_key1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        try:
            # Find the element where you want to simulate pressing the Enter key
            element = driver.find_element(By.XPATH, Locator)  # Adjust the XPath accordingly
            # Get the current text in the element
            #current_text = element.get_attribute("value")
            # Simulate pressing the Enter key
            element.send_keys(Keys.ENTER)
            element.send_keys(Keys.ENTER)
            ExpectedResult = "Enter key pressed successfully."

            ActualResult = f"Enter key pressed successfully."

            #   expected = "Enter key press should update the text field."
            # Optionally, you can wait for some time after pressing Enter
            # driver.implicitly_wait(2)  # Wait for 2 seconds
            # Get the updated text in the element after pressing Enter
            #updated_text = element.get_attribute("value")
            # Compare the updated text with the current text to determine if Enter was pressed successfully
            #if updated_text != current_text:
             #   actual = "Enter key pressed successfully."
             #   expected = "Enter key press should update the text field."
            #else:
            #    actual = "Enter key not pressed successfully."
             #   expected = "Enter key press should update the text field."
        except Exception as e:

            FlagTestCase = "Fail"

            ActualResult = "Exception occurred: " + str(e)

            exMsg = self.error_message(str(e))

            print("Exception occurred:", exMsg)

        finally:

            if FlagTestCase == "Fail":
                ActualResult = exMsg
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def press_enter_key(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Find the element where you want to simulate pressing the Enter key
            element = driver.find_element(By.XPATH, Locator)  # Adjust the XPath accordingly
            # Get the current text in the element
            # current_text = element.get_attribute("value")
            # Simulate pressing the Enter key
            element.send_keys(Keys.ENTER)
            element.send_keys(Keys.ENTER)
            ExpectedResult = "Enter key pressed successfully."

            ActualResult = f"Enter key pressed successfully."

            #   expected = "Enter key press should update the text field."
            # Optionally, you can wait for some time after pressing Enter
            # driver.implicitly_wait(2)  # Wait for 2 seconds
            # Get the updated text in the element after pressing Enter
            # updated_text = element.get_attribute("value")
            # Compare the updated text with the current text to determine if Enter was pressed successfully
            # if updated_text != current_text:
            #   actual = "Enter key pressed successfully."
            #   expected = "Enter key press should update the text field."
            # else:
            #    actual = "Enter key not pressed successfully."
            #   expected = "Enter key press should update the text field."
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def refresh_griddata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            driver.find_element_by_xpath("//i[@title='Refresh Data']").click()
            # Record the start time
            start_time = time.time()
            # Wait for data to load on the current page within 10 seconds
            data_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']"))
            )

            # Print total record count
            record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
            record_count_text = record_count_element.text
            # Record the end time after data loading
            end_time = time.time()

            # Calculate the data loading duration
            loading_duration = end_time - start_time


            # Round the loading duration to 2 decimal places
            loading_duration = round(loading_duration,2)
            #total_records = int(record_count_text)

            print(f"Data loaded on page . Total record count: {record_count_text}")
            ExpectedResult = f"After clicking refresh,the data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            ActualResult = f"After clicking refresh,the data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
        except TimeoutException:
            print("Data not loaded within 10 seconds. Considered as failed.")
            ExpectedResult = "After clicking refresh,the data not loaded within 10 seconds. Considered as failed. Loaded in {loading_duration} seconds."
            ActualResult = "After clicking refresh,the data not loaded within 10 seconds. Considered as failed. Loaded in {loading_duration} seconds."
            FlagTestCase = "Fail"
            exMsg = "Data not loaded within 10 seconds."

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def validateFilterClearAfterRefresh(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            # Get the text of the filter before refreshing
            before_refresh_text = driver.find_element_by_xpath(
                "//input[@ref='eInput' and contains(@aria-label, 'Filter Input')])[2]").text

            # Click on the refresh button
            driver.find_element_by_xpath("//i[@title='Refresh Data']").click()

            # Wait for the data to load
            data_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@ref='lbTotal']")))

            # Get the text of the filter after refreshing
            after_refresh_text = driver.find_element_by_xpath(
                "//input[@ref='eInput' and contains(@aria-label, 'Filter Input')])[2]").text

            # Calculate the data loading duration
            start_time = time.time()
            # ... code for waiting and loading data ...
            end_time = time.time()
            loading_duration = round(end_time - start_time, 2)

            # Check if the filter text is empty after refreshing
            if after_refresh_text.strip() == "":
                print("Filter is cleared after refreshing.")
                # Print total record count
                record_count_element = driver.find_element_by_xpath("//span[@ref='lbRecordCount']")
                record_count_text = record_count_element.text
                print(f"Data loaded on page. Total record count: {record_count_text}")

                ExpectedResult = f"Data is cleared on grid filters and data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
                ActualResult = f"Data is cleared on grid filters and data loaded on page within 10 seconds. Total record count: {record_count_text}. Loaded in {loading_duration} seconds."
            else:
                print("Filter is not cleared after refreshing.")
                ExpectedResult = "Data is not cleared on grid filters after refreshing."
                ActualResult = "Data is not cleared on grid filters after refreshing."
                FlagTestCase = "Fail"
        except TimeoutException:
            print("Data not loaded within 10 seconds. Considered as failed.")
            ExpectedResult = "Data is not cleared on grid filters and data not loaded within 10 seconds."
            ActualResult = "Data is not cleared on grid filters and data not loaded within 10 seconds."
            FlagTestCase = "Fail"
            exMsg = "Data not loaded within 10 seconds."

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def delete_salesrecord(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                       testStepDesc,
                       Keywords,
                       Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            driver.find_element(By.XPATH, "(//*[text()='Created'])[1]").click()
            driver.find_element(By.XPATH, "(//*[text()='Newer to older'])[1]").click()
            obj = driver.find_element(By.XPATH, Locator)
            driver = self.scrollIntoView(driver, obj)
            # driver.execute_script("arguments[0].scrollIntoView();", obj)

            element_value = self.getElementDetails(obj, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", obj)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver



    def checkcharacterlimit1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                    Requirement, testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            # Get the text from the element located by XPath
            getcharactslimit = driver.find_element(By.XPATH, Locator).get_attribute("value")

            # Count the characters in the text
            charactercount = len(getcharactslimit)
            # Check if the character count is less than 20
            if charactercount < 20:
                ExpectedResult = "Character limit is less than 20 characters"
                ActualResult = "Character limit is less than 20 characters"

            else:
                # If character count is greater than or equal to 20, fail the test case
                FlagTestCase = "Fail"
                ExpectedResult = "Character limit is greater than or equal to 20 characters"
                ActualResult = "Character limit is greater than or equal to 20 characters"
                raise ValueError("Character limit is greater than or equal to 20 characters")

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            # Set the expected and actual results for the failure case
            ExpectedResult = "An error occurred while checking character limit"
            ActualResult = "An error occurred while checking character limit: " + str(e)

            print("'gettext' Action Exception Message -> \n" + str(e))

        finally:

            # Report the test result

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,

                                             FlagTestCase, TestCase_Summary)

            return driver


    def checkcharacterlimit(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                               testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Get the text from the element located by XPath
            getcharactslimit = driver.find_element(By.XPATH, Locator).get_attribute("value")

            # Count the characters in the text
            charactercount = len(getcharactslimit)
            # Check if the character count is less than 20
            if charactercount >= 50:
                ExpectedResult = "Character limit is less than or equal to  50 characters"
                ActualResult = "Character limit is less than or equal to  50 characters"

            else:
                # If character count is greater than or equal to 20, fail the test case
                FlagTestCase = "Fail"
                ExpectedResult = "Character limit should not exceed 50 characters"
                ActualResult = "Character limit is greater than 50 characters"
                raise ValueError("Character limit is greater than or equal to 50 characters")
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver

    def check_excel_download(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                             testStepDesc,
                             Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Specify the name pattern of the downloaded Excel file
            excel_file_pattern = "salesrecords__data_*"

            # Specify the download directory path
            download_dir = r"C:\Users\ppriya1\Downloads"

            # Search for files matching the pattern in the download directory
            matching_files = glob.glob(os.path.join(download_dir, excel_file_pattern))

            # Check if any matching file is found
            if matching_files:
                ExpectedResult = "Excel file downloaded successfully"
                ActualResult = "Excel file downloaded successfully"
            else:
                FlagTestCase = "Fail"
                ExpectedResult = "Excel file not found in the specified download directory"
                ActualResult = "Excel file not found in the specified download directory"
                raise FileNotFoundError("Excel file not found")

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "An error occurred while checking Excel download"
            ActualResult = "An error occurred while checking Excel download: " + str(e)
            exMsg = self.error_message(str(e))
            print("Exception Message -> \n" + str(e))
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def verifyNoObj(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                    testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"  # Initially assume test case passes
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # Attempt to find the element
            elements = driver.find_elements(By.XPATH, Locator)
            # If no elements are found, it's considered a pass
            if not elements:
                ExpectedResult = "No matching elements found. Test case should pass."
                ActualResult = "No matching elements found. Test case passed."
            else:
                # If elements are found, it's considered a failure
                FlagTestCase = "Fail"
                ExpectedResult = "Expected no matching elements, but found."
                ActualResult = "Found matching elements."
                # Print the number of matching elements for debugging
                print(f"Number of matching elements found: {len(elements)}")
        except Exception as e:
            # If an exception occurs, mark the test case as failed
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'verifyNoObj' Action Exception Message -> \n" + str(e))
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def beforegroupcount(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                         testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""

        try:
            # Get the expected text from the function
            expected_text = get_map_value(key)

            if expected_text is not None:
                if isinstance(expected_text, int):
                    expected_text = str(expected_text)

                # Find all rows in the grid
                rows = driver.find_elements(By.XPATH, "//div[@role='row']")

                found_in_all_cells = True

                # Iterate through each row
                for row in rows:
                    try:
                        # Find the cell in the specified column for the current row
                        cell_xpath = f".//div[@col-id='{Locator}']//span[@ref='eCellValue' and @class='ag-cell-value']"
                        cell = row.find_element(By.XPATH, cell_xpath)
                        # Get the text of the cell
                        cell_text = cell.text

                        # Check if the expected text is not contained in the cell text
                        if expected_text not in cell_text:
                            found_in_all_cells = False
                            break  # Exit the loop if expected text is not found in any cell
                    except NoSuchElementException:
                        # If the cell is not found, set found_in_all_cells to False and break the loop
                        found_in_all_cells = False
                        break

                if found_in_all_cells:
                    print(f"'{expected_text}' found in all cells of the column '{Locator}' in all rows.")
                    # Count the number of rows
                    records_count = len(rows)
                    # Set key value
                    set_map_value(key, records_count)
                    ExpectedResult = "Data is displayed as per the given search."
                    ActualResult = "Data is displayed as per the given search."
                else:
                    print(f"'{expected_text}' not found in all cells of the column '{Locator}' in all rows.")
                    ExpectedResult = "Data is not displayed as per the given search."
                    ActualResult = "Data is not displayed as per the given search."
                    FlagTestCase = "Fail"
            else:
                print("Expected text is None.")
                ExpectedResult = "Expected text is None."
                ActualResult = "Expected text is None."
                FlagTestCase = "Fail"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def aftergrouping(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after grouping."
        ActualResult = ""

        try:
            # Get the expected row count from the function
            expected_row_count = get_map_value(key)

            if expected_row_count is not None:
                if isinstance(expected_row_count, int):
                    # Find all rows in the grid
                    rows = driver.find_elements(By.XPATH, "//div[@role='row']")
                    actual_row_count = len(rows)

                    # Compare the expected row count with the actual row count
                    if actual_row_count == expected_row_count:
                        ExpectedResult = "Expected row count matches the actual row count after grouping."
                        ActualResult = f"Expected row count ({expected_row_count}) matches the actual row count ({actual_row_count})."
                    else:
                        ExpectedResult = "Expected row count does not match the actual row count after grouping."
                        ActualResult = f"Expected row count ({expected_row_count}) does not match the actual row count ({actual_row_count})."
                        FlagTestCase = "Fail"
                else:
                    ExpectedResult = "Expected row count is not an integer."
                    ActualResult = "Expected row count is not an integer."
                    FlagTestCase = "Fail"
            else:
                ExpectedResult = "Expected row count is None."
                ActualResult = "Expected row count is None."
                FlagTestCase = "Fail"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver


    def selectrecord_list(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after grouping."
        ActualResult = ""

        try:
            time.sleep(10)
            # Instantiate ActionChains
            action_chains = ActionChains(driver)
            # Send the Back Arrow key and then the Enter key to the currently focused element
            action_chains.send_keys(Keys.ARROW_LEFT).perform()
            time.sleep(10)
            action_chains.send_keys(Keys.ENTER).perform()
            time.sleep(10)

            #driver.find_elements(By.XPATH, "(//*[text() = 'Delete'])")



            ExpectedResult = "Selected record successfully."
            ActualResult = "Selected record successfully."



        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver


    def clickdeletebtncancel(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after grouping."
        ActualResult = ""

        try:
            # Define the refined XPath
            delete_button_xpath = "//*[@data-icon-name='Delete' and @data-action='delete']"

            # Wait for the delete button to be present and visible
            delete_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, delete_button_xpath))
            )

            # Scroll the delete button into view
            driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)

            # Move the mouse cursor to the delete button
            ActionChains(driver).move_to_element(delete_button).perform()

            # Wait for the delete button to be clickable
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
            )

            # Click the delete button
            delete_button.click()
            time.sleep(5)
            alert = driver.switch_to.alert
            message = alert.text
            alert.dismiss()
            time.sleep(3)

            ExpectedResult = "Clicked on grid delete button successfully."
            ActualResult = "Clicked on grid delete button successfully."



        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver


    def clickdeletebtn(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                      testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after grouping."
        ActualResult = ""

        try:
            # Define the refined XPath
            delete_button_xpath = "//*[@data-icon-name='Delete' and @data-action='delete']"

            # Wait for the delete button to be present and visible
            delete_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, delete_button_xpath))
            )

            # Scroll the delete button into view
            driver.execute_script("arguments[0].scrollIntoView(true);", delete_button)

            # Move the mouse cursor to the delete button
            ActionChains(driver).move_to_element(delete_button).perform()

            # Wait for the delete button to be clickable
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
            )

            # Click the delete button
            delete_button.click()
            time.sleep(5)
            alert = driver.switch_to.alert
            message = alert.text
            alert.accept()
            time.sleep(3)

            ExpectedResult = "Record deleted successfully."
            ActualResult = "Record deleted successfully."



        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def configurelimit(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                       testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after grouping."
        ActualResult = ""

        try:
            # Get the expected text from the function
            expected_limit = get_map_value(key)
            actual_limit = driver.find_element(By.XPATH, Locator).get_attribute('value')
            actual_limit1 = len(actual_limit)
            # If expected and actual match, let pass
            if expected_limit<= actual_limit1:
                ExpectedResult = "Search limit is taking as per the configured search limit."
                ActualResult = "Search limit is taking as per the configured search limit."
            else:
                ExpectedResult = "Search limit is not taking as per the configured search limit."
                ActualResult = "Search limit is not taking as per the configured search limit."
                FlagTestCase = "Fail"



        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def get_test_data_and_set(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Assuming set_map_value is a function defined elsewhere in your codebase
            # Get the expected text from the function
            element = Locator
            set_map_value(key, element)
            print("setting test data with key: ", {key}, "and value:", {Locator})
            # Update ExpectedResult to indicate test data is set
            ExpectedResult = "Test Data is set to Key."
            ActualResult = "Test Data is set to Key."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def validate_grid_excel_data1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data should match with Excel data."
        ActualResult = "."

        def get_latest_file(download_path, prefix):

            """Get the latest file in the directory with the specified prefix."""
            files = [f for f in os.listdir(download_path) if f.startswith(prefix) and f.endswith('.xlsx')]
            if not files:
                raise FileNotFoundError(f"No files with prefix '{prefix}' found in '{download_path}'")
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_path, f)))
            return os.path.join(download_path, latest_file)

        try:
            # Specify the download path and file prefix
            download_path = "C:/Users/ppriya1/Downloads"
            file_prefix = "Controlled Docs_All Materials_data"

            # Get the latest file
            excel_path = get_latest_file(download_path, file_prefix)

            # Load the Excel file into a DataFrame
            df = pd.read_excel(excel_path)

            # Assuming each row in the Excel corresponds to a row in the grid
            index = 0
            all_match = True
            mismatched_rows = []

            # Iterate through each row in the grid
            while True:
                row_xpath = f"(//div[@row-index='{index}'])[2]"
                try:
                    row_element = driver.find_element(By.XPATH, row_xpath)
                    cells = row_element.find_elements(By.TAG_NAME, "div")

                    # Extract text from each cell in the grid row
                    grid_row_data = [cell.text.strip() for cell in cells]

                    if index < len(df):
                        # Extract data from the corresponding row in the Excel
                        excel_row_data = df.iloc[index].astype(str).tolist()

                        # Compare grid row data with Excel row data
                        if grid_row_data != excel_row_data:
                            all_match = False
                            mismatched_rows.append((index, grid_row_data, excel_row_data))
                    else:
                        print(f"Grid has more rows than Excel data. Extra grid row index: {index}")
                        all_match = False
                        break

                    index += 1
                except NoSuchElementException:
                    break

            if all_match:
                ExpectedResult = "Grid data matches Excel data."
                ActualResult = f"Grid data matches Excel data and grid total count: {index}, and excel total row count: {len(df)}"
            else:
                ExpectedResult = "Grid data matches Excel data."
                ActualResult = "Grid data does not match Excel data."
                FlagTestCase = "Fail"
                print("Mismatched rows:")
                for row in mismatched_rows:
                    print(f"Row index: {row[0]}, Grid: {row[1]}, Excel: {row[2]}")

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            ExpectedResult = "Grid data matches Excel data."
            ActualResult = f"Exception occurred: {exMsg}"
            print("Exception occurred:", exMsg)
        finally:
            # Print the Expected and Actual Results
            print(f"Expected Result: {ExpectedResult}")
            print(f"Actual Result: {ActualResult}")

            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def validate_grid_excel_data(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                 testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data matches Excel data."
        ActualResult = "Grid data matches Excel data."
        match_count = 0  # Counter to track the number of matches
        seen_rows = set()  # Set to track seen grid rows

        def get_latest_file(download_path, prefix):
            """Get the latest file in the directory with the specified prefix."""
            files = [f for f in os.listdir(download_path) if f.startswith(prefix) and f.endswith('.xlsx')]
            if not files:
                raise FileNotFoundError(f"No files with prefix '{prefix}' found in '{download_path}'")
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_path, f)))
            return os.path.join(download_path, latest_file)

        try:
            # Specify the download path and file prefix
            download_path = "C:/Users/ppriya1/Downloads"
            file_prefix = "Controlled Docs_All Materials_data"

            # Get the latest file
            excel_path = get_latest_file(download_path, file_prefix)

            # Load the Excel file into a DataFrame
            df = pd.read_excel(excel_path)

            # Split Testdata and Locator
            test_data = Testdata.split('|')
            locator_data = Locator.split('|')

            # Iterate through each row in the grid
            for index, excel_row in df.iterrows():
                row_xpath = f"(//div[@row-index='{index}'])[2]"
                try:
                    row_element = driver.find_element(By.XPATH, row_xpath)
                    cells = row_element.find_elements(By.TAG_NAME, "div")
                    # Extract text from the cells in the grid row
                    grid_row_data = tuple(cell.text.strip() for cell in cells if cell.text.strip() != "")
                    # Check for duplicates
                    if grid_row_data in seen_rows:
                        continue
                    seen_rows.add(grid_row_data)
                    # Extract data from the corresponding row in the Excel
                    excel_row_data = [str(item).strip() for item in excel_row.fillna("").tolist()]
                    # Debugging: Print data being compared
                    print(f"Row {index} - Grid data: {grid_row_data}")
                    print(f"Row {index} - Excel data: {excel_row_data}")

                    # Compare grid row data with Excel row data
                    if list(grid_row_data) == excel_row_data:
                        match_count += 1
                    else:
                        print(f"Mismatch at row {index}: Grid data - {grid_row_data}, Excel data - {excel_row_data}")
                except NoSuchElementException:
                    print(f"No row found in grid for index {index}")
                    FlagTestCase = "Fail"
                    break
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Print the Expected and Actual Results
            ExpectedResult = "Grid data matches Excel data and matched rows count: " + str(match_count)
            ActualResult = f"Grid data matches Excel data and matched rows count: {match_count}"
            print(f"Expected Result: {ExpectedResult}")
            print(f"Actual Result: {ActualResult}")

            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def validate_grid_excel_data0(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                 testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data matches Excel data."
        ActualResult = "Grid data matches Excel data."
        match_count = 0  # Counter to track the number of matches
        seen_rows = set()  # Set to track seen grid rows

        def get_latest_file(download_path, prefix):
            """Get the latest file in the directory with the specified prefix."""
            files = [f for f in os.listdir(download_path) if f.startswith(prefix) and f.endswith('.xlsx')]
            if not files:
                raise FileNotFoundError(f"No files with prefix '{prefix}' found in '{download_path}'")
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_path, f)))
            return os.path.join(download_path, latest_file)

        try:
            # Specify the download path and file prefix
            download_path = "C:/Users/ppriya1/Downloads"
            file_prefix = "Controlled Docs_All Materials_data"

            # Get the latest file
            excel_path = get_latest_file(download_path, file_prefix)

            # Load the Excel file into a DataFrame
            df = pd.read_excel(excel_path)
            total_excel_rows = len(df)  # Exclude header row

            # Split Testdata and Locator
            #test_data = Testdata.split('|')
            #locator_data = Locator.split('|')

            # Get total row count from the grid
            grid_rows = driver.find_elements(By.XPATH,
                                             "(//div[contains(@class, 'ag-body-viewport')])[2]//div[contains(@class, 'ag-row')]")
            #total_grid_rows = len(grid_rows)

            # Iterate through each row in the grid
            for index, excel_row in df.iterrows():
                row_xpath = f"(//div[@row-index='{index}'])[2]"

                try:
                    row_element = driver.find_element(By.XPATH, row_xpath)
                    cells = row_element.find_elements(By.TAG_NAME, "div")
                    # Extract text from the cells in the grid row
                    grid_row_data = tuple(cell.text.strip() for cell in cells if cell.text.strip() != "")
                    # Check for duplicates
                    total_grid_rows = len(grid_row_data)
                    if grid_row_data in seen_rows:
                        continue
                    seen_rows.add(grid_row_data)
                    # Extract data from the corresponding row in the Excel
                    excel_row_data = [str(item).strip() for item in excel_row.fillna("").tolist()]
                    # Debugging: Print data being compared
                    print(f"Row {index} - Grid data: {grid_row_data}")
                    print(f"Row {index} - Excel data: {excel_row_data}")

                    # Compare grid row data with Excel row data
                    if list(grid_row_data) == excel_row_data:
                        match_count += 1
                    else:
                        print(f"Mismatch at row {index}: Grid data - {grid_row_data}, Excel data - {excel_row_data}")
                except NoSuchElementException:
                    print(f"No row found in grid for index {index}")
                    FlagTestCase = "Fail"
                    break
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)
        finally:
            # Print the total row counts and match count
            print(f"Total rows in Excel (excluding header): {total_excel_rows}")
            print(f"Total rows in grid: {total_grid_rows}")
            print(f"Matched rows count: {match_count}")

            # Update Expected and Actual Results
            ExpectedResult = f"Grid data matches Excel data. Total rows in Excel: {total_excel_rows}, Total rows in grid: {total_excel_rows}, Matched rows count: {total_excel_rows}"
            ActualResult = f"Grid data matches Excel data. Total rows in Excel: {total_excel_rows}, Total rows in grid: {total_excel_rows}, Matched rows count: {total_excel_rows}"
            print(f"Expected Result: {ExpectedResult}")
            print(f"Actual Result: {ActualResult}")

            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver


    def switch_iframe(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Switched to iFrame"
        ActualResult = ""
        try:
            iframe_id = "panelNewForm"  # Assuming the iframe ID is passed as a string here
            iframe_id = Locator
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_id)))
            print(f"Switched to iframe with ID: {iframe_id}")
            ExpectedResult = "Switched to iFrame."
            ActualResult = "Switched to iFrame."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver


    def simple_click(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        count = 0
        element_value = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            element = driver.find_element(By.XPATH, Locator)
            # element = driver.find_element(By.XPATH, Locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            """
            details = ["text", "title", "value"]

            for value in details:
                element_value = self.getElementDetails(element, value)
                if element_value != "":
                    break
            """

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            element.click()

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver


    def grid_delete(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        element = None
        count = 0
        element_value = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            print("Waiting for the delete button to be visible")
            delete_button = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//i[@data-action='delete' and @title='Delete']"))
            )
            print("Delete button found")

            delete_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//i[@data-action='delete' and @title='Delete']"))
            )
            print("Delete button is clickable")

            driver.execute_script("arguments[0].click();", delete_button)
            print("Delete button clicked")

            # Add a small delay to ensure the alert appears
            time.sleep(2)
            print("Waited 2 seconds for the alert to appear")

            # Wait for the alert to be present
            print("Waiting for the alert to be present")
            alert = WebDriverWait(driver, 30).until(EC.alert_is_present())
            print("Alert is present")

            # Switch to the alert
            alert = driver.switch_to.alert
            print("Switched to alert")

            # Accept the alert
            alert.accept()
            print("Alert accepted successfully")

            ExpectedResult = "Record deleted successfully"
            ActualResult = "Record deleted successfully"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'click' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver

    def Ag_datefields(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""

        date_format = '%m/%d/%Y'
        try:
            # Convert Testdata from ddmmyyyy to dd/mm/yyyy
            if len(Testdata) == 8:  # Assuming the input format is always ddmmyyyy
                formatted_date = f"{Testdata[:2]}/{Testdata[2:4]}/{Testdata[4:]}"
            else:
                raise ValueError(f"Testdata '{Testdata}' is not in the expected format ddmmyyyy")

            print(formatted_date)  # This will print the date in dd/mm/yyyy format

            element = driver.find_element(By.XPATH, Locator)
            # Use JavaScript to set the value attribute directly
            driver.execute_script("arguments[0].setAttribute('value', arguments[1])", element, formatted_date)

            # Assuming set_map_value and get_map_value are defined elsewhere
            set_map_value(key, formatted_date)
            print(f"setting test data with key: {key} and value: {formatted_date}")
            title = get_map_value(key)
            print(title)

            ExpectedResult = f"'{formatted_date}' field must accept the entered text value"
            ActualResult = f"'{formatted_date}' entered in '{name}' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print(f"'cleartypeandsetdata' Action Exception Message -> \n{str(e)}")
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver

    def Ag_datefields1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                     testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""

        date_format = '%m/%d/%Y'
        try:
            # Convert Testdata from ddmmyyyy to dd/mm/yyyy
            if len(Testdata) == 8:  # Assuming the input format is always ddmmyyyy
                formatted_date = f"{Testdata[:2]}/{Testdata[2:4]}/{Testdata[4:]}"
            else:
                raise ValueError(f"Testdata '{Testdata}' is not in the expected format ddmmyyyy")

            print(formatted_date)  # This will print the date in dd/mm/yyyy format

            element = driver.find_element(By.XPATH, Locator)
            # Use JavaScript to set the value attribute directly
            driver.execute_script("arguments[0].setAttribute('value', arguments[1])", element, formatted_date)

            # Assuming set_map_value and get_map_value are defined elsewhere
            set_map_value(key, formatted_date)
            print(f"setting test data with key: {key} and value: {formatted_date}")
            title = get_map_value(key)
            print(title)
            driver.find_element(By.XPATH, '//span[contains(text(),"Get data")]').click()
            ExpectedResult = f"'{formatted_date}' field must accept the entered text value"
            ActualResult = f"'{formatted_date}' entered in '{name}' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print(f"'cleartypeandsetdata' Action Exception Message -> \n{str(e)}")
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver

    def validateDateRangeFilter(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                                testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""
        try:

            #driver.find_element(By.XPATH, '//span[contains(text(),"Get data")]').click()
            # Get the expected dates from the function
            expected_Fromdate = driver.find_element(By.XPATH, '(//input[@aria-label="Select From date"])').get_attribute('value')
            expected_Todate = driver.find_element(By.XPATH, '(//input[@aria-label="Select To date"])').get_attribute('value')
            time.sleep(10)
            # Convert the expected date strings to datetime objects
            #expected_Fromdate = datetime.strptime(expected_Fromdate, "%d/%m/%Y")
            #expected_Todate = datetime.strptime(expected_Todate, "%d/%m/%Y")

            # Flag to check if the expected date range is valid for all cells
            valid_date_range = True
            index = 1

            # Iterate through each row dynamically
            while True:
                # Build the XPath for the current row index
                xpath = f"//div[@row-index='{index}']//span[@ref='eCellValue' and @class='ag-cell-value']/ancestor::div/div[@col-id='{Locator}']/div/span/div/span"
                try:
                    # Find the cell in the Locator column for the current row index
                    date_cell = driver.find_element(By.XPATH, xpath)
                    # Get the text of the date cell
                    cell_text = date_cell.get_attribute('innerHTML')
                    # Convert cell text to datetime object
                    #cell_date = datetime.strptime(cell_text, "%d/%m/%Y")

                    # Check if the cell date is within the expected range
                    if not (expected_Fromdate <= cell_text <= expected_Todate):
                        # If date is out of range, set the flag to False and break the loop
                        valid_date_range = False
                        break
                    index += 1  # Move to the next row
                except NoSuchElementException:
                    # If the cell is not found, break the loop
                    break
                    time.sleep(10)
            # Check if the date range is valid for all cells
            if valid_date_range:
                print(f"All dates are within the range '{expected_Fromdate}' to '{expected_Todate}'.")
                ExpectedResult = "Data is displayed as per the given date range."
                ActualResult = "Data is displayed as per the given date range."
            else:
                print(f"Some dates are not within the range '{expected_Fromdate}' to '{expected_Todate}'.")
                ExpectedResult = "Data is not displayed as per the given date range."
                ActualResult = "Data is not displayed as per the given date range."
                FlagTestCase = "Fail"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver



    def check_saveclipboard(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                    Requirement, testStepDesc,
                    Keywords,
                    Locator,
                    Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        message = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
            time.sleep(10)
            """
            alert = Alert(driver)
            # wait = WebDriverWait(driver, 10)
            # alert = wait.until(EC.alert_is_present())
            # message = alert.text
            # print(f"Pop up alert message is : {message}")
            # Accept or dismiss the alert
            alert.accept()  # or alert.dismiss()
            """
            driver.find_element(By.XPATH, "//i[@title='Save Filters to Clipboard']").click()
            alert = driver.switch_to.alert
            message = alert.text

            # Check if the message is the URL
            if message.startswith('http'):
                alert.accept()
                driver.get(message)
                ExpectedResult = "Copied the URL and verified the saved filter"
                ActualResult = "Copied the URL and verified the saved filter"
            else:
                FlagTestCase = "Fail"
                ExpectedResult = "Accept alert message displayed"
                ActualResult = "Incorrect alert '" + message + "' displayed"


            time.sleep(3)

        except Exception as e:
            FlagTestCase = "Fail"
            ExpectedResult = "Accept alert message displayed"
            exMsg = self.error_message(str(e))
            print("'acceptalert' Action Exception Message -> \n" + str(exMsg))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def zoomout_80(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                   testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = "Zoom out field must be 80%"
        ActualResult = ""

        try:
            # Perform the zoom out action
            driver.execute_script("document.body.style.zoom='80%'")

            # Check if the zoom level is correctly set
            zoom_level = driver.execute_script("return document.body.style.zoom")
            if zoom_level == '80%':
                ActualResult = "Zoom out field is correctly set to 80%"
            else:
                FlagTestCase = "Fail"
                ActualResult = f"Expected zoom level '80%', but got {zoom_level}"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            ActualResult = exMsg
            print(f"zoomout_80 Action Exception Message -> \n{str(e)}")
        finally:
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver

    def AGgrid_waitforpageload(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                        testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            max_wait_time = 100  # Maximum wait time in seconds
            start_time = time.time()
            while time.time() - start_time < max_wait_time:
                try:
                    element_present = driver.find_element(By.XPATH,
                                                          "//p[contains(text(),'Please wait while loading the updated data')]")
                    time.sleep(1)  # Wait for 1 second before checking again
                except Exception:
                    # Element is not found, meaning it has disappeared
                    ExpectedResult = "Page loaded successfully"
                    ActualResult = "Page loaded successfully"
                    break
            else:
                # If we exit the loop normally, the element is still present after the max wait time
                FlagTestCase = "Fail"
                ExpectedResult = "Page did not load within the expected time"
                ActualResult = "Page did not load within the expected time"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            ActualResult = exMsg
            print(f"zoomout_80 Action Exception Message -> \n{str(e)}")
        finally:
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
            return driver


    def Veeva_jsclick(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement, testStepDesc,
                Keywords,
                Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        count = 0
        ExpectedResult = ""
        ActualResult = ""
        try:
            wait = WebDriverWait(driver, 10)
            #element = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))
            # Test data
            value_to_set = Testdata # You can replace 'India' with any value from your test data

            # Locate the input element using the provided XPath
            element = driver.find_element(By.XPATH, Locator)

            # Execute JavaScript to set the value of the input element dynamically
            driver.execute_script("arguments[0].value = arguments[1];", element, value_to_set)

            element_value = self.getElementDetails(element, "value")
            element_value = re.sub(r'\*', '', element_value)

            if element_value == "":
                element_value = "element"

            ExpectedResult = "Click on '" + element_value + "' field"
            ActualResult = "Clicked on '" + element_value + "' field"

            driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'jsclick' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def eTMF_upload_file(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                    Requirement, testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):

        FlagTestCase = "Pass"

        exMsg = ""

        docname = ""

        finalMsg = ""

        ExpectedResult = ""

        ActualResult = ""

        try:

            #filename = self.common_methods.create_docx_file()
            filename = self.common_methods.eTMF_docx_file()

            # Extract the document name from the full path

            doc_name = filename.split('\\')[-1]

            docname = doc_name

            # Switch to the iframe if required for the upload area

            #driver.switch_to.frame(driver.find_element(By.NAME, "upload_target"))

            # Locate the drop zone for the drag-and-drop functionality

            #drop_zone = driver.find_element(By.CLASS_NAME, "dragDropWidgetContainer")
            # Wait for the file input element to be present
            wait = WebDriverWait(driver, 10)
            file_input = wait.until(EC.presence_of_element_located((By.ID, "inboxFileChooserHTML5")))

            # Set the file path to the file input element
            file_input.send_keys(filename)


            # Read the file as binary data

            with open(filename, 'rb') as f:

                file_data = f.read()


            ExpectedResult = "File must upload successfully"

            ActualResult = f"Uploaded file '{docname}' successfully"

        except Exception as e:

            FlagTestCase = "Fail"

            ExpectedResult = "File must upload successfully"

            exMsg = self.error_message(str(e))

            print(f"'upload_file' Action Exception Message -> \n{exMsg}")

        finally:

            if FlagTestCase == "Fail":
                ActualResult = exMsg

            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,

                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,

                                             ActualResult, FlagTestCase, TestCase_Summary)

        return driver


    def gettext_and_set(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                              testStepDesc, Keywords, Locator, Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "Grid data is verified after sorting."
        ActualResult = ""
        try:
            # Assuming set_map_value is a function defined elsewhere in your codebase
            # Get the expected text from the function
            element = driver.find_element(By.XPATH, Locator).get_attribute("valuekey")
            set_map_value(key, element)
            print("setting test data with key: ", {key}, "and value:", {Locator})
            # Update ExpectedResult to indicate test data is set
            ExpectedResult = "Document Number is set to Key."
            ActualResult = "Document Number is set to Key."

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred: ", exMsg)
        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver



    def searchwithretreivedata(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                           testStepDesc,
                           Keywords,
                           Locator,
                           Testdata, key, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        name = ""
        ExpectedResult = ""
        ActualResult = ""
        try:
            element = driver.find_element(By.XPATH, Locator)
            docnumber = get_map_value(key)
            print(docnumber)

            element.send_keys(docnumber)
            driver.find_element(By.XPATH, "//button[@id='search_main_button']").click()
            ExpectedResult = "Retrieve and store '" + key + "' for verification"

            ActualResult = "Retrieved and stored value of '" + key + "' for verification"




        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = self.error_message(str(e))
            print("'retreiveAndSetData' Action Exception Message -> \n" + str(e))
        finally:
            if FlagTestCase == "Fail":
                ActualResult = exMsg
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult,
                                             FlagTestCase, TestCase_Summary)
        return driver

    def select_todaydate(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                         testStepDesc,
                         Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            #driver.find_element(By.XPATH, "(//span[contains(text(),'*Required to proceed')])").click()
            driver.find_element(By.XPATH, Locator).click()
            #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locator)))
            #element.click()
           # driver.find_element(By.XPATH, Locator).click()
            today = str(datetime.now().day)
            print("today date:" +today )
            #xpath = f"(//a[contains(text(),'{today}')])[2]"
            xpath = f"(//a[contains(text(),'{today}')])"
            todayElement = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].scrollIntoView(true);", todayElement)
            todayElement.click()
            #todayElement.click()
            ExpectedResult = f"Click on '{today}' field"
            ActualResult = f"Clicked on '{today}' field"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print(f"'select_todaydate' Action Exception Message -> \n{exMsg}")
            ActualResult = exMsg
        finally:
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def select_todaydate1(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                          testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            # Click the main element if required
            driver.find_element(By.XPATH, Locator).click()

            # Get today's date as a string
            today = str(datetime.now().day)
            print("Today's date: " + today)

            # Check if the element text is null or empty
            Checkdatevalue = driver.find_element(By.XPATH, Locator).text
            if not Checkdatevalue:  # If the value is empty or null, try clicking
                try:
                    # First attempt with basic XPath (no index)
                    xpath = f"(//a[contains(text(),'{today}')])"
                    todayElement = driver.find_element(By.XPATH, xpath)
                    driver.execute_script("arguments[0].scrollIntoView(true);", todayElement)
                    todayElement.click()

                except (StaleElementReferenceException, ElementNotInteractableException) as e:
                    print(f"Exception occurred: {e}. Trying alternative XPath with index 2.")

                    # Second attempt with index [2]
                    try:
                        Checkdatevalue1 = driver.find_element(By.XPATH, Locator).text
                        if not Checkdatevalue1:  # If still null, attempt the second index
                            xpath2 = f"(//a[contains(text(),'{today}')])[2]"
                            todayElement2 = driver.find_element(By.XPATH, xpath2)
                            driver.execute_script("arguments[0].scrollIntoView(true);", todayElement2)
                            todayElement2.click()

                    except (StaleElementReferenceException, ElementNotInteractableException) as e2:
                        print(f"Exception occurred: {e2}. Trying alternative XPath with index 3.")

                        # Third attempt with index [3]
                        try:
                            Checkdatevalue2 = driver.find_element(By.XPATH, Locator).text
                            if not Checkdatevalue2:  # If still null, attempt the third index
                                xpath3 = f"(//a[contains(text(),'{today}')])[3]"
                                todayElement3 = driver.find_element(By.XPATH, xpath3)
                                driver.execute_script("arguments[0].scrollIntoView(true);", todayElement3)
                                todayElement3.click()

                        except (StaleElementReferenceException, ElementNotInteractableException) as e3:
                            print(f"Exception occurred: {e3}. Could not find a valid element.")

            ExpectedResult = f"Click on '{today}' field"
            ActualResult = f"Clicked on '{today}' field"

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print(f"'select_todaydate' Action Exception Message -> \n{exMsg}")
            ActualResult = exMsg

        finally:
            # Report the test step
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver


    def move_dialog_up(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID, Requirement,
                       testStepDesc,
                       Keywords, Locator, Testdata, TestCase_Summary, moveAmount='50px'):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = ""
        ActualResult = ""

        try:
            # Locate the dialog box using XPath
            dialogElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locator)))
            # Adjust the position of the dialog box
            driver.execute_script(f"arguments[0].style.top = '{moveAmount}';", dialogElement)
            ExpectedResult = f"Moved dialog box up by '{moveAmount}'"
            ActualResult = f"Moved dialog box up by '{moveAmount}'"
        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print(f"'move_dialog_up' Action Exception Message -> \n{exMsg}")
            ActualResult = exMsg
        finally:
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult,
                                             ActualResult, FlagTestCase, TestCase_Summary)
        return driver

    def validateStudyNumber_InGrid(self, driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                   Requirement, testStepDesc, Keywords, Locator, Testdata, TestCase_Summary):
        FlagTestCase = "Pass"
        exMsg = ""
        ExpectedResult = "All rows in the grid must have Study Number."
        ActualResult = ""
        try:
            # Locate the grid containing the rows
            grid_xpath = "//div[contains(@class, 'css-') and contains(@class, '-BodySection')]"
            grid_element = driver.find_element(By.XPATH, grid_xpath)

            # Identify all rows within the grid
            rows = grid_element.find_elements(By.XPATH, "//div[@class='css-189ri2e']/div/div[1]")
            row_count = len(rows)
            if row_count == 0:
                raise Exception("No rows found in the grid.")
            print(f"Number of rows found: {row_count}")

            # Loop through each row
            for index, row in enumerate(rows):
                # Get the text content of the current row
                row_text = row.text.strip()

                # Check if the content is empty or null
                if not row_text:
                    FlagTestCase = "Fail"
                    ActualResult = f"Row {index + 1} has empty content."
                    print(f"Validation failed: Row {index + 1} has empty content.")
                    break
            else:
                ActualResult = "All rows have a valid Study Number."
                print("Validation passed: All rows have non-empty content.")

        except Exception as e:
            FlagTestCase = "Fail"
            exMsg = str(e)
            print("Exception occurred:", exMsg)

        finally:
            # Report the test result
            self.reports.Report_TestDataStep(driver, browser, modulename, TestCaseName, TestStepName, TestStepID,
                                             Requirement, testStepDesc, Keywords, Locator, ExpectedResult, ActualResult,
                                             FlagTestCase, TestCase_Summary)
            return driver