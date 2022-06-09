

def binary_search (arr,start,end,i):
    if end>=start:
        mid=(end+start)//2
        if arr[mid]==i:
            return "Element present at Index {}".format(mid)
        elif arr[mid]>i:
            return binary_search(arr,start,mid-1,i)
        else:
            return binary_search(arr,mid+1,end,i)
    else:
        return 'Element not Present in Array'

#Lets Check with an Examples
arr=[2,3,4,10,40]
print(binary_search(arr, 0, len(arr)-1, 2))

print(binary_search(arr, 0, len(arr)-1, 3))

print(binary_search(arr, 0, len(arr)-1, 10))


