import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def random_array(a,b,c):
    arr = []
    for i in range(a):
        arr.append(random.randint(b, c))
    return arr

def read_file(a):
    file = open( a + ".txt", "r")
    data = file.read()
    file.close()
    array = eval(data)
    arr = convert_to_list(array)
    return arr

def write_file(a, arr):
    file = open(a + ".txt", "w")
    arr_str = str(arr)
    file.write(arr_str)
    file.close()

def convert_to_list(arr):
    lst = []
    for elem in arr:
        lst.append(elem)
    return lst