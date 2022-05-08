#Time Complexity: O(n)
#Space Complexity: O(1)



def unOrderedLinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1,12,46,5,6,70,8,9]
print(unOrderedLinearSearch(arr,5))
print(unOrderedLinearSearch(arr,10))