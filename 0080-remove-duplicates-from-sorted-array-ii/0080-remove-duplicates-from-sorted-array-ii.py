class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while True:
            try:
                if(nums[i-1]==nums[i] and nums[i+1]==nums[i]):
                    del nums[i]
                    i=i-1
                i=i+1
            except:
                return len(nums)
        