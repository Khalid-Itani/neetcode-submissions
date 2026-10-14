class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums.sort()
        i = 0
        longest = 0

        while i < len(nums):
            curr = 1
            while i+1 < len(nums):
                if nums[i + 1] == nums[i]:
                    i+=1
                elif nums[i+1] == nums[i] + 1:
                    i+=1
                    curr+=1
                else:
                    break #sequence ends
            longest = max(longest, curr)
            i+=1
        return longest
        
            

            