class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        passed = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in passed:
                return [passed[diff], i]
            passed[n] = i
