class Solution:
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while fast != 1:

            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

            if slow == fast:
                return False

        return True

    def getNext(self, n):
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        return total