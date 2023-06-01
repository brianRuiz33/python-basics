""" 
Python 101
Topics: Variables, loops
"""

# User
name = "Jake"
last_name = "peralta"
age = 34
is_detective = True
salary = 1349.56
friends = ["Amy Santiago", "Charles Boyle", "Rosa Diaz", "Terry Cruz"]


def say_hello(name):
    print(f"Hello {name}")


def is_under_age(age):
    min_age = 21

    if age < min_age:
        return True

    return False


def count_friends(friends):
    counter = 0
    for friend_name in friends:
        counter += 1

    return counter


friends_count = len(friends)

stop = False
# Pip8
