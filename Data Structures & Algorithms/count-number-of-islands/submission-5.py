class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        num_of_islands = 0

        num_rows = len(grid)
        num_columns = len(grid[0])

        visted = set()

        def dfs(i,j):
            if i < 0 or i >= num_rows or j < 0 or j >= num_columns or grid[i][j] == '0' or (i,j) in visted:
                return 
            else:
                visted.add((i,j))
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
        
        for i in range(num_rows):

            for j in range(num_columns):

                if grid[i][j] == '1' and (i,j) not in visted:

                    num_of_islands += 1
                    dfs(i,j)
        return num_of_islands

        

        







        