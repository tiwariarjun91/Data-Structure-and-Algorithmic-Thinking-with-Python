# reducing space complexity after problem 3

def check_duplicate_negation(arr):
    for i in range(0,len(arr)):
        if arr[abs(arr[i])] < 0:
            print("Duplicate Exists")
            return
        else:
            arr[[arr[i]] = -1 * arr[arr[i]]

    print("No Duplicate number exists in this array")

arr = [3,2,1,2,2,3]
check_duplicate_negation(arr)
check_duplicate_negation([2,3,6,1,5,4,7,8,8,0])