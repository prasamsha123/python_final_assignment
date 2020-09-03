class Book:
    def __init__(self, BookID, BookName, Author, BookEdition, DateBorrowed, DateIssued):
        self.BookID = BookID
        self.BookName = BookName
        self.Author = Author
        self.BookEdition = BookEdition
        self.DateBorrowed = DateBorrowed
        self.DateIssued = DateIssued

    def set_BookID(self, BookID):
        self.BookID = BookID

    def get_BookID(self):
        return self.BookID

    def set_BookName(self, BookName):
        self.BookName = BookName

    def get_BookName(self):
        return self.BookName

    def set_Author(self, Author):
        self.Author = Author

    def get_Author(self):
        return self.Author

    def set_BookEdition(self, BookEdition):
        self.BookEdition = BookEdition

    def get_BookEdition(self):
        return self.BookEdition

    def set_DateBorrowed(self, DateBorrowed):
        self.DateBorrowed = DateBorrowed

    def get_DateBorrowed(self):
        return self.DateBorrowed

    def set_DateIssued(self, DateIssued):
        self.DateIssued = DateIssued

    def get_DateIssued(self):
        return self.DateIssued



