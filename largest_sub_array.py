class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print("The subarray has the largest sum",solution.maxSubArray(nums))