# Count Special Quadruplets

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:


	nums[a] + nums[b] + nums[c] == nums[d], and
	a < b < c < d


 
Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.


Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].


Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5


 
Constraints:


	4 <= nums.length <= 50
	1 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-08-23T10:31:49.580Z  

```py
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        r=[]
        for i in range(len(nums)):
            if i>0 and  nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        r.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and  nums[left]==nums[left-1]:
                            left+=1
                        while left<right and  nums[right]==nums[right+1]:
                            right-=1
                        
                    elif s<target:
                        left+=1

                    else:
                        right-=1

        return r
```

---

[View on LeetCode](https://leetcode.com/problems/count-special-quadruplets/)