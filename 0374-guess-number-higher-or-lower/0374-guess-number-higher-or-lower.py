# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the range
        l, r = 1, n 
        
        # Binary Search
        while True: 
            m = (l + r) // 2    # Calculate middle of the range
            res = guess(m)      # Get feedback from the API
            if res > 0:
                l = m + 1 
            elif res < 0:
                r = m - 1 
            else:
                return m
            
            
