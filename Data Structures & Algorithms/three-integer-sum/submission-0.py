class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        N = len(nums)
        for i in range(N - 2):
            n = nums[i]

            target = -n

            left = i + 1
            right = N - 1


            while(left < right):
                total = nums[left] + nums[right]
                if (total < target):
                    left += 1
                
                elif (total > target):
                    right -= 1
                
                else:
                    temp = [n, nums[left], nums[right]]

                    if (temp not in result):
                        result.append(temp)

                    left += 1
                
                
        
        return result
