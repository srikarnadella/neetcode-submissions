class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)// 2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif target > nums[mid]:
                l = mid
                r = r - 1
            elif target < nums[mid]:
                r = mid
                l = l + 1
            else:
                return mid
        return -1