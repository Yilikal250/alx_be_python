class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  def __str__(self):
    return f"{self.title} by {self.author}"    
  
    
class EBook(Book):
  def __init__(self, file_size:int, title, author):
    super().__init__(title, author)  
    self.file_size = file_size
  def __str__(self):
    return f"{self.title} by {self.author}, File Size: {self.file_size}"   


class PrintBook(Book):
  def __init__(self, page_count:int,title, author):
      super().__init__(title, author)
      self.page_count = page_count
  def __str__(self):
    return f"{self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
  books = []
  def add_book(self, book):
      self.books.append(book)
  # def list_books(self):
  #     pass    
  def __repr__(self):
         return "me"
      

 
classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

my_library = Library()

my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)


print(Library.books)
 
      