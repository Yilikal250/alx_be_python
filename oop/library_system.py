class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def __str__(self):
    return f"Book: {self.title} by {self.author}"    
  
    
class EBook(Book):
  def __init__(self,title, author, file_size:int):
    super().__init__(title, author)  
    self.file_size = file_size
  def __str__(self):
    return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"   


class PrintBook(Book):
  def __init__(self,title, author,page_count:int):
      super().__init__(title, author)
      self.page_count = page_count
  def __str__(self):
    return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
  books = []
  def add_book(self, book):
      self.books.append(book)
  @classmethod
  def list_books(cls):
        for inst in cls.books:
            print(inst)    
 
      