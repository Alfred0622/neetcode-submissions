class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        for i, n in enumerate(nums):
            diff[n] = i
        
        for i, n in enumerate(nums):
            d = target - n
            if (d in diff) and i != diff[d]:

                return [i, diff[d]]