import requests,sys,webbrowser,bs4

res=requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,"html.parser")
print(soup)
linkElements = soup.select('a[href^="/url?q="]')
print(linkElements)
linkToOpen = min(5,len(linkElements))
print(linkToOpen)
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))