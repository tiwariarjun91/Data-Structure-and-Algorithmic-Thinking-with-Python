def orderedLinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i]>target:
            return -1
    return -1

def orderedLinearSearch2(arr,target):
    for i in range(0,len(arr),2):
        if arr[i] == target:
            return i
        if arr[i]>target:
            if arr[i-1] == target:
                return i-1
            else:
                return -1
    return -1


arr = [1,2,3,4,5,6,7,8,9,10]

print(orderedLinearSearch(arr,5))
print(orderedLinearSearch(arr,150))
print(orderedLinearSearch2(arr,6))
print(orderedLinearSearch(arr,100))