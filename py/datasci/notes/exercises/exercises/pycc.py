# Python Crash Course Exercises

# 1. What is 7 to the power of 4?

# print(7 ** 4)

# 2. Split the string 
# s = "Hi there Sam!"
# into a list

# print(s.split())

# 3.  Given the variables 
# planet = "Earth"
# diameter = 12742
# Use .format() to print the following string:"
# "The diameter of Earth is 12472 kilometers"

# the_string = "The diameter of {} is {} kilometers.".format(planet, diameter)
# print(the_string)

# Given this nested list, use indexing to grab the word "hello" 

# first = [1, 2 , [3,4], [5, [100, 200, ["hello"]] ,23, 11], 1, 7]
# print(first[3][1][2][0])

# Given this nest dictionary grab the word "hello". Be prepared, this will be annoying and tricky.

# d = {'k1': [1,2,3, {'tricky': ['oh', 'man', 'inception', {'target': [1,2,3, "hello"]} ] } ]}

# print(d['k1'][3]['tricky'][3]['target'][3])

# What is the main difference between a tuple and a list

# A tuple is immutable while a list is mutable; that is, the elements of a list can be reassigned while the elements of a tuple cannot.

# Create a function that grabs the email website domain from a string in the form:
# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com

# string_domain = "user@domain.com"


# def domainGet (x):
#     domain_string = x.split("@") 
#     return domain_string[1]

# print(domainGet(string_domain))


# Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitilization.

# def is_dog (x):
#     search_string = x.split()
#     for i in range(len(search_string)):
#         if (search_string[i] == "dog" or search_string[i] == "Dog"):
#             return True
#         else:
#             return False

# test_string = "The quick brown fox jumps over the lazy dog"
# print(is_dog(test_string))

# Some edge cases include "dog" written in all upper case or "dog" with puncuation.


# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore the edge cases.

# def countDog (x):
#     search_string = x.split()
#     dog = 0
#     for i in range(len(search_string)):
#         if (search_string[i] == "dog"):
#             dog +=1
#     return dog

# test_str = "This dog runs faster than the other dog dude!"

# print(countDog(test_str))


# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's', For example:
# seq = ['soup', 'dog', 'salad', 'cat', 'great'] 

# filter(function or lambda expression, list_in)


# list_out = list(filter(lambda x: x[0] == "s", seq))


# print(list_out)


# You are driving a little too fast, and a police officer stops you. Write a function to return one odf 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If sped is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is you birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

# If speed < 60 then "No ticket"

# If 61 <= speed  <= 80, then "Small ticket"

# If speed >=81, then "Big Ticket"


def caught_speeding (speed, is_birthday):
    if (is_birthday != True):
        if (speed < 60):
            return "not ticket"
        elif (speed >= 61 and speed <= 80):
            return "Small ticket"
        else:
            return "Big ticket"
    else:
        if (speed < 65):
            return "not ticket"
        elif (speed >= 66 and speed <= 85):
            return "Small ticket"
        else:
            return "Big ticket"

# print(caught_speeding(81,False))

