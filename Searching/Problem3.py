# Is there any alternative way of solving problem 1
# HashMap

#Time Complexity : O(n)
#Time Complexity : O(n)

def check_duplicate_hash(nums):
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            print("Duplicate  exists in the givern array",i)

    print("No duplicate")


check_duplicate_hash([34,98,7,6,23,1000])
check_duplicate_hash([34,98,7,6,23,34,1000])