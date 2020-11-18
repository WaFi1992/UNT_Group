import unittest
import requests
from bs4 import BeautifulSoup
import re
from scrape import getBookDetails



class TestMethod(unittest.TestCase):
    

    def testISBN(self):
    # check if a title for book is on page, if not there was a false isbn entered and there are no search results
    # severity: high
    # if we dont get the correct ISBN we cant help our users find the right books
    # test line 7-12 in scrape.py (may move scrape.py into forms.py in the future)

        isbn = 9780321982384 
        
        url = f"https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={str(isbn)}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr"

        #scraping
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        #(scraping) find elements
        title = soup.find(id='describe-isbn-title')
        
        self.assertTrue(title)


    
    def testTitle(self):
        # function to test title pulled vs actual title
        # severity: high
        # if this test fails our users could have the wrong book
        # tests line 26
        r = getBookDetails(9780321982384)
        self.assertEqual(r["title"], "Linear Algebra and Its Applications")
        
    

    def testPublisher(self):
        # function to test title pulled vs actual title
        # severity: high
        # if this test fails our users could have a book from the wrong publisher
        # tests line 29
        r=getBookDetails(9780321982384)
        self.assertEqual(r["publisher"], "Pearson, 2014")

    def testAuthor(self):
        # function to test author pulled vs actual author
        # severity: high
        # if this test fails our users could have a book from the wrong author
        # tests line 32
        r=getBookDetails(9780321982384)
        self.assertEqual(r["author"], "Lay, David; Lay, Steven; McDonald, Judi")


if __name__ == '__main__':
    unittest.main()