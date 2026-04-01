import requests
from bs4 import BeautifulSoup
import pandas as pd 

url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
#print(r)

soup= BeautifulSoup(r.text,"lxml")
#print(soup)

table= soup.find("table", class_="ih-td-tab w-100 auction-tbl")
#print(table)
title=table.find_all("th")

header=[]
for i in title:
    name=i.text
    header.append(name)
#print(header)
df=pd.DataFrame(columns=header)
#print(df)

rows=table.find_all("tr")
# #print(rows)
for i in rows[1:]:
    first_td = i.find_all("td")[0].text.strip().replace("\n","")
    data=i.find_all("td")[1:]
    row=[tr.text.strip().replace("\n","") for tr in data]
     #print(row)
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
print(df)

#df.to_csv("ipl 2022 stat auction.csv")
