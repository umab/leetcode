class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)  # this returns {a:3, b:5, c...} blah

        for i in range(len(s)):
            if s[i] in right:
                right[s[i]] -= 1
                if right[s[i]] == 0:
                    right.pop(s[i])
                
            for j in range(26):
                char = chr(ord("a") + j) 
                if char in left and char in right:
                    res.add((char, s[i]))
            left.add(s[i])
        return len(res)