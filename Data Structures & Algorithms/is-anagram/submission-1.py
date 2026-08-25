class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}
        for char in s:
            if char in temp:
                temp[char]+=1
            else:
                temp[char] = 1
        othertemp = {}
        for char in t:
            if char in othertemp:
                othertemp[char]+=1
            else:
                othertemp[char] = 1
        
        return temp == othertemp
        