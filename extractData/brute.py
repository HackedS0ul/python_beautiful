import requests
from bs4 import BeautifulSoup

target_url = "https://esaurida.lt"

resp = requests.get(target_url)
file = 'data.txt'
soup = BeautifulSoup(resp.content, 'html.parser')
temp_links = []
# returns title of the page
#print(soup.title.string)

# get and add links into list 
getLinks = soup.find_all('a', href=True)
# checking that any link is available
links = []
if getLinks:
    for i in getLinks:

        if i not in temp_links:
            temp_links.append(i['href'].strip())
            print(len(temp_links))
        else:
            print("record is existing!")
    
else:
    print("Can't find any link")
#length of links
#print(len(links))

# removing duplicates for data file

for data in temp_links:
    if data not in links:
        links.append(data)
    else:
        print("Url found in data file.. ")

        print("removing element on line " + str(len(links)))


with open(file, 'w+', encoding='utf-8') as f:
    f.write(str("\n".join(links)))
