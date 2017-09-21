
#1 - Assigning an integer to a variable
x = 11

#2 - Assigning a string to a variable
introductions = ("Let's have fun with these numbers:")

#3 - Assigning a float to a variable
y = float(1.33)

#4 - Using the print function and .format() notation to print my variables
print '{} {} and {}'.format(introductions,x,y)

#5 - Using the operators: +,-,*,/,+=,=,% - in that order
print '\nx plus y is:' 
print (x+y)
print '\nx minus y is:'
print (x-y)
print '\nx times y is:'
print (x*y)
print '\nx divided by y is:'
print (x/y)
print '\ny increased by .67 is:'
y += float(.67)
print y
remainder = (x%y)
print '\nThe remainder of x divided by y is:'
print remainder

#6 - Using the logical operators: and, or, not - in that order

print '\nx plus 1, y plus 10, and x plus y minus 1 are all equal to:'
same = (x + 1) and (y + 10) or (x + y - 1)
anyOtherNumber = (not same)
print same

#7 - Using the conditional statements: if, elif, else - in that order

print "\nLet's just double check to be sure...  was that last statement True or false?"
if same == 12:
    print True

print "\nMore comparisons could be helpful... Is a new variable, z, more or less than 12?"
z = 12

if z > same:
    print '\nz is more than 12'

elif z == same:
    print '\nz is actually 12!'

else:
    print '\nz has to be less than 12'

#8 - Use of a while loop

print "\nI'm really into this 12 thing right now.  Let's count to 12 to celebrate!"

counter = 0

while counter <= same:
    print counter
    counter = counter+1

#9 - Use of a for loop

print "\nGosh, that was so much fun I think we need to do it again!"

for counter in range (0,13):
    print counter

#10 - Creating a list and iterating through it with a for loop to print each item on a new line

print "\nHere's a short list of some movies that have twelve, or dozen, in the title:"

movie_titles_with_12_list = ["Twelve Monkeys", "Ocean's Twelve", "The Dirty Dozen", "Cheaper by the dozen"]

for titles in movie_titles_with_12_list:
    print titles

#11 - Creating a tuple and iterating through it with a for loop to print each item on a new line

print "\nWhat order were they released in though?"

my_movie_tuple = ("The Dirty Dozen", 1967,
                  "Twelve Monkeys", 1995,
                  "Cheaper by the Dozen", 2003,
                  "Ocean's Twelve", 2004)

for movie in my_movie_tuple:
    print movie

#12 - Defining a function that returns a string variable

def bakersDozen(x,y):
    addition = (x + y)
    print ("\nOddly enough, there is a well known example of a dozen not being equal to 12. \nA baker's dozen is actually equal to:")
    print addition

#13 - Calling the defined function above and printing the result to the shell

print"\nAre there any examples where a dozen isn't 12?"
answer = raw_input('\nType "y" for yes and "n" for no.')
if answer == "y":
    print "\nYou are correct!"
    bakersDozen(x,y)
    
elif answer == "n":
    print "\nYou are mistaken."
    bakersDozen(x,y)

else:
    print '\nThe key you typed was not "y" or "n", but you should still know the truth...'
    bakersDozen(x,y)
    
    


