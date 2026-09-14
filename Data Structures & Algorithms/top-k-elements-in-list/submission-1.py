class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda : 0)

        for n in nums:
            counts[n] += 1
        
        N = len(nums)

        buckets = [list() for _ in range(N)]

        for i, v in counts.items():
            buckets[v-1].append(i)
        
        ans = list()
        for n in range(N, 0, -1):
            ans += buckets[n-1]
            if (len(ans) >= k):
                return ans[:k]
            
        
        return ans
        