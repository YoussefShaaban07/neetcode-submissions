class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result+=str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            count = int(s[start:i])
            i += 1
            word = s[i : i + count]
            result.append(word)
            i += count
        return result