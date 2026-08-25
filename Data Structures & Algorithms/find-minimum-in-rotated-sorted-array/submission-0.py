class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        runningMin = min(nums[l], nums[r])
        while l <= r:
            mid = (r - l) // 2
            print(nums[l],nums[mid],nums[r])
            runningMin = min(runningMin, nums[l], nums[r], nums[mid])
            print("running min", runningMin)
            if nums[r] < nums[mid]:
                l = mid + 1
                r -=1
            elif nums[l] > nums[mid]:
                l+=1
                r = mid - 1
            else:
                l+=1
                r-=1
        return runningMin

        