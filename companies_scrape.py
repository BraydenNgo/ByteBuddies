import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://www.sec.gov/rules/other/4-460list.htm'
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
table = soup.find('table')
companies_lst = []

# extract all the companies
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        data = cell.text.strip()
        companies_lst.append(data)


# remove the empty data in the list
while '' in companies_lst:
    companies_lst.remove('')

companies_lst = companies_lst[1::]
df = pd.DataFrame(companies_lst, columns=['companies'])

# write the DataFrame to a CSV file
df.to_csv('my_data.csv', index=False)
print(df)