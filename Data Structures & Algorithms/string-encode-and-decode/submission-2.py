class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs==None:
            return None
        return ".".join(strs)

    def decode(self, s: str) -> List[str]:
        if str==None:
            return None
        return s.split(".")
