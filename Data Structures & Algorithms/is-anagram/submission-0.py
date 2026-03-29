class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=set(s)
        t=set(t)
        for n in s:
            if n in t:
                t.remove(n)
                continue
            return False

        return True
        