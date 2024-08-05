import requests
from bs4 import BeautifulSoup


target_url=input("enter target url:")

founded_links=[]

def make_request(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    return soup
def craw(url):
    links=make_request(url)
    for link in links.find_all("a"):
        founded_link=link.get("href")
        if founded_link:#== if founded_link not noun
            if "#" in founded_link:
                founded_link=founded_link.split("#")[0]

            if target_url in founded_link and founded_link not in founded_links:
                founded_links.append(founded_link)
                print(founded_link)
                #recursive
                craw(founded_link)




craw(target_url)
#html parsing
