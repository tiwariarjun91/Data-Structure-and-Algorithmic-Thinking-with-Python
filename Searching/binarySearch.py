#Time Complexity  : O(logn)
#Space Complexity : O(1) // only for the iterative approach


#Binary Search Iterative

def binarySearchIterative(nums, target):
    low = 0
    high = len(nums)-1

    while(low<=high):
        mid = low + (high-low)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid]>target:
            high = mid -1
        else:
            low = mid + 1
    return -1


#Binary Search Recursive

def binarySearchRecursive(nums , low, high, target):
    if high == -100:
        high = len(nums) -1

    if low <= high:
        mid = low + (high - low) //2
        # if low == high:
        #     if nums[low] == target:
        #         return low
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
           return binarySearchRecursive(nums,low,mid-1,target)
        else:
           return binarySearchRecursive(nums,mid+1,high,target)
    return -1


arr = [1,2,3,4,5,6]

print(binarySearchIterative(arr,5))
print(binarySearchIterative(arr,10))
print(binarySearchRecursive(arr,0,-100,5))
print(binarySearchRecursive(arr,0,-100,10))
