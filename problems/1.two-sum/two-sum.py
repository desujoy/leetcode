class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_index = {}
        for i in range(len(nums)):
            if target - nums[i] in value_index:
                return [value_index[target - nums[i]], i]
            value_index[nums[i]] = i
        return [-1, -1]
    
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
