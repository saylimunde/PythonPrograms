class Book:
    def __init__(self,title,author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.royalty = 0

    #getter and setter for title

    def gettitle(self):
        return self.title

    def settitle(self,value):
        self.title = value

    #getter and setter for author


    def getauthor(self):
        return self.author

    def setauthor(self,value):
        self.author = value

    #getter and setter for publisher

    def getpublisher(self):
        return self.publisher

    def setpublisher(self,value):
        self.publisher = value

    #getter and setter for price

    def getprice(self):
        return self.getprice

    def setprice(self,value):
        self.price = value

    #getter and setter for royalty

    # def getroyalty(self):
    #     return self.royalty

    # def setroyalty(self,value):
    #     self.royalty = value
        
    def calculate_royalty(self,copies_sold):
        if copies_sold <= 500:
            royalty =  0.10

        elif copies_sold <= 1500:
            royalty = 0.125
        else:
            royalty = 0.15
            
        self.royalty = copies_sold * self.price * royalty
        return self.royalty

class Ebook(Book):

    def __init__(self,title,author, publisher, price,ebook_format):
        super().__init__(title,author,publisher,price)
        self.ebook_format = ebook_format

    def calculate_royalty(self,copies_sold):

        royalty = super().calculate_royalty(copies_sold)

        royalty_after_gst = royalty * 0.88
        self.royalty = royalty_after_gst
        return royalty_after_gst

book1 = Book("The Alchemist", "Paulo Coelho", "HarperCollins", 879)
print(f"Book Title: {book1.title}")

ebook1 = Ebook("Think Like a Monk", "Jay Shetty", "Simon & Schuster", 258, "EPUB")
print(f"Ebook Title: {ebook1.title}")
print(f"Ebook Format: {ebook1.ebook_format}")

book_royalty = book1.calculate_royalty(1000)
print(f"Book Royalty for 1000 copies: {book_royalty} Rs")

ebook_royalty = ebook1.calculate_royalty(1000)
print(f"Ebook Royalty for 1000 copies: {ebook_royalty} Rs")
