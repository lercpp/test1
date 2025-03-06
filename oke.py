def find_greater(arr, value):
    a=[]
    for i in range(len(arr)):
        if arr[i]>=value:
            a.append(arr[i])
    return a

def filter_less(arr, value):
    a=[]
    for i in range(len(arr)):
        if arr[i]<value:
            a.append(arr[i])
    return a

def filter_equal(arr, value):
    a=[]
    for i in range(len(arr)):
        if arr[i]==value:
            a.append(arr[i])
    return a
def filter_not(arr, value):
    a=[]
    for i in range(len(arr)):
        if arr[i]!=value:
            a.append(arr[i])
    return a

def test():
    test_array = [1,2,3,4]

    print(find_greater(test_array,3))
    print(filter_less(test_array, 4))
    print(filter_equal(test_array, 5))
    print(filter_not(test_array, 6))

def matri(x):
    a=x[0][0]+x[1][0]+x[1][1]+x[2][0]+x[2][1]+x[2][2]
    print(a)