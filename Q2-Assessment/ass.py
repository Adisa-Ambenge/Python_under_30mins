# Question 1
# Input = story,length,moral_lessons,age_group
# Process = determine the classes and methods
# Output =translated story
       
class Story:
     def __init__(self,content,length,moral_lessons,age_group):
         self.content=content
         self.length=length
         self.moral_lessons=moral_lessons
         self.age_group = age_group
         
     def colonialiasm(story):
         pass
     def Myths(story):
         pass

class StoryTeller:
    def __init__(self, name, language, culture):
        self.name = name
        self.language = language
        self.culture = culture
    def colonialism(self):
        pass
    def Myths(self):
        pass


class Translator:
    def translate(story,language):
        stories = {self.content},language
        return stories

# Question 2
# Input = ingredients,prep time,cooking method,nutritional info
# Process = determine class,subclasses
# Output = display recipe and it's info


class Recipe:
    def __init__(self, food, ingredients, prep_time, cooking_method, nutritional_info):
        self.food = food
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info

recipe1 = Recipe("chicken","onions,tomato","30mis","fry","protein")
class MoroccanRecipe(Recipe):
    def __init__(self,ingredients, prep_time, cooking_method, nutritional_info, spices):
      super().__init__(ingredients, prep_time, cooking_method, nutritional_info)
      self.spices = spices

    def display_recipe(self):
     super().display_recipe()
     return {self.spices}

class EthiopianRecipe(Recipe):
    def __init__(self,ingredients, prep_time, cooking_method, nutritional_info,spicess):
     super().__init__(ingredients, prep_time, cooking_method, nutritional_info)
     self.spicess = spicess

    def display_recipe(self):
     super().display_recipe()
     return {self.spicess}


class NigerianRecipe(Recipe):
    def __init__(self,ingredients, prep_time, cooking_method, nutritional_info, plantain):
     super().__init__(ingredients, prep_time, cooking_method, nutritional_info)
     self.plantain = plantain

    def display_recipe(self):
     super().display_recipe()
     return {self.plantain}
 
#  Question 5
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price =price
        self.quantity=quantity
    def calculate_total():
        price = 2000
        quantity = 5
        product = price * quantity
      
# Question 6
class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def calculate_average(self):
        total_grades = sum{self.grades}
        avg = total_grades/len{self.grades}
        return avg
    
    def display_info(self):
        return f" {self.name} {self.age} {self.grades}"

    def pass(self):
    average = self.calculate_average()
    return average

# Question 7

class FlightBooking:
    def __init__(self):
        self.flights = []
        
def search_flight(self,destnination,date):
    available_flights = []
    for flight in self.flights:
        if flight.destination ==destination and flight.date ==date:
            available_flights.append(flight)
            return available_flights
             

def reserve_seat(self,flight,customer):
    return f"{self.customer} reserved seat in {self.flight}"

#  INPUT = Title,author,isAvailable
#  process= determine class and methods
#  output = book title
 
class Book:
    def __init__(self, title, author, available):
     self.title = title
    self.author = author
    self.available= available

class LibraryCatalog:
    def __init__(self):
     self.books = []

def new_book(self, book):
   self.books.append(book)

def search_by_title(self, title):
  books = []
for book in self.books:
  if book.title.lower() == title.lower():
   books.append(book)
return books

def search_by_author(self, author):
  books = []
for book in self.books:
   if book.author.lower() == author.lower():
    books.append(book)
return books