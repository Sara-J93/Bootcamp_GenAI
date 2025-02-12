<<<<<<< HEAD
# # Exercise2
# # -1
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# print (family.items() ) 
# family = {
#     'rick': 43,
#     'beth': 13,
#     'morty': 5,
#     'summer': 8
# }
# total_cost = 0
# for key, value in family.items():
#     if value < 3:
#         price = 0
#     elif value >= 3 and value <= 12:
#         price = 10
#     else :
#         price = 15
#     print (f"{key} should pay {price}")
# #2
#     total_cost += price 
# #     print (f"Total cost for the family is {total_cost}")

#     # Exercise 4
# # def describe_city( city, country= "France"):
# #     print (f"{city} is in {country}.")
# # describe_city("Paris")
# # describe_city("Tokyo", "Japan")
# # describe_city("New York", "USA")

# # Exercise 5*
# import random
# def generate_random_number(user_number):
#     random_number = random.randint(1, 100)
#     if user_number == random_number:
#         print("Success! The numbers match!")
#     else:
#         print(f"Fail! The numbers don't match. Your number: {user_number}, Random number: {random_number}")


# user_number = int(input("Enter a number between 1 and 100: "))
# generate_random_number(user_number)

# Exercise 6
# def make_shirt(size="large", message="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {message}.")
# make_shirt()

# make_shirt("medium")

# make_shirt("small", "Hello, World!")

# Exercise 7
import random

def get_random_temp(season):
     
    if season.lower() == "winter":
        return random.randint(-10, 16)
    elif season.lower() == "spring":
        return random.randint(5, 25)
    elif season.lower() == "summer":
        return random.randint(15, 40)
    elif season.lower() == "autumn" or season.lower() == "fall":
        return random.randint(0, 20)
    else:
        return random.randint(-10, 40) 

# temperature = get_random_temp()
# print(f"The randomly generated temperature is: {temperature}°C")
   
# def main ():
#     temperature = get_random_temp()
#     print(f"The temperature right now is {temperature} degrees Celsius.")


#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 17 <= temperature <= 23:
#         print("Nice and cool weather, enjoy your day!")
#     elif 24 <= temperature <= 32:
#         print("It’s warm, stay hydrated.")
#     else:
#         print("It’s really hot! Wear sunscreen and stay in the shade.")
# main()





=======
# # Exercise2
# # -1
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# print (family.items() ) 
# family = {
#     'rick': 43,
#     'beth': 13,
#     'morty': 5,
#     'summer': 8
# }
# total_cost = 0
# for key, value in family.items():
#     if value < 3:
#         price = 0
#     elif value >= 3 and value <= 12:
#         price = 10
#     else :
#         price = 15
#     print (f"{key} should pay {price}")
# #2
#     total_cost += price 
# #     print (f"Total cost for the family is {total_cost}")

#     # Exercise 4
# # def describe_city( city, country= "France"):
# #     print (f"{city} is in {country}.")
# # describe_city("Paris")
# # describe_city("Tokyo", "Japan")
# # describe_city("New York", "USA")

# # Exercise 5*
# import random
# def generate_random_number(user_number):
#     random_number = random.randint(1, 100)
#     if user_number == random_number:
#         print("Success! The numbers match!")
#     else:
#         print(f"Fail! The numbers don't match. Your number: {user_number}, Random number: {random_number}")


# user_number = int(input("Enter a number between 1 and 100: "))
# generate_random_number(user_number)

# Exercise 6
# def make_shirt(size="large", message="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {message}.")
# make_shirt()

# make_shirt("medium")

# make_shirt("small", "Hello, World!")

# Exercise 7
import random

def get_random_temp(season):
     
    if season.lower() == "winter":
        return random.randint(-10, 16)
    elif season.lower() == "spring":
        return random.randint(5, 25)
    elif season.lower() == "summer":
        return random.randint(15, 40)
    elif season.lower() == "autumn" or season.lower() == "fall":
        return random.randint(0, 20)
    else:
        return random.randint(-10, 40) 

# temperature = get_random_temp()
# print(f"The randomly generated temperature is: {temperature}°C")
   
# def main ():
#     temperature = get_random_temp()
#     print(f"The temperature right now is {temperature} degrees Celsius.")


#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 17 <= temperature <= 23:
#         print("Nice and cool weather, enjoy your day!")
#     elif 24 <= temperature <= 32:
#         print("It’s warm, stay hydrated.")
#     else:
#         print("It’s really hot! Wear sunscreen and stay in the shade.")
# main()





>>>>>>> origin/master
   