list_of_values = ['a', 'b', 'c', 'd', 'e']

# loop from 1 ..(n=5) O(n)
def function1(values):
  for value in values:
    print(value)

# no loop O(1)
def function2(values):
  print(values[0])
  print(values[1])

# O(n^2)
def function3(values):
  for x in values:
    for y in values:
      print(x, y)

# O(n)
def function4(values):
  for i in range(4):
    print("Python is great")

  # O(1)
  print("Software Engineering is awesome!")
  print("Software Engineering is awesome!")
  
  for value in values:
    print(value)

  for value in values:
    print(value)

# # It may be helpful to comment out all of the functions beside the function you are focusing on. This can help with determining the output of the function you are analyzing.

function1(list_of_values)
function2(list_of_values)
function3(list_of_values)
function4(list_of_values)

# O(n)
def function5(n):
  test_list=[]

  for num in range(n):
    test_list.append('add me')

  return test_list

print(function5(3))


def sum_of_list(numberedList):
  listSum = 0
  for i in numberedList:
    listSum = listSum + i
  return listSum

print(sum_of_list([1,4,3]))

# O(n) time complexity