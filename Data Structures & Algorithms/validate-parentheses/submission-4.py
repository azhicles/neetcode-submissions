class Solution:
    def isValid(self, s: str) -> bool:
        ref = {'(': ')',
                '{': '}',
                '[': ']'}
        stack = []

        for i in s: 
            if i in ref.keys():
                stack.append(i)

            else:
                if not stack: 
                    return False
                cur = stack.pop()
                if ref[cur] != i:
                    return False
        
        return not stack
            
