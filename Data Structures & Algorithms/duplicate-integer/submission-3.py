class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bank = set()
        for n in nums:
            if n in bank:
                return True
            bank.add(n)
        return False
        