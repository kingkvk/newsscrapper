import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

today = date.today()
date=today.day
year=today.year
month=today.month

url=f"https://vajiramias.com/current-affairs/{year}/{month}"
GS1=["History","Culture","Geography","Social Issues"]
GS2=["Polity & Governance","International","Social Justice"]
GS3=["Defence & Security","Science & Tech","Economy","Education","Health","Environment","Diaster Management"]
GS4=["Ethics","Integrity","Aptitude"]

data=requests.get(url)

soup=BeautifulSoup(data.content,'html.parser')
title=soup.find_all("div", {"class": "feed_item_title"})
stitle=soup.find_all("div", {"class": "feed_item_subtitle"})
content=soup.find_all("div",{"class":"feed_item_content"})
category=soup.find_all("span",{"class":"tag_box"})
date=soup.find_all("small")

Title=[]
Stitle=[]
Content=[]
Category=[]
Date=[]
Subject=[]
for x in title:
    Title.append((x.text).strip())
for x in stitle:
    Stitle.append((x.text).strip())
for x in content:
    Content.append((x.text).strip())
for x in category:
    Category.append((x.text).strip())
for x in date:
    Date.append((x.text).strip())
for x in Category:
    if x in GS1:
        Subject.append("GS1")
    elif x in GS2:
        Subject.append("GS2")
    elif x in GS3:
        Subject.append("GS3")
    elif x in GS4:
        Subject.append("GS4")
    else:
        Subject.append("CA")

dataset=list(zip(Title,Stitle,Content,Category,Date,Subject))
df=pd.DataFrame(dataset,columns=['feed_title','feed_subtitle','feed_content','feed_category','feed_date','feed_subject'])

url="http://boringpanda.pythonanywhere.com/"
for x in range(10):
    q={
        "title":Title[x],
        "subtitle":Stitle[x],
        "content":Content[x],
        "category":Category[x],
        "date":date[x],
        "subject":Subject[x]
    }
 
    data=requests.put(url+"news/",q)
print(data)