class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = list()
        postfix = list()

        pre = 1
        post = 1

        for n in nums:
            prefix.append(pre)
            pre *= n
        
        for k in range(len(nums) - 1, -1 , -1):
            postfix.append(post)
            post *= nums[k]
        
        postfix = postfix[::-1]

        result = list()

        for p1, p2 in zip(prefix, postfix):
            result.append(p1 * p2)

        
        return result
