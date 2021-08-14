# class Book:
#     #attributes - size, pages, colour, thickness
#     #methods - turning a page, closing, opening

#     def __init__(self, title, author, pages, current_page):
#         #assignment to object attributes
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
#         self.bookmark = 1  #assign by default
    
#     def bookmark_page(self, page):
#         if self.bookmark <= self.page:
#             self.bookmark = page
    
#     def turn_page(self):
#         if self.current_page == self.pages:
#             self.current_page = 1
#         else:
#             self.current_page += 1 

#     #string representation
#     def __str__(self):
#         return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"
    
#     def __len__(self):
#         return self.pages

#     def turn_page_back(self):
#         self.current_page -= 1
#     #create a method turn back the page

#     def go_to_page(self, page_number):
#         if page_number <= self.pages:
#             self.current_page = page_number


    

# my_book = Book("A great book", "me", 100, 99)
# # my_book.go_to_page(199)
# # print(my_book.__str__())
# # print(my_book)
# # print(my_book.bookmark) #attr
# my_book.turn_page() #method
# # my_book.bookmark_page()
# print(my_book.current_page)
#exercises
#Q1 as above

#Q2
def __init__(self, width, height):
    self.width = width
    self.height = height

#Q3
class Vehicle:

    def __init__(self, model, make, colour, seating, max_speed):
        self.model = model
        self.make = make
        self.colour = colour
        self.seating = seating
        self.max_speed = max_speed

    def __str__ (self):
        return f"Vehicle Summary:\n Make: {self.make}\n Model: {self.model}\n Colour: {self.colour}\n Seating: {self.seating}\n Max Speed: {self.max_speed}\n"

ford = Vehicle ("Ford", "Falcon", "blue", 5, 250)

print(ford)
