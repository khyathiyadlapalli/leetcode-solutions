# Palindrome Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 
Example 1:

Input: head = [1,2,2,1]
Output: true


Example 2:

Input: head = [1,2]
Output: false


 
Constraints:


	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9


 
Follow up: Could you do it in O(n) time and O(1) space?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-09-05T12:55:24.896Z  

```py
            while right:
                if left.val!=right.val:
                
                    return False
            return True
                left.next
                right.next

```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/)