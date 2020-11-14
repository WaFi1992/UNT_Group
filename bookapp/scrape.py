import requests
from bs4 import BeautifulSoup
import re


#isbn = StringField('ISBN', validators=[DataRequired()])


def getBookDetails(isbn):

    #(scraping) insert isbn into url to navigate to page with book info
    url = f"https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={str(isbn)}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr"

    results = {}

    #scraping
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #(scraping) find elements
    #might have to take another look at how to retrieve the img
    imgCover = soup.find(id='coverImage')
    #print(imgCover.get('src'))

    #find title in between brackets
    title = soup.find(id='describe-isbn-title')
    #print(f"Title: {title.contents[0]}")

    publisher = soup.find(itemprop='publisher')
    #print(f"Publisher: {publisher.contents[0]}")

    author = soup.find(itemprop='author')
    #print(f"Author: {author.contents[0]}")

    results.update({'imgCover': imgCover.get('src'),
                    'title': title.contents[0],
                    'publisher': publisher.contents[0],
                    'author': author.contents[0]})
    

    return results
