class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftInd = 0
        rightInd = len(s) - 1
        
        while leftInd < rightInd:
            print("Left ind vs right ind", s[leftInd], "Space", s[rightInd])
            if not (s[leftInd].isalnum()):
                leftInd+=1
                continue
            if not (s[rightInd].isalnum()):
                rightInd-=1
                continue
            if s[leftInd].lower() == s[rightInd].lower():
                leftInd+=1
                rightInd-=1
                print("good)")
            else:
                return False
        
        return True
        