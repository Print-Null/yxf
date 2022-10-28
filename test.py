from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
# chromedriver = base_dir + "tools/chrome/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
# chromedriver = "/usr/bin/chromedriver"
# s = Service(r"D:\chromedriver\106.0.5249.61\chromedriver.exe")

# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options)


def test_baidu():
    driver.get("https://www.baidu.com")
    assert driver.title == "百度一下，你就知道"
    driver.quit()
