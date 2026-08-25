import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate all values so heapq (min-heap) behaves like a max-heap
        temp = [-s for s in stones]
        heapq.heapify(temp)

        while len(temp) > 1:
            x = -heapq.heappop(temp)  # largest stone
            y = -heapq.heappop(temp)  # second largest stone
            rem = x - y
            if rem > 0:
                heapq.heappush(temp, -rem)  # push leftover back in

        return -temp[0] if temp else 0