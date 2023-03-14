print((lambda a, b: a if a > b else b)(25, 17))


def greater(a, b):
    if a > b:
        return a
    else:
        return b


print(greater(25, 17))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x % 2, my_list))

print(new_list)


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# a function that returns True if letter is vowel
def filter_vowels(in_letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return in_letter in vowels


filtered_vowels = filter(filter_vowels, letters)


# converting to tuple
print(tuple(filtered_vowels))
