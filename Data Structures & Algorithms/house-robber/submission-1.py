class Solution:
    def rob(self, nums: List[int]) -> int:

        curr1 = 0
        curr2 = 0


        for x in nums:
            temp = max(x + curr1, curr2)
            curr1 = curr2
            curr2 = temp
        return curr2
