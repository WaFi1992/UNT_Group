import unittest
from scrape import getBookDetails



class TestMethod(unittest.TestCase):

    def testISBN(self):
                


    def testTitle(self):
        r = getBookDetails(9780321982384)
        self.assertEqual(r["title"], 'Linear Algebra and Its Applications')
        

    #def testTitle(self):
    #    self.assertEqual(self, 'Linear Algebra and Its Applications')

    #def testPublisher(self):
    #    self.assertEqual(self, "Pearson, 2014")

    #def testAuthor(self):
    #    self.assertEqual(self, "Lay, David; Lay, Steven; McDonald, Judi")


if __name__ == '__main__':
    unittest.main()