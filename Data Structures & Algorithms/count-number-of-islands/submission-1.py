class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0

        # num of rows
        m = len(grid)
        # num of columns
        n = len(grid[0])
        # to make sure to not have an infinite cycle
        visted = set()

        def dfs(i,j):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or (i,j) in visted:
                return
            else:
                visted.add((i,j))
                dfs(i, j + 1)
                dfs(i + 1 , j)
                dfs(i - 1 , j)
                dfs(i , j - 1) 



        for i in range(m):

            for j in range(n):

                if (i,j) not in visted and grid[i][j] == '1':
                    num_islands +=1 
                    dfs(i,j)
        return num_islands







        