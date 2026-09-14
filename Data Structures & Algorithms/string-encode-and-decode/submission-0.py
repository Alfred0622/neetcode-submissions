class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []

        for s in strs:
            sizes.append(len(s))
        for s, sz in zip(strs, sizes):
            res.append(str(sz))
            res.append('#')
            res.append(s)
        
        print(res)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if (not s):
            return []
        
        print(s)
        res, i =  [], 0

        while(i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            res.append(s[j+ 1: j + l + 1])
            i = j + 1 + l

        return res
