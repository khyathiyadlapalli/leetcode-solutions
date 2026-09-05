# Linked List Cycle

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 
Constraints:


	The number of the nodes in the list is in the range [0, 104].
	-105 <= Node.val <= 105
	pos is -1 or a valid index in the linked-list.


 
Follow up: Can you solve it using O(1) (i.e. constant) memory?

## Solution

**Language:** Python  
**Runtime:** 53 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-05T11:19:06.968Z  

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            area=width*h
            max_area=max(area,max_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
```

---

[View on LeetCode](https://leetcode.com/problems/linked-list-cycle/)