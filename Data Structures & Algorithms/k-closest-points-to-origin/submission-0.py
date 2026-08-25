import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        distoutput = []
        heapq.heapify(distoutput)
        for coord in points:
            heapq.heappush(distoutput,[self.distance(coord), coord])
        print(distoutput)
        for _ in range(k):
            temp = heapq.heappop(distoutput)
            print(temp)
            output.append(temp[1])
        return output
    
    def distance(self, point: List[int]) -> int:
        return math.sqrt((point[0])**2 + (point[1])**2)