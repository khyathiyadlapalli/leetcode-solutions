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