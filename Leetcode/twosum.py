class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


# Create an instance of the Solution class
solution = Solution()

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result) 