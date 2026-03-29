class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=set(s)
        t=set(t)
        for n in s:
            if n in t:
                t.remove(n)
            else:
                return False

        return True
        