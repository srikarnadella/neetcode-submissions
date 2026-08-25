class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in data:
                data[temp].append(word)
            else:
                data[temp] = [word]
        
        return list(data.values())