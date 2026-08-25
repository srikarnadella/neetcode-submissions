class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        for ind, val in enumerate(nums):
            twoSum[val] = ind
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in twoSum and twoSum[diff] != ind:
                return [ind, twoSum[diff]]