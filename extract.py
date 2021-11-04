"""
Extracts data from page source code and saves it to csv file
Takes two arguments: file containing page source code, csv file to write to
"""

import sys
from bs4 import BeautifulSoup
import pandas as pd
import re

try:
	pagefile = sys.argv[1]
	csvfile = sys.argv[2]
except IndexError:
	raise SystemExit(f"Usage: {sys.argv[0]} <page-source.txt> <file-name-to-write.csv>")

print("Parsing...")
with open(pagefile) as file:
    soup = BeautifulSoup(file, 'html.parser')

all_entries = []
print("Extracting...")
for meeting in soup.find_all(class_='css-ggcp4y'):
    this_entry = {}
    this_entry["Name"] = meeting.find(class_='css-1m3h46c').get_text()

    daytime = meeting.find(class_='css-1kn9d3w').get_text()
    # A sub-group of meetings have 'Ongoing' here rather than 'Tuesday 8:00 pm'etc
    if re.match('.*day', daytime):
        this_entry["Day"] = re.match('.*day', daytime).group()
        this_entry["Time"] = daytime[-8:].strip()
    else: this_entry["Day"] = daytime
    
    entry_link_buttons = meeting.find_all(class_='css-1akp03c')
    entry_link_titles = [link_bttn['title'] for link_bttn in entry_link_buttons]
    for title in entry_link_titles:
        if re.match('Visit (.+)', title):
            this_entry["Video"] = re.match('Visit (.+)', title).group(1)
        elif re.match('Email (.+)', title):
            this_entry["Email"] = re.match('Email (.+)', title).group(1)
        elif re.match('Call (.+)', title):
            this_entry["Phone"] = re.match('Call (.+)', title).group(1)
            
    # Not every meeting has a description
    if meeting.find(class_='css-fzcsno'):
        this_entry["Desc"] = meeting.find(class_='css-fzcsno').get_text()

    # Removes weekday category labels ('Tuesday' etc) bc they are redundant
    entry_categ_buttons = meeting.find_all(class_='css-108n2y7')
    entry_categs = [button.get_text() for button in entry_categ_buttons]
    categ_words = [word for word in entry_categs if not re.match('.*day', word)]
    this_entry["Categories"] = ",".join(categ_words)
    
    all_entries.append(this_entry)

print("Successfully extracted", len(all_entries), "entries")

df = pd.DataFrame(all_entries)
df.to_csv(csvfile, index=False)

print("Successfully saved data to", csvfile)
