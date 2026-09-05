# 4Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:


	0 <= a, b, c, d < n
	a, b, c, and d are distinct.
	nums[a] + nums[b] + nums[c] + nums[d] == target


You may return the answer in any order.

 
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


 
Constraints:


	1 <= nums.length <= 200
	-109 <= nums[i] <= 109
	-109 <= target <= 109

## Solution

**Language:** Python  
**Runtime:** 406 ms (beats 35.10%)  
**Memory:** 19.5 MB (beats 7.49%)  
**Submitted:** 2026-09-05T09:26:56.883Z  

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

[View on LeetCode](https://leetcode.com/problems/4sum/)