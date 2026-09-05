# Happy Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:


	Starting with any positive integer, replace the number by the sum of the squares of its digits.
	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
	Those numbers for which this process ends in 1 are happy.


Return true if n is a happy number, and false if not.

 
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Example 2:

Input: n = 2
Output: false


 
Constraints:


	1 <= n <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-05T13:14:07.865Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        left=head
        right=prev
        while right:
            if left.val!=right.val:
                
                return False
            left=left.next
            right=right.next
        return True

        
```

---

[View on LeetCode](https://leetcode.com/problems/happy-number/)