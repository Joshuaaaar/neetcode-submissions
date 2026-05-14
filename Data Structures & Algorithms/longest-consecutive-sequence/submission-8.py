class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        longest_sequence = 0

        for num in nums:

            if num - 1 not in s:

                next_num = num + 1 
                seq = 1
                while next_num in s:

                    seq += 1
                    next_num = next_num + 1 
                
                longest_sequence = max(longest_sequence, seq)
        
        return longest_sequence




                

                
                
        