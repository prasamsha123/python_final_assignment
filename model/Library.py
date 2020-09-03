class Library:
    def __init__(self, BookID, BookTitle, Author, MemberType, FirstName, Surname, DateBorrowed, Address):
        self.BookID = BookID
        self.BookTitle = BookTitle
        self.Author = Author
        self.MemberType = MemberType
        self.FirstName = FirstName
        self.Surname = Surname
        self.Address = Address
        self.DateBorrowed = DateBorrowed
        self.Address = Address

    def set_BookID(self, BookID):
        self.BookID = BookID

    def get_BookID(self):
        return self.BookID

    def set_BookTitle(self, BookTitle):
        self.BookTitle = BookTitle

    def get_BookTitle(self):
        return self.BookTitle

    def set_Author(self, Author):
        self.Author = Author

    def get_Author(self):
        return self.Author

    def set_MemberType(self, MemberType):
        self.MemberType = MemberType

    def get_MemberType(self):
        return self.MemberType

    def set_FirstName(self, FirstName):
        self.FirstName = FirstName

    def get_FirstName(self):
        return self.FirstName

    def set_Surname(self, Surname):
        self.Surname = Surname

    def get_Surname(self):
        return self.Surname

    def set_DateBorrowed(self, DateBorrowed):
        self.DateBorrowed = DateBorrowed

    def get_DateBorrowed(self):
        return self.DateBorrowed

    def set_Address(self, Address):
        self.Address = Address

    def get_Address(self):
        return self.Address
