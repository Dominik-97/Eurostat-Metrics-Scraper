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


#COUNT_OF_ELEMS = len(driver.find_elements_by_xpath('//*[@class="dynatree-exp-c"]'))
#COUNT_OF_ELEMS = len(driver.find_elements_by_class_name('dynatree-has-children'))
#ELEMENTS = driver.find_elements_by_class_name('dynatree-has-children')
#print(dir(driver))
#[@style='background:#0373F1;']

#print(COUNT_OF_ELEMS)

#COUNT_OF_ELEMS = len(driver.find_elements_by_xpath('//*[@class="dynatree-expander"]'))
#ELEMENTS = driver.find_elements_by_xpath('//*[@class="dynatree-expander"]')

#i = 0

print(len(driver.find_elements_by_xpath("//*[contains(@class, 'dynatree-exp-c') and contains(@class, 'dynatree-has-children')]")))

while len(driver.find_elements_by_xpath("//*[contains(@class, 'dynatree-exp-c') and contains(@class, 'dynatree-has-children')]")) > 0:#i < COUNT_OF_ELEMS:
    #print(COUNT_OF_ELEMS)
    ELEMENTS = []
    ELEMENTS = driver.find_elements_by_xpath("//*[contains(@class, 'dynatree-exp-c') and contains(@class, 'dynatree-has-children')]")
    time.sleep(0.5)
    for element in ELEMENTS:
        #print(ELEMENTS)
        element.click()
        time.sleep(0.1)
    #i += 1

FIN_ELEM = driver.find_element_by_class_name('dynatree-container').get_attribute('innerHTML')
#print(FIN_ELEM)

result = re.sub(r"<(?:a\b[^>]*>|\/a>)", "", FIN_ELEM)

f = open("result.html", "w")
f.write("<head>\n<meta charset=\"UTF-8\">\n</head>\n<body>")
f.write(result)
f.write("\n</body>")
f.close

#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()

import subprocess

generate_file = subprocess.run(["pandoc", "result.html", "-t", "gfm-raw_html", "-o", "output.md"])
print("The exit code was: %d" % generate_file.returncode)