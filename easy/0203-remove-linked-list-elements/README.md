# Remove Linked List Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 
Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Example 2:

Input: head = [], val = 1
Output: []


Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


 
Constraints:


	The number of nodes in the list is in the range [0, 104].
	1 <= Node.val <= 50
	0 <= val <= 50

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-09-05T13:20:58.043Z  

```py
class Solution:
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = self.getNext(n)

        while slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return slow == 1

    def getNext(self, n):
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total
```

---

[View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)