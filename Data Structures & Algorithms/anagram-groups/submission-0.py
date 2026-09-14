class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        anagram = defaultdict(lambda: list())

        for s in strs:
            s_s = sorted(s)

            anagram["".join(s_s)].append(s)
        

        return [v for v in anagram.values()]