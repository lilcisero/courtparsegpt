import requests
from bs4 import BeautifulSoup

url = 'https://www.drudgereport.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# You can use the `find_all()` method to find all `\<img\>` tags, which represent images on a webpage. For example, to find all images and print their `src` attributes (which contain the image URLs), you can use the following code:

img_tags = soup.find_all('img')
for img in img_tags:
    print(img['src'])


