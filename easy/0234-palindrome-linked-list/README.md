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
**Runtime:** 40 ms (beats 36.37%)  
**Memory:** 42.6 MB (beats 54.09%)  
**Submitted:** 2026-09-05T13:00:36.355Z  

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

[View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/)