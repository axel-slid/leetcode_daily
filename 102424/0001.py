# What I Did
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0

        for i in range(len(nums)):  # first pointer
            for j in range(len(nums)):  # second pointer
                j += 1
                if j == len(nums):
                    j -= 1
                if (nums[i] + nums[j] == target) and j != i:
                    s = [i, j]

        return s


# What I Should Have Done
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in map:
                return [i, map[new_target]]

            map[nums[i]] = i


# Why the Second is Better:
# The second solution is better because it makes use of a hashmap (dictionary) to store values
# as we iterate through the list. For each element, we calculate the difference needed to reach 
# the target (new_target) and check if that difference is already in the hashmap.
# - If it is, we have found our two numbers and can return their indices.
# - If not, we add the current number to the hashmap.
# This approach allows us to find the solution in O(n) time complexity, as opposed to the
# O(n^2) time complexity of the first solution due to the nested loops.
