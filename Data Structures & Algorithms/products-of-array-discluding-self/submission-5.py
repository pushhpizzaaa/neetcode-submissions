class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output =[]

        # for i in range(len(nums)):
        #     prod = 1 

        #     for j in range(len(nums)):
        #         if i != j:
        #             prod = prod * nums[j]
        #     output.append(prod)
        
        # return output
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output