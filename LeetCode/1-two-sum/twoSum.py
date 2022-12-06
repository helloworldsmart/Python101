# https://leetcode.com/problems/two-sum/
# https://ithelp.ithome.com.tw/articles/10269246
# First: 2022/12/06

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
