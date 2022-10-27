from selenium import webdriver
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = base_dir.replace("\\", "/") + "/"
allure_results_path = os.path.join(base_dir, "allure-results")
allure_report_path = os.path.join(base_dir, 'allure-results/reports')
# chromedriver = base_dir + "tools/chrome/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)


def test_baidu():
    driver.get("https://www.baidu.com")
    assert driver.title == "百度一下，你就知道"
    driver.quit()
