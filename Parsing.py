# import  requests
# res=requests.get("https://coinmarketcap.com/")
# res_text=res.text
# res_parse=res_text.split("<span>")
# coin=[]
# for elem in res_parse:
#     if elem.startswith("$"):
#         for el in elem.split("</span>"):
#             if el.startswith("$") and el[1].isdigit():
#                 print(el)
#                 coin.append(el)
# bitcoin=coin[0]
# print('cost bitcoin =', bitcoin)
# print(coin)

# import pandas as pd
# import requests
# from bs4 import BeautifulSoup as bs
# res = requests.get("https://coinmarketcap.com/")
# if res.status_code==200:
#     soup=bs(res.text,features="html.parser")
#     soup_list=soup.find_all('a',{'href':'/currencies/bitcoin/markets/'})
#     print(soup_list)
#     res=soup_list[0].find('span')
#     print('cost bitcoin =', res.text)

# import requests
# import pandas
# from bs4 import BeautifulSoup as bs
# url = "https://www.work.ua/jobs/?ss=1&setlp=ua"
# file="work.csv"
# res=requests.get(url)
# def res(site=url):
#     inf={"title":[],"zarplata":[]}
#     res = requests.get(site)
#     soup = bs(res.text, features="html.parser")
#     soup_list=soup.find_all("h2", class_="")
#     soup_list2 = soup.find_all("b", class_="")
#     for name in soup_list:
#         inf['title'].append(name.a['title'])
#     for num in soup_list2:
#         inf['zarplata'].append(num.text)
#     return inf
# dannie=["title","zarplata"]
# f=pd.DataFrame(data=res(), columns=dannie)
# f.to_csv(file,sep=";",charset="utf8")

# import requests #poluch dannie
# res=requests.get("https://coinmarketcap.com/")
# res_text=res.text
# res_parse=res_text.split("<span>")
# coin=[]
# for elem in res_parse:
#     if elem.startswith("$"):
#         for el in elem.split("</span>"):
#             if el.startswith("$") and el[1].isdigit():
#                 coin.append(el)
#                 #print(el)
# bitcoin=coin[0]
# print("Bitcoin cost =",bitcoin)

# import requests
# from bs4 import BeautifulSoup as bs
# res=requests.get("https://coinmarketcap.com/")
# if res.status_code==200:
#     soup=bs(res.text,features="html.parser")
#     soup_list=soup.find_all("a",{"href":"/currencies/bitcoin/markets/"})
#     res=soup_list[0].find("span")
#     print("Bitcoin cost =",res.text)

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
url="https://www.work.ua/jobs/?ss=1&setlp=ua"
file="work.csv"
# res=requests.get(url)
# if res.status_code==200:
#     soup = bs(res.text, features="html.parser")
#     soup_list=soup.find_all("h2",class_="")
#     soup_list2 = soup.find_all("b",class_="")
#     for name in soup_list:
#         print(name.a["title"])
#     for num in soup_list2:
#         print(num.text)
def ress(site=url):
    inf={"title":[],"zarplata":[]}
    res = requests.get(site)
    soup = bs(res.text, features="html.parser")
    soup_list=soup.find_all("h2",class_="")
    # soup_list2 = soup.find_all("b",class_="")
    soup_list2 = soup.find_all("p", class_="overflow")
    for name in soup_list:
        inf["title"].append(name.a["title"])
    for num in soup_list2:
        inf["zarplata"].append(num.text)
    return inf
dannie=["title","zarplata"]
f=pd.DataFrame(data=ress(),columns=dannie)
f.to_csv(file,sep=";",encoding='utf8') #encoding="utf8"