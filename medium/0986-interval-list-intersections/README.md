# Interval List Intersections

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 
Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []


 
Constraints:


	0 <= firstList.length, secondList.length <= 1000
	firstList.length + secondList.length >= 1
	0 <= starti < endi <= 109
	endi < starti+1
	0 <= startj < endj <= 109 
	endj < startj+1

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-05T08:41:03.726Z  

```py
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                # Face-up: spend power, gain score
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)

            elif score > 0:
                # Face-down: spend score, gain power
                power += tokens[right]
                right -= 1
                score -= 1

            else:
                break

        return max_score
```

---

[View on LeetCode](https://leetcode.com/problems/interval-list-intersections/)