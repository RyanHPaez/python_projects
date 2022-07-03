# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)


input_num = int(input("Enter the number of rows: "))
list = [] #an empty list
for n in range(input_num):
    list.append([])
    list[n].append(1)
    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])
    if(input_num != 0):
        list[n].append(1)
for n in range(input_num):
    print(" " * (input_num - n), end = " ", sep = " ")
    for m in range(0, n + 1):
        print('{0:5}'.format(list[n][m]), end = " ", sep = " ")
    print()