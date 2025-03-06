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