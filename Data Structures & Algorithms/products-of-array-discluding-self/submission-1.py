class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        res = [0] * len(nums)

        for i in nums:
            if i != 0:
                prod *= i
            else:
                zeros += 1
        
        if zeros > 1:
            return [0] * len(nums)
        
        for i,c in enumerate(nums):
            if zeros > 0:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//c
        return res