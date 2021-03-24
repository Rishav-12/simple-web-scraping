# This script downloads a user's GitHub profile picture
import requests
from bs4 import BeautifulSoup
import wget

# Using web scraping to obtain the image link and then downloading it to our machine using wget library

github_user = input("Enter your GitHub user name : ")
url = f'https://github.com/{github_user}'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

image = soup.find('img', {'alt' : 'Avatar'})
link = image['src']

profile_pic = wget.download(link)
