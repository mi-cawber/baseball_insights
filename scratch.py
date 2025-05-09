import requests as req 
import bs4 

res = req.get('https://mi-cawber.github.io/music.html')

soup = bs4.BeautifulSoup(res.text, 'html.parser')



# captures wanted elements using CSS selector?
elems = soup.select('img')

print(len(elems))

# iterate over elements
for img in elems:
    print(img)