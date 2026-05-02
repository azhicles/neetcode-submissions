class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints = {}
        for idx, i in enumerate(nums): 
            if i in ints: 
                return [ints[i], idx]
            else: 
                ints[target-i] = idx