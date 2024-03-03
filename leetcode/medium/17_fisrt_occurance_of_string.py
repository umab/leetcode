class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

    
        #len(haystack) - len(needle + 1)
        # no point in starting to look for substr when haystack is left with chars < needle
        # +1 to include last location
    
        for i in range(len(haystack) - len(needle) + 1): 
            if haystack[i: i+len(needle)] == needle: # check if substr from i->i+len(needle) == needle
                return i
        return -1 
            

