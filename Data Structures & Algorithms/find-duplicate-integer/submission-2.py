class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = {}
        for num in nums:
            if num in temp:
                return num
            else:
                temp[num] = True
        return -1