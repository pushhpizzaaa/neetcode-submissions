class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nset = set(nums)
        # longest = 0
        # length = 0

        # for i in nset:
        #     if i - 1 not in nset:
        #         current = i
        #         length = 1

        #         while current + 1 in nset:
        #             current += 1
        #             length += 1

            
        #     longest = max(longest, length)

        # return longest
        
        if not nums:
            return 0

        nums.sort()
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                current += 1

            else:
                current = 1

            longest = max(longest, current)

        return longest
