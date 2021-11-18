AA Virtual Meetings Directory Scraper & Analytics
=====

* scrapes the online AA meetings directory, and saves the contents including category tags and user-generated descriptions into a csv file
* demos EDA and inferential statistical analysis on the data

Background
---
[aa-intergroup.org](https://aa-intergroup.org/meetings) contains the official online directory of virtual/remote Alcoholics Anonymous meetings. The meetings are created and maintained by real people, featuring titles and descriptions written in unstructured plain language, sometimes long and colorful, sometimes short and reserved. These descriptions are meant to attract desired members and presumably keep away undesired bad actors. These characteristics make this dataset a good potential target for natural language analysis. *(coming soon)*

Another useful feature is the use of category labels that denote whether meetings are closed to non-AA-members, focused on particular study materials, only for men/women/LGBTQ etc. A meeting may have more than one category label, and the directory does seem to be successfully enforcing those categories that are exclusive (eg, records can not and are not both Open and Closed, Men Only and Women Only, etc). **The current version of this project focuses on statistical analysis that makes use of these plentiful categories in combination with complete weekday and time schedule information.**

Contents
---
The project is demonstrated in four jupyter notebooks:

1. `1-Scraping.ipynb` demonstrates obtaining the dataset with the use of Selenium, explains how to use the `selen.py` script
2. `2-Parsing-Storing.ipynb` demonstrates extracting data from the scraped page source code, explains how to use the `extract.py` script
3. `3-EDA.ipynb` demonstrates exploratory data analysis and visualizations
4. `4-Analysis` demonstrates a two-tailed single sample t test, one-tailed two sample t test, and chi square test 