# Challenge1
number = int(input("choose a number"))
length = int(input("choose length of the list"))
multiples = [number * i for i in range(1, length +1)]
print (multiples)

# Challenge2
word = input("Enter a word")
new_word = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        new_word += word[i]
        print (new_word) 