import pytest
from src.actions.actions import Actions

# Instantiate singleton
action = Actions()


import os
from openpyxl import load_workbook
from src.Utilities.CommonMethods import commonMethods

def get_test_data_from_excel():
    test_data = []

    rootpath = commonMethods.get_project_root(None)
    datapath = os.path.join(rootpath, "Data", "CTKMS_R1_TestData.xlsx")
    workbook = load_workbook(datapath)

    testBrowsers = workbook["TestBrowsers"]
    testModules = workbook["TestModules"]
    testCases = workbook["TestCases"]

    for browser_row in testBrowsers.iter_rows(min_row=2, values_only=True):
        browser_name, browser_run = browser_row[:2]
        if browser_run != 'Y':
            continue

        for module_row in testModules.iter_rows(min_row=2, values_only=True):
            main_module, modulename, module_description, module_run = module_row[:4]
            if module_run != 'Y':
                continue

            for test_case_row in testCases.iter_rows(min_row=2, values_only=True):
                TestCaseName, TestCaseDescription, Run = test_case_row[:3]
                if modulename not in TestCaseName or Run != 'Y':
                    continue

                testStepSheet = workbook[main_module]
                for step_row in testStepSheet.iter_rows(min_row=2, values_only=True):
                    if TestCaseName not in step_row[0] or step_row[4] != 'Y':
                        continue

                    step_data = {
                        "browser": browser_name,
                        "modulename": modulename,
                        "TestCaseName": TestCaseName,
                        "TestCaseDescription": TestCaseDescription,
                        "TestStepName": step_row[0],
                        "TestStepID": step_row[1],
                        "Requirement": step_row[2],
                        "Description": step_row[3],
                        "Keywords": step_row[5],
                        "Locator": step_row[6],
                        "Testdata": step_row[7],
                        "index": step_row[8],
                        "key": step_row[9]
                    }
                    test_data.append(step_data)

    return test_data



@pytest.mark.parametrize("step", get_test_data_from_excel())
def test_excel_driven_execution(step):
    driver = None
    try:
        keyword = step["Keywords"]

        if keyword == 'browser':
            driver = action.invokeBrowser(step["browser"], step["modulename"], step["TestCaseName"],
                                              step["TestStepName"], step["TestStepID"], step["Requirement"],
                                              step["Description"], keyword, step["Locator"],
                                              step["Testdata"], step["TestCaseDescription"])

        elif keyword == 'enter_unique_text1':
            driver = action.enter_unique_text1(step["browser"], step["modulename"], step["TestCaseName"],
                                     step["TestStepName"], step["TestStepID"], step["Requirement"],
                                     step["Description"], keyword, step["Locator"],
                                     step["Testdata"], step["TestCaseDescription"])

        # TODO: Add more keywords and corresponding Actions methods as needed

    except Exception as e:
        print(f"\n❌ Error in step '{step['TestStepName']}' for browser '{step['browser']}': {str(e)}")
        raise

    finally:
        if driver:
            driver.quit()
