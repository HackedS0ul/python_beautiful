import requests
from bs4 import BeautifulSoup
import os 
from os.path import exists

target_url = "https://esaurida.lt"

resp = requests.get(target_url)
file = 'data.txt'
soup = BeautifulSoup(resp.content, 'html.parser')
links = []
# returns title of the page
#print(soup.title.string)

# get and add links into list 
getLinks = soup.find_all('a', href=True)
# checking that any link is available 
if getLinks:
    for i in getLinks:
        
        if i is not links:
            links.append(i['href'].strip())
        else:
            print("record is existing!")
    

else:
    print("Can't find any link")
#length of links
#print(len(links))




with open(file, 'w+', encoding='utf-8') as f:
    if result is not file:
       f.write(str("\n".join(links)))
    else:
        os.remove()
        

