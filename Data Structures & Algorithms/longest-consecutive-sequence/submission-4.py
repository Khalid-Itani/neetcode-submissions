class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 0
        i = 0

        while i < len(nums):
            curr_len = 1

            while i + 1 < len(nums):
                # duplicate → skip
                if nums[i + 1] == nums[i]:
                    i += 1
                # consecutive → extend sequence
                elif nums[i + 1] == nums[i] + 1:
                    curr_len += 1
                    i += 1
                # break in sequence
                else:
                    break

            longest = max(longest, curr_len)
            i += 1

        return longest