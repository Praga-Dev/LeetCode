class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for c in s:
            if c not in braces:
                stack.append(c)
            elif not stack or stack.pop() != braces[c]:
                return False
        
        return True