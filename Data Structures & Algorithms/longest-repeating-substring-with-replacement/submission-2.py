class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)

        if (N in {0, 1}):
            return N

        left = 0
        right = 1

        max_freq = 1
        counts = defaultdict(lambda : 0)
        counts[s[left]] += 1

        ans = 1
        while(right < N):
            counts[s[right]] += 1

            max_freq = max(max_freq, counts[s[right]])

            L = right - left + 1

            if (L - max_freq <= k):
                ans = max(ans, L)
            else:
                counts[s[left]] -= 1
                left += 1
            right += 1
        
        return ans
            
        

        