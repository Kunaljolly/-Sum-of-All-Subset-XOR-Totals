class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        # Generate all subsets
        for i in range(2**len(nums)):
            xor_total = 0
            for j in range(len(nums)):
                # If jth bit in the ith subset is set, include nums[j] in the XOR total
                if (i & (1 << j)) > 0:
                    xor_total ^= nums[j]
            result += xor_total
        return result
