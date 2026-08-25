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
**Runtime:** 520 ms (beats 28.04%)  
**Memory:** 19.2 MB (beats 89.42%)  
**Submitted:** 2026-08-25T15:48:57.121Z  

```py
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):

                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1

        return count
```

---

[View on LeetCode](https://leetcode.com/problems/count-special-quadruplets/)