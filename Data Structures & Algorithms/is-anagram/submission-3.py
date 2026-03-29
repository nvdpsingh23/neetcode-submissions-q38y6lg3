class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        seen1 = set()
        seen2 = set()
        for items in s:
            if items in seen1:
                pass
            else:
                seen1.add(items)
        for items in t:
            if items in seen2:
                pass
            else:
                seen2.add(items)

        for items in seen1:
            if items in seen2:
                pass
            else:
                return False
        return True