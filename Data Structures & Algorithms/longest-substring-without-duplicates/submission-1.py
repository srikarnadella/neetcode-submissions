class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0 ,1
        runningCount = 1
        curr = {s[0]: 0}
        while r < len(s):
            if s[r] in curr and curr[s[r]] >= l:
                l = curr[s[r]] + 1
                curr[s[r]] = r
            else:
                curr[s[r]] = r
            runningCount = max(runningCount, r - l + 1)
            r += 1
        return runningCount
            