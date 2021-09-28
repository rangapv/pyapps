#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

import pandas as pd
dfs = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")

response = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")
document = response.text


soup = BeautifulSoup(document, "lxml")
#prints the entire url in html tag format
#print(soup.prettify())

headings = soup.find_all("h2")
subtitles = [x.text for x in headings]
#prints the heading only
print(subtitles)



table = soup.find("table")
output_rows = []
for table_row in table.find_all('tr'):
     columns = table_row.find_all('td')
     output_row = [x.text for x in columns]
     output_rows.append(output_row)

#prints in table form
print(pd.DataFrame(output_rows))


