class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        for num, cnt in count.items():
            buckets[cnt].append(num)
        
        res = []
        ind = len(buckets) - 1
        while len(res) < k:
            if len(buckets[ind]) != 0:
                res.append(buckets[ind].pop())
         

            if len(buckets[ind]) == 0:
                ind-=1
            

        return res