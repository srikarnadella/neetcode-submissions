class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        print(nums)

        for ind, val in enumerate(nums):
            target = -val
            if ind < len(nums) - 1:
                l, r = ind + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == -val:
                        temp = [val, nums[l], nums[r]]
                        output.add(tuple(temp))
                        r-=1
                        l+=1
                    elif nums[l] + nums[r] > -val:
                        r-=1
                    elif nums[l] + nums[r] < -val:
                        l+=1

        return list(output)