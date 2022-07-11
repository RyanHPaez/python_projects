from ast import Expression
from typing import Iterable


m = (list(map(lambda state: state.capitalize(), ['washington', 'alaska'])))
print(m)

print(list(map(lambda state: state.capitalize(), ['washington', 'alaska'])))

divisible = {num for num in range (10) if num % 2 == 0}
print(divisible)

double = {num: num * 2 for num in range(4) if num % 1 == 0}
print (double)

squares = [num*num for num in range(5)]
print(squares)

perimeter = lambda side_length: 4*side_length
print(perimeter(2))

area = lambda length, width: length * width
print(area(5,5))

def area (length,width):
    return length * width
print(area(5,5))


alpha = 'abcjkbhlgugiulgiluegav'
my_lst = [alpha[i] for i in range (10 ) ]
my_lst = [ele for ele in alpha if alpha.index(ele)]
print(my_lst)


names = ['Alice', 'Bob', 'Charlie']
my_dict = {ele: ele.upper() for ele in names}
print(my_dict)

# Problem 1: Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.

grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

# Problem 2: Write a lambda function to cube every element of a list

cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2]))

#Problem 3: Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.

even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

# Problem 4: Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).

nums = [i for i in range(1,101)]
print(nums)

# Problem 5: Use a dictionary comprehension to count the length of each word in a sentence.

sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})