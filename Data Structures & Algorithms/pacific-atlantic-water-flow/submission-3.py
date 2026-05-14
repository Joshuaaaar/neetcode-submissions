from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p_que = deque()
        a_que = deque()

        p_set = set()
        a_set = set()


        rows = len(heights)
        columns = len(heights[0])

        for j in range(columns):

            p_que.append((0,j))
            p_set.add((0,j))
        
        for i in range(1,rows):
            p_que.append((i,0))
            p_set.add((i,0))
        
        for i in range(rows):
            a_que.append((i,columns - 1))
            a_set.add((i,columns - 1))
        
        for j in range(columns - 1):
            a_que.append((rows - 1, j))
            a_set.add((rows - 1 , j))
        
        def get_coords_of_border(que, seen):

            while que:
                (i, j) = que.popleft()
                for i_off , j_off in [(0,1),(1,0),(0,-1),(-1,0)]:

                    r , c = i + i_off , j + j_off 

                    if 0 <= r < rows and 0 <= c < columns and heights[r][c] >= heights[i][j] and (r,c) not in seen:

                        que.append((r,c))
                        seen.add((r,c))
            
            return seen
        
        get_coords_of_border(p_que,p_set)
        get_coords_of_border(a_que,a_set)

        return list(p_set.intersection(a_set))






        





        