class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        su=0
        for i in range(0,len(nums)):
            for j in range(i+1,(len(nums))):
                su= nums[i]+nums[j]
                if su==target:


                    return [i,j]
        