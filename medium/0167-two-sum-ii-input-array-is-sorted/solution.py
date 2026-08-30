class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)-1):
                if numbers[i]+numbers[j]==0:
                    return[i,j]
        
