class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        result = 0
        for n in nums:
            c = 1
            if (n -1 in num_set):
                continue
            
            k = n + 1
            while(k in num_set):
                k += 1
                c += 1
            
            result = max(c, result)
        
        return result