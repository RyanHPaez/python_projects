#1-----------------------------------------------------------------------

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))

#2-----------------------------------------------------------------------

def flatten_and_sort2(array):
    item = []
    for y in array:
        for x in y:
            item.append(x)    
    item.sort()
    return item

list_2 = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original flatten 1 List', list_2)
print('Transformed sorted 1 Flat List', flatten_and_sort2(list_2))

#3---------------------------------------------------------------------

def flatten_and_sort3(array):
    newList = []
    for item in array:
        newList += item
    return sorted(newList)

list3 = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original flatten 2 List', list3)
print('Transformed sort 2 Flat List', flatten_and_sort3(list3))

#4----------------------------------------------------------------------

def flatten_and_sort4(array):
    return sorted([j for i in array for j in i])

list4 = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original flatten 4 List', list4)
print('Transformed sort 4 Flat List', flatten_and_sort4(list4))

#solution--------------------------------------------------------------

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

solution_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('solution List', solution_list)
print('Transformed Flat solution List', flatten_and_sort(solution_list))
