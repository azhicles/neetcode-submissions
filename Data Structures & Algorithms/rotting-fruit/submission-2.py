from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)] # left, right, up, down
        q = deque()

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                
                if grid[i][j] == 1:
                    count += 1

        if not q:
            if count > 0: 
                return -1
            return 0

        while q:
            cur = q.popleft()
            for d in dirs:
                r = min(max((cur[0] + d[0]), 0), m-1)
                l = min(max((cur[1] + d[1]), 0), n-1)
                if grid[r][l] == 1:
                    q.append((r, l, cur[2]+1))
                    grid[r][l] = 2
                    count -= 1
        
        if count == 0:
            return cur[2]
        
        else: 
            return -1 
            

