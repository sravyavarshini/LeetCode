class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while True:
            if (nums[i]==nums[i+1]):
                return nums[i]
            i=i+1