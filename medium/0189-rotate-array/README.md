# Rotate Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


 
Constraints:


	1 <= nums.length <= 105
	-231 <= nums[i] <= 231 - 1
	0 <= k <= 105


 
Follow up:


	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
	Could you do it in-place with O(1) extra space?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-09-05T07:54:51.333Z  

```py
class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0
        while read<len(chars):
            current= chars[read]
            count=0
            while read<len(chars) and chars[read]==current:
                read+=1
                count+=1

            chars[write]=current
            write+=1

            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write
```

---

[View on LeetCode](https://leetcode.com/problems/rotate-array/)