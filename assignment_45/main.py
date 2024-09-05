# QUESTION01: Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

person1= "Eric"
print(f"Hello {person1}  would you like to learn some Python today?")

# QUESTION:02 3. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

person2="Aleeza"
print(person2.lower(),person2.upper(),person2.title())

# QUESTION:04 Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
message = "I have no speciall talent,I am only passionately curious"
print(f"Albert Einstein said, {message}")

# QUESTION05:5. Famous Quote 2: Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.

famous_person="Albert Einstein"
message2="I have no speciall talent,I am only passionately curious"
print(f"{famous_person} said,{message2}")

#QUESTION:06 Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name after striping the white spaces.

person3= "\t\n Aleezy \t\n"
print("Name with whitespace:")
print(person3)
striped_name=person3.strip()
print("\nName after stripping whitespace:")
print(striped_name)

# QUESTION 07: Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results.
print("Addition: 5+3=",5+3)
print("Subtraction: 12-4=" ,11-3)
print("Multiplication: 2*4=",2*4)
print("Division: 24/3=",24//3)

# QUESTION 08:8. You should create four lines that look like this:

# _____________________________________________

# console.log(5 + 3)

# _____________________________________________

# Your output should simply be four lines with the number 8 appearing once on each line.
print("________________________________")
print(5+3)
print("________________________________")
print(12-4)
print("________________________________")
print(4*2)
print("________________________________")
print(24//3)
print("________________________________")

# QUESTION 09:Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.

favourite_no="24"
print(f"{favourite_no} is my favourite number")

# QUESTION :10  Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write
# because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence
# describing what the program does.

# AUTHOR: ALEEZA SALEEM
# DATE 20/08/2024
def add(x,y):
    return x +y
res=add(2,7)
print(res)


# QUESTION:11 Names: Store the names of a few of your friends in a array called names. Print each person’s name by accessing each element in the list, one at a time.
friends_list=["Aleeza","Sadia","Zeba"]
print(friends_list[0])
print(friends_list[1])
print(friends_list[2])

# QUESTION12: Greetings: Start with the array you used in Exercise 11, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
friend_message="You are such best friend"
print(f"{friends_list[0]},{friend_message}")
print(f"{friends_list[1]},{friend_message}")
print(f"{friends_list[2]},{friend_message}")

# QUESTION13: Your Own Array: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transportation=["mercedes","land cruiser","onetwo-five"]
print(f"I would like to own a {transportation[0]}")
print(f"I would like to own a {transportation[1]}")
print(f"I would like to own a {transportation[2]}")

# QUESTION:14:Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

invited_guest=["Talha","Wajdan","Salaar"]
guest_message="You are invited to dinner"
print(f"{invited_guest[0]},{guest_message}")
print(f"{invited_guest[1]},{guest_message}")
print(f"{invited_guest[2]},{guest_message}")

# QUESTION:15 Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

print(f"{invited_guest[2]} can't make it to dinner")
invited_guest[2]="Yazdan"
print(f"{invited_guest[2]},{guest_message}")



# QUESTION:16 • Start with your program from Exercise 14. Add a print statement at the end of your program stating the name of the guest who can’t make it. • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. • Print a second set of invitation messages, one for each person who is still in your list.

print(f"{invited_guest[0]},{guest_message}")
print(f"{invited_guest[1]},{guest_message}")
print(f"{invited_guest[2]},{guest_message}")

# QUESTION 17: Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# • Start with your program from Exercise 16. Add a new line that prints a message saying that you can invite only two people for dinner.

# • Remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite them to dinner.

# • Print a message to each of the two people still on your list, letting them know they’re still invited.

# • Remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Sorry for that but due to less space i am inviting just two guests")
removed_guests= invited_guest.pop()
print(f"Sorry {removed_guests} you are not invited to dinner")
print(f"{invited_guest[0]} and {invited_guest[1]} {guest_message}")
removed_guests=invited_guest.pop()
removed_guests=invited_guest.pop()
print(f"{invited_guest}")

# QUESTION 18:Seeing the World: Think of at least five places in the world you’d like to visit.

# • Store the locations in a array. Make sure the array is not in alphabetical order.

# • Print your array in its original order.

# • Print your array in alphabetical order without modifying the actual list.

# • Show that your array is still in its original order by printing it.

# • Print your array in reverse alphabetical order without changing the order of the original list.

# • Show that your array is still in its original order by printing it again.

# • Reverse the order of your list. Print the array to show that its
# order has changed.

# • Reverse the order of your list again. Print the list to show it’s back to its original order.

# • Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.

# • Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# Step 1: Original array
countries = ["Australia", "Saudia", "UK", "USA", "Switzerland"]
print("Original order:", countries)

# Step 2: Print array in alphabetical order without modifying the original list
print("Alphabetical order:", sorted(countries))

# Step 3: Show that the array is still in its original order
print("Original order (unchanged):", countries)

# Step 4: Print array in reverse alphabetical order without modifying the original list
print("Reverse alphabetical order:", sorted(countries, reverse=True))

# Step 5: Show that the array is still in its original order
print("Original order (unchanged):", countries)

# Step 6: Reverse the order of the list
countries.reverse()
print("Reversed order:", countries)

# Step 7: Reverse the order of the list again
countries.reverse()
print("Original order restored:", countries)

# Step 8: Sort the array in alphabetical order
countries.sort()
print("Sorted in alphabetical order:", countries)

# Step 9: Sort the array in reverse alphabetical order
countries.sort(reverse=True)
print("Sorted in reverse alphabetical order:", countries)


# QUESTION 19. Dinner Guests: Working with one of the programs from Exercises 14 through 18, print a message indicating the number of people you are inviting to dinner.

num_of_guests= len(invited_guest)
print(f"\nNumber of people invited to dinner: {num_of_guests}")

# QUESTION 20. Think of something you could store in a array. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything  else you’d like. Write a program that creates a list containing these items.

arr_list=["rivers","mountains","cities","languages","lakes"]
print(arr_list)

# QUESTION 21. They think of something you could store in a TypeScript Object. Write a program that creates Objects containing these items.

object_list={
    "rivers","mountains","cities","languages","lakes"
}
print(object_list)

# QUESTION 22. Intentional Error: If you haven’t received an array index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

index_err=[0,1,2,3]
# print(index_err[6])
print(index_err)

# QUESTION 23. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

# let car = 'subaru';

# console.log("Is car == 'subaru'? I predict True.")

# console.log(car == 'subaru')

# • Look closely at your results, and make sure you understand why each line evaluates to True or False.

# • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.


# TEST 1
x=2
y=3
print("Is x is greater than y ? I predict false")
print(x>y)
# TEST 2
print("Is x is smaller than y ? I predict true")
print(x<y)
# TEST 3
print("Is x is smaller than and equal to y ? I predict false")
print(x>=y)
# TEST 4
print("Is x is greater  than and equal to y ? I predict true")
print(x<=y)
# TEST 5
print("Is x is not equal to y? I predict true")
print(x!=y)
# TEST 6
print("Is x is equal to? I predict false")
print(x==y)
# TEST 7
print("Is x equals to 2 and  y=3  ?, I predict true")
print(x==2 and y==3)
 
# TEST 8
print("Is x equals to 2 and  y=4  ?, I predict false")
print(x==2 and y==4)

# TEST 9
print("Is x equals to 2 or  y=4  ?, I predict true")
print(x==2 or y==4)

# TEST 10
print("Is x equals to 1 or  y=4  ?, I predict false")
print(x==1 or y==4)

# QUESTION 24. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests. Have at least one True and one False result for each of the following:

# • Tests for equality and inequality with strings

# • Tests using the lower case function

# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

# • Tests using "and" and "or" operators

# • Test whether an item is in a array

# • Test whether an item is not in a array

# Test 11
str1="apple"
str2="mango"
print("Is str1 is equal to str2? I predict false")
print(str1==str2)
# TEST 12
print("Is str1 is equal to str2 ignoring data types? I predict false")
print(str1.lower()==str2.lower())
# TEST 13
p=1
q=2
print("Is p is greater than q ? I predict false")
print(p>q)
# TEST 14
print("Is p is smaller  than q ? I predict true")
print(p<q)
# TEST 15 
print("Is p is greater than and equal to q ? I predict false")
print(p>=q)
# TEST 16 
print("Is p is smaller than and equal to  q ? I predict true")
print(p<=q)
# TEST 17 
print ("Is p=1 and q=2? I predict true")
print(p==1 and q==2)
# TEST 18
print ("Is p=1 or q=3? I predict true")
print(p==1 or q==2)
# TEST 19
fruits = ["kiwi", "papaya", "apple"]
print("Is 'kiwi' in the list? I predict True")
print('kiwi' in fruits)  # True
print("Is 'banana' not in the list? I predict True")
print('banana' not in fruits)  # True


# QUESTION 25:25. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.

# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

alien_color="green"
if(alien_color=="green"):
    print("you earned 5 points")
else:
    print("failed!!!!!!!!")
alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points")
else:
    print("Failed!!!!!!!!")

# QUESTION 26:Alien Colors #2: Choose a color for an alien as you did in Exercise 25, and write an if-else chain.

# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.

# • Write one version of this program that runs the if block and another that runs the else block.
if(alien_color=="green"):
    print("you got 5 points")
else:
    print("you got 10 points")
# Alien Color that triggers the else block
alien_color = "yellow"
if(alien_color=="green"):
    print("you got 5 points")
else:
    print("you got 10 points")

# QUESTION 27: Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-else chain.

# • If the alien is green, print a message that the player earned 5 points.

# • If the alien is yellow, print a message that the player earned 10 points.

# • If the alien is red, print a message that the player earned 15 points.

# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

# Alien Color that triggers the "green" condition
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
elif alien_color == "red":
    print("You earned 15 points.")
else:
    print("Alien color not recognized.")

# Alien Color that triggers the "yellow" condition
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
elif alien_color == "red":
    print("You earned 15 points.")
else:
    print("Alien color not recognized.")

# Alien Color that triggers the "red" condition
alien_color = "red"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
elif alien_color == "red":
    print("You earned 15 points.")
else:
    print("Alien color not recognized.")


# QUESTION 28. Stages of Life: Write an if-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

# • If the person is less than 2 years old, print a message that the person is a baby.

# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.

# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.

# • If the person is age 65 or older, print a message that the person is an elder.

age= 30
if(age<2):
    print("The person is a baby.")
elif 2<=age <4:
    print("The person is a toddler.")
elif 4<=age <13:
     print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


# QUESTION 29:Favorite Fruit: Make a array of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your array.

# • Make a array of your three favorite fruits and call it favorite_fruits.

# • Write five if statements. Each should check whether a certain kind of fruit is in your array. If the fruit is in your array, the if block should print a statement,
# such as You really like bananas!

fvrt_fruit=["Mango","watermelon","guava"]
if("Mango" in fvrt_fruit):
    print("Mango is my favourite fruit")
if "watermelon" in fvrt_fruit:
    print("Watermelon is my favorite fruit.")
if "guava" in fvrt_fruit:
    print("Guava is my favorite fruit.")


# QUESTION30. Hello Admin: Make a array of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the array, and print a greeting to each user:

# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?

# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.


usernames = ["admin", "talha", "wajdan", "yazdan", "salaar"]

# Loop through each username in the array
for username in usernames:
    if username == "admin":
        # Special greeting for the admin
        print("Hello admin, would you like to see a status report?")
    else:
        # Generic greeting for other users
        print(f"Hello {username}, thank you for logging in again.")

# QUESTION 32. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

# • Make a list of five or more usernames called current_users.

# • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.

# • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying that the username is available.

# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

# Define the list of current usernames
current_users = ["sadaf", "zeba", "sadia", "erum", "aleeza"]

# Define the list of new usernames
new_users = ["tahir", "gulfam", "abrar", "humair", "talha"]

# Convert current users list to lowercase for case insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new user
for new_user in new_users:
    # Convert new user to lowercase for case insensitive comparison
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")





