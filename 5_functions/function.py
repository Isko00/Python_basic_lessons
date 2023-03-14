def print_hello():
    print("Hello from a function")


print_hello()


def print_greeting(fname):
    print("Hello, " + fname + '!')


print_greeting("Emil")
print_greeting("Roza")
print_greeting("Aruzhan")


def select_second_from_tuple(*kids):
    print("The youngest child is " + kids[2])


select_second_from_tuple("Emil", "Tobias", "Linus")


def select_last_name_from_dictionary(**kid):
    print("His last name is " + kid["lname"])


select_last_name_from_dictionary(fname="Islam", lname="Ospanov")


def print_i_am_from_countryname(country = "Norway"):
    print("I am from " + country)


print_i_am_from_countryname("Sweden")
print_i_am_from_countryname("India")
print_i_am_from_countryname()
print_i_am_from_countryname("Brazil")


def print_food_list(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

print_food_list(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
