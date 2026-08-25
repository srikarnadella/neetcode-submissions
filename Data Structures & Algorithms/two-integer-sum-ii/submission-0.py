class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftInd = 0
        rightInd = len(numbers) - 1

        while leftInd < rightInd:
            total = numbers[leftInd] + numbers[rightInd]
            if total < target:
                leftInd+=1
            elif total > target:
                rightInd -=1
            else:
                return [leftInd  + 1, rightInd + 1]
        