class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 1
        r = n

        while l < r:
            l_num = numbers[l-1]
            r_num = numbers[r-1]
            total = l_num + r_num

            if total == target: 
                return [l, r]
            
            elif total < target:
                l += 1
            
            else: 
                r -= 1 