# Exersice 1 sur slack
# Create a dictionary by using all the given variables.
# first_name = 'John'
# last_name = 'Doe'
# favorite_hobby = 'Python'
# sports_hobby = 'gym'
# age = 82

# Person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'favorite_hobby': 'Python',
#     'sports_hobby': 'gym',
#     'age': 82
# }
# # print (f"Person: {Person['first_name']} {Person['last_name']} {Person['favorite_hobby']} {Person['sports_hobby']} {Person['age']}")

# # # Exersice 2 sur slack
# # # Print the total duration of the playlist

# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }
# total = 0
# liste_music = playlist['songs']
# duration_first_music = liste_music[0]['duration']
# for music in liste_music:
 #     music_duration = music ['duration']
 #     total += music_duration
# print (f"Total duration of the playlist: {total}")

# colors = "red, pink"
# for index, color in enumerate(colors):
#     print (f"{index}, {color}")

# verifier que le nombre donner superieur à 18 
# def check_age (age_user)
# if age_user >= 18:
#   print ("you are an adult")
# else age_user < 18:
#     print ("you are a child")

# age_user = int(input("enter your age:"))
# check_age(age_user)


#exersice slack# Create a function average_length_of_words which takes a string as an argument and returns the average length of the words in the string.
# You can assume that there is a single space between each word and that the input does not have punctuation.
# The result should be rounded to one decimal place (hint: see round).
# average_length_of_words('only four lett erwo rdss') == 4 (modifié) 

def calculate_average (sentence):  #here between brackets we put parametres
List_of_words = sentence.split("") #split the sentence into words
print (List_of_words)



    # calculate_average('hello how are you') #here we call the function
