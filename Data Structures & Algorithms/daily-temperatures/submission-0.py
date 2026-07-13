class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        sol=[0]*n       
        stack = []
        for i,v in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((v,i))
                continue
            while stack and v > stack[-1][0]:
                sol[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append((v,i))
        return sol
