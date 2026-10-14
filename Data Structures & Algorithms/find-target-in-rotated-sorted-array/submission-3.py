class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        #left half search
        if pivot > 0 and target >= nums[0] and target <= nums[pivot - 1]:
            l, r = 0, pivot - 1

            while l <= r:
                m = (l + r) // 2

                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
        #right half search
        else:
            l, r = pivot, n - 1

            while l <= r:
                m = (l + r) // 2

                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
        return -1