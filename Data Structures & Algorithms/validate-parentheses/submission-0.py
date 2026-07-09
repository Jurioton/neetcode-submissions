class Solution:
    def oppbrac(self, s: str) -> str:
        if s == ']':
            return '['
        if s == '}':
            return '{'  
        if s == ')':
            return '('  

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('[','{','('):
                stack.append(i)
                continue
            if not stack:
                return False
            
            x= stack.pop()
            if self.oppbrac(i) != x:
                return False           
        return not stack 