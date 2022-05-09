# Can we improve the time complexity of Problem 1's solution:

def check_duplicates_sorting(nums):
    nums.sort()

    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            print("Duplicate number exists", nums[i])

    print("No duplicate number in the given array")

check_duplicates_sorting([34,98,7,6,23,1000])
check_duplicates_sorting([34,98,7,6,23,34])