# # exercise 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat_1 = Cat("Mika", 23)
# cat_2 = Cat("Sara", 31)
# cat_3 = Cat("Olga", 38)

# def oldest_cat(cats):
#     oldest_age = 0
#     for cat in cats:
#         if cat.age > oldest_age:
#             oldest_age = cat.age
#             oldest_cat = cat
#     return oldest_cat

# oldest = oldest_cat([cat_1, cat_2, cat_3])

# print(f"The oldest cat is {oldest.name}, aged {oldest.age}.")


# exercise 2

# class Dog:
#     def __init__ (self, name, height):
#         self.name = name
#         self.height = height

#     def bark (self):
#         print (f"{self.name} goes woof" )
    
#     def jump (self): 
#         print (f"{self.name} jumps {self.height*2}")


# davids_dog = Dog("Rex", 50)

# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)

# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print (f"{davids_dog.name} is taller than {sarahs_dog.name}")

# exercise 3
# class Song:
#     def __init__ (self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print (line)
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#  exercise 4
class Zoo:
    def __init__ (self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)       #append means add. it adds the new animal to the list
    def get_animals(self):
        print (self.animals)
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}

