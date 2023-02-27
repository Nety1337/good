import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
url="https://auto.ria.com/newauto/marka-jeep/"
file="Auto.csv"
def pars(site = url):
    inf = []
    res = requests.get(site)
    if res.status_code != 200:
        print("Ошибка 1")
    else:
        soup = bs(res.text, features="html.parser")
        soup_list = soup.find_all("section", class_="proposition")
        for i in soup_list:
            usd = soup.find("span", class_="green")
            ua = soup.find("span", class_="size16")
            reg = soup.find("span", class_="region")
            if usd or ua or reg:
                usd = usd.get_text(strip=True).replace(' ', '')
                ua = ua.get_text(strip=True).replace(' ', '')
                reg = reg.get_text(strip=True).replace(' ', '')
            else:
                print("Ошибка 2")
            inf.append({
                "title": i.find("h3", class_="proposition_name").get_text(strip=True),
                "link": i.find("a").get("href"),
                "USD": usd,
                "UA": ua,
                "REG": reg
            })
    print(inf)
pars()
car = ["title", "link", "USD", "UA", "REG"]
f=pd.DataFrame(data=pars(),columns=car)
f.to_csv(file,sep=";",encoding='utf8') #encoding="utf8"