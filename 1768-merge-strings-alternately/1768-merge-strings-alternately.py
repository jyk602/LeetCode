class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
#         # Solution 1
#         output = [] 
#         i, j = 0, 0
        
#         while i < len(word1) and j < len(word2):
#             output.append(word1[i])
#             output.append(word2[j])
#             i += 1
#             j += 1 
        
#         output.append(word1[i:])
#         output.append(word2[j:])
#         return "".join(output)
    
    
        ############
        
        # Solution 2 
        res = "" 
        i ,j = 0, 0
        
        while i < len(word1) and j <len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1 
            
        res += word1[i:] + word2[j:]
        return res 
    
    