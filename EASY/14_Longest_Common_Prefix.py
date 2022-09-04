class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        
        for i in zip(*strs):
            if len(set(i)) == 1:
                index += 1
            else:
                break
        
        return strs[0][:index]