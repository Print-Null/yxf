# -- coding: utf-8 --
import pytest
import os
import sys
import test
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    allure_results = test.allure_results_path
    if not os.path.exists(allure_results):
        os.makedirs(allure_results)
    allure_reports = test.allure_report_path
    if not os.path.exists(allure_reports):
        os.makedirs(allure_reports)
    pytest.main(["-s", "test.py", "--alluredir", allure_results])
    os.system(f"allure generate {allure_results} -o {allure_reports}")
