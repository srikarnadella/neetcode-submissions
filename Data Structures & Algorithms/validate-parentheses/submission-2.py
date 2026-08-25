class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {"[": "]", "{":"}", "(": ")"}
        for char in s:
            if char in key:
                stack.append(key[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return not stack