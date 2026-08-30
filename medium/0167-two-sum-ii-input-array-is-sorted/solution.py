class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return[i,j]
        
