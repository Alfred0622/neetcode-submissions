class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1

        N = len(s)

        if (N == 0 or N == 1):
            return N
        ans = 1
        counts = defaultdict(lambda : 0)
        counts[s[left]] += 1

        while(right < N):
            counts[s[right]] += 1

            while(counts[s[right]]>= 2):
                counts[s[left]] -= 1
                left += 1
            
            L = right - left + 1
            ans = max(L, ans)
            right += 1
        
        return ans
            