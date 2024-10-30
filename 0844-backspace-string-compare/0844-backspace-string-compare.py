class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_stack, t_stack = [], []
        
        for c in s:
            if c == "#":
                s_stack and s_stack.pop()
            else: 
                s_stack.append(c)
        
        for c in t: 
            if c == "#":
                t_stack and t_stack.pop()
            else: 
                t_stack.append(c) 
                
        if s_stack == t_stack:
            return True
        else: 
            return False
        