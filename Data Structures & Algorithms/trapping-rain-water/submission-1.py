class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        
        lar_pre = 0
        lar_suf = 0

        res = 0

        for i in range(1, len(height)):
            curr = height[i-1]
            if curr > lar_pre:
                prefix[i] = curr
                lar_pre = prefix[i]
            else:
                prefix[i] = lar_pre

        for i in range(len(height) - 2, -1, -1):
            curr = height[i+1]
            if curr > lar_suf:
                suffix[i] = curr
                lar_suf = suffix[i]
            else:
                suffix[i] = lar_suf

        for i in range(len(height)):
            test = min(prefix[i], suffix[i]) - height[i]
            if test > 0:
                res += test
        return res
