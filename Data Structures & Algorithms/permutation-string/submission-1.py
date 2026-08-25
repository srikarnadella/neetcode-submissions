from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        print("Target", s1Count)
        for i in range(len(s2) - len(s1) + 1):
            print("I", i)
            tempCount = Counter(s2[i:i+len(s1)])
            print(tempCount)
            if tempCount == s1Count:
                return True
        
        return False

        