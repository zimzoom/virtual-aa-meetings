"""
Utility functions
"""
import requests

# https://dataquestio.github.io/web-scraping-pages/simple.html
# https://aa-intergroup.org/meetings?types=English
# http://pythonscraping.com/pages/javascript/ajaxDemo.html

def save_html(url, filename):
	page = requests.get(url)
	if page.status_code == 200:
		with open(filename, 'w') as file:
			file.write(page.text)
	else:
		print("Bad status code: ", page.status_code)

