class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        t_char = {}
        s_char = {}
        for i in range(len(s)):
            s_char[s[i]] = 1 + s_char.get(s[i], 0)
            t_char[t[i]] = 1 + t_char.get(t[i], 0)
        return s_char == t_char