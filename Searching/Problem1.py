#Given an array of n numbers, give an algorithm for checking whetehr there are any duplicate elements in the array or no?

#Time Complexity : O(n^2)
#Space Complexity : O(1)


def check_duplicate_brute_force(nums):
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                print("Duplicate numbers exist ",nums[i])
                return
    print("No duplicates in the given array")


check_duplicate_brute_force([1,2,3,4,5,6,7,8,9])
check_duplicate_brute_force([1,2,3,4,5,5,6,7,8,9])