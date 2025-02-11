# Exercise 1
sentence = ("abcd")
for _ in sentence: print ("Hello world")
# or
for _ in range(4): print ("Hello World")

# Exercise 2
result = (99 ** 3)*8
print(result)

# Exercise 3
user_name = input ("What's your name?")
my_name = "Sara"
if user_name == my_name:
    print ("Our parents have a great taste in names!")
else:
    print (f"nice name {user_name}, but I still prefer {my_name}")

# Exercise 4
hight = int(input("How tall are you in cm?"))
if hight > 145:
    print ("You are tall enough to ride")
else: print ("You need to grow some more to ride")

Exercise 5
my_fav_numbers = {9, 19}
my_fav_numbers.add(90)
my_fav_numbers.add(99)
print (my_fav_numbers)
fav_numbers_list = list (my_fav_numbers)
print (fav_numbers_list)
my_fav_numbers.remove(19)
print (my_fav_numbers)
friend_fav_numbers = {10, 20, 30}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print (our_fav_numbers)

Exercise 6
no because tuples are immutable once created

Exercise 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
print (basket)
basket.insert(0, "Apples")
print (basket)
num_apples = basket.count("Apples")
print (num_apples)
basket.clear()
print (basket)

# Exercise 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    print (sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print (f"I made your {sandwich}")