class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=set()
        for i,val in enumerate (nums):
            s=target-nums[i]
            if s in a:
                return [nums.index(s),i]
            else:
                a.add(val)