import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd

bank_info = []

for len in range(1,20):
    link = f"https://bank.uz/uz/credits?PAGEN_1={len}"

    req = requests.get(link)
    soup = bs(req.text,'html.parser')

    credits = soup.find_all('div',class_='table-card-offers-bottom')

    for credit in credits:

        info = credit.find('div',class_='table-card-offers-block1-text')
        bank = info.span.text

        credit_type = info.a.text
        annual_percent = credit.find('div',class_="table-card-offers-block2").text

        year_ = credit.find('div',class_='table-card-offers-block3')
        term = year_.span.text

        quantity_ = credit.find('div',class_='table-card-offers-block4')
        quantity = quantity_.span.text

        more_info = credit.find('div',class_='table-card-offers-block5')
        link = more_info.a['href']

        bank_info.append([bank,credit_type,annual_percent,term,quantity,link])

fields = ['Bank','Credit Type', 'Annual Percent', 'Term','Quantity','More Info Link']


df = pd.DataFrame(data=bank_info,columns=fields)
df.to_csv('bank_info.csv')
