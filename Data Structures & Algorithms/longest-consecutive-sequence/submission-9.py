class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        num = set(nums)
        
        for i in num:
            curr = 1
            if i-1 in num:
                continue
            else:
                while i+1 in num:
                    curr+=1
                    i+=1
            if curr > longest:
                longest = curr
        return longest
