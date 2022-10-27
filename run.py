# -- coding: utf-8 --
import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = base_dir.replace("\\", "/") + "/"
    allure_results_path = os.path.join(base_dir, "allure-results")
    allure_report_path = os.path.join(base_dir, 'allure-results/reports')
    if not os.path.exists(allure_results_path):
        os.makedirs(allure_results_path)
    if not os.path.exists(allure_report_path):
        os.makedirs(allure_report_path)
    pytest.main(["-s", "test.py", "--alluredir", allure_results_path])
    os.system(f"allure generate {allure_results_path} -o {allure_report_path}")
