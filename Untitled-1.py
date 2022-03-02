'''apple = ((4*2)*(3.14))
print (apple)
print ("Apple is:", apple, "inches in circumference")
color = input ("What colors are apples? ")
print (color)'''
## This is how you find the circumference of an apple.

'''name = "Steve"
verb = "runs"
preposition = "to"
article = "the"
direct_object = "store"
print (
    direct_object.upper() + verb.title() + preposition.lower() + name.lower()
)'''
#.upper makes everything uppercase, .title makes the first letter capital, .lower makes everything lowercase.

'''deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck.append(2)
print(deck)'''
#Append Adds function to the end of the list.

'''deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck.insert (1,"charmander")
print(deck)'''
#Insert function adds to the list

'''deck = ["pikachu", "mew", "mewtwo", "charizard"]
deck = deck.pop()
print(deck)'''
#Pop removes an item among the list depending on the position, default is last.

'''my_list = ["it's", "peanut butter", "jelly", "time"]
new_word=''
for word in my_list:
    new_word += word + " "
print (new_word)'''
#For every new word in the list add a " " so it will go to the next word.

'''my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
my_string = ""
for index, object in enumerate(my_list):
    my_string += object + " "
    if index == 3 or index == 4:
        my_string += "and "
    print(my_string)'''

'''my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for index in range(3):
    print(my_list[index], end=" ")'''
#Range specifies up to which point to stop reading.

'''my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
my_string = ""
for index in range(len(my_list)):
    if index ==6:
        my_string += "chillin' with my homie"
    my_string[index] = "chicken wing"
print(my_string)'''
#Len is = Length of list

'''my_list = [1, 3.0, ["a","b", ["A","B","C"], "d"], "John"]
for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end=" ")'''
#isinstance iterates the group within member

'''my_list = [1, 3.0, ["a","b", ["A","B","C"], "d"], "John"]
print(my_list[2][2][0])'''

'''my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for food in my_list:
    if food == "chicken wing":
        continue
    print(food, end=" ")'''

'''my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
for food in my_list:
    if food == "chicken wing":
        break
    print(food, end=" ")'''
#No output because string is broken.

'''name = "Destiny's Child"
if name == "Destiny's Child":
    print ("Say my name, say my name", end=" ")
print("If no one is around you", end=" ")
if name:
    print("Say baby I love you", end=" ")
else:
    print("if you ain't runnin' game", end=" ")'''
#an empty string evaluates to False and a string contaiing characters will return True.

'''x=5
y=10
i="5"
j="10"
if x == i and x != y:
    print ("Blackbird", end=" ")
else:
    print("Singing", end=" ")
print("in the", end=" ")
if x < int(j) or i ==j:
    print("dead", end=" ")
else:
    print("of night", end=" ")'''

'''x = 5
print("A Spoon", end=" ")
if x == 4 or x==5:
    print ("full of", end=" ")
elif x>=4:
    print("sugar", end=" ")
else:
    print("helps the medicine", end=" ")
print("go down", end=" ")'''
#elif is a way to chain statements short for else if.
#This will check another condition if the previous conditions failed (returned false)
#elif must be after an 'if' and before an 'else'
