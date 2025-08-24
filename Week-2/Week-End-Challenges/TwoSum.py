'''Q :
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], targ '''

# o(n^2) : Brute Force
def findIndexofTwoSum(lst,target):
    
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                return [i,j]
    
    return ""

# O(n) : Hash Map
def TwoSum(lst,target):
    seen = {}
    for i,num in enumerate(lst):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num]=i
    return []

lst = [2,7,11,15]
target=9

print(findIndexofTwoSum(lst,target))

print(TwoSum(lst,target))
