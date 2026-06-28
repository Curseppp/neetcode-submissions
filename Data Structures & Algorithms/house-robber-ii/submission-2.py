class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        return max(self.robLinear(nums, 1,  n-1), self.robLinear(nums, 0, n-2))

    def robLinear(self, nums: List[int], left: int, right: int) -> int:
        if right == 1:
            return nums[0]

        dp = [0] * 3
        dp[0] = nums[left]
        dp[1] = max(nums[left + 1], dp[0])

        for i in range(2, len(nums[left:right + 1])):
            dp[2] = max(dp[1], dp[0] + nums[left + i])
            dp[0], dp[1] = dp[1], dp[2]

        return dp[1]