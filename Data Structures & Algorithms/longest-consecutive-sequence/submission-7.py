class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)

        sequence = 0


        for num in nums:
            
            if num - 1 not in s:

                next_num = num + 1 
                length = 1 

                while next_num in s:
                    length +=1 
                    next_num = next_num + 1
                sequence = max(length,sequence)
        return sequence
                
                

                
                
        