class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
class EBook(Book):
  def __init__(self, file_size:int, title, author):
    super().__init__(title, author)  
    self.file_size = file_size
    
class PrintBook(Book):
  def __init__(self, page_count:int,title, author):
      super().__init__(title, author)
      self.page_count = page_count

      