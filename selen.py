"""
Opens browser, navigates to web page, scrolls all the way to bottom,
    and saves page source code to file
Takes two arguments: page URL, file to write to
"""

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

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Save source to file
pageSource = driver.page_source
with open(filename, 'w') as file:
	file.write(pageSource)

# Close browser
input("Press enter to end session")
driver.quit()
