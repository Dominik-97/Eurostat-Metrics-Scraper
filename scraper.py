from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome()
driver.get("http://apl.czso.cz/pll/eutab/html.h")

if "Eurostatu" in driver.title:
    print("OK")
else:
    print("NOK")

while len(driver.find_elements_by_xpath("//*[contains(@class, 'dynatree-exp-c') and contains(@class, 'dynatree-has-children')]")) > 0:
    ELEMENTS = []
    ELEMENTS = driver.find_elements_by_xpath("//*[contains(@class, 'dynatree-exp-c') and contains(@class, 'dynatree-has-children')]")
    time.sleep(0.5)
    for element in ELEMENTS:
        element.click()
        time.sleep(0.1)

FIN_ELEM = driver.find_element_by_class_name('dynatree-container').get_attribute('innerHTML')

RESULT = re.sub(r"<(?:a\b[^>]*>|\/a>)", "", FIN_ELEM)

f = open("result.html", "w")
f.write("<head>\n<meta charset=\"UTF-8\">\n</head>\n<body>")
f.write(RESULT)
f.write("\n</body>")
f.close

driver.close()

import subprocess

GENERATE_FILE = subprocess.run(["pandoc", "result.html", "-t", "gfm-raw_html", "-o", "output.md"])
print("The exit code was: %d" % GENERATE_FILE.returncode)