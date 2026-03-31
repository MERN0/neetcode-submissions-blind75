class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx, currMax = nums[0], 0

        for n in nums:
            if currMax < 0:
                currMax = 0
            currMax += n
            maxx = max(currMax, maxx)

        return maxx
