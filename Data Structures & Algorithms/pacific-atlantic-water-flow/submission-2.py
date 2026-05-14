from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        a_queue = deque()
        p_queue = deque()

        a_set = set()
        p_set = set()


        rows = len(heights)

        columns = len(heights[0])

        # populate the pacific one with borders
        
        for j in range(columns):
            p_queue.append((0,j))
            p_set.add((0,j))
        
        for i in range(1,rows):
            p_queue.append((i,0))
            p_set.add((i,0))
        
        # populate the atlantic one with borders

        for j in range(columns):

            a_queue.append((rows-1,j))
            a_set.add((rows-1,j))

        for i in range(rows - 1):

            a_queue.append((i,columns - 1))
            a_set.add((i,columns - 1))
        

        def get_coords(que , seen):
            coords = set()
            while que:
                i , j = que.popleft()
                coords.add((i,j))
                for i_off , j_off in [(0,1),(0,-1),(-1,0),(1,0)]:
                    r, c = i + i_off, j + j_off

                    if 0 <= r < rows and 0 <= c < columns and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
            return coords
        
        p_coord = get_coords(p_queue,p_set)
        a_coord = get_coords(a_queue,a_set)

        return list(p_coord.intersection(a_coord))





        