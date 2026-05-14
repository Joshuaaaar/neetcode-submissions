class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # comparsion between length of list and list converted to a set
        return not (len(nums) == len(set(nums)))