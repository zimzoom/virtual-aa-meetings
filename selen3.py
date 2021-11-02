from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time
import sys

try:
	url = sys.argv[1]
	filename = sys.argv[2]
except IndexError:
	raise SystemExit(f"Usage: {sys.argv[0]} <page-url> <file-name-to-write>")

#chrome_options = Options()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)
#print(driver.find_element_by_id('content').text)

pageSource = driver.page_source
with open(filename, 'w') as file:
	file.write(pageSource)

driver.close()
