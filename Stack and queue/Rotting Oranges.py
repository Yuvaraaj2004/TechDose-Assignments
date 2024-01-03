class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        check = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def valid(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == 2:
                return False
            return True
        c = [0]

        def bfs(n):
            if len(n) == 0:
                return
            l = []
            c[0] += 1
            for i in n:
                for j in check:
                    if valid(i[0]+j[0], i[1]+j[1]):
                        grid[i[0]+j[0]][j[1]+i[1]] = 2
                        l.append([i[0]+j[0], j[1]+i[1]])
            '''for i in grid:
                print(i)
            print()'''
            if len(l) != 0:
                bfs(l)
        l = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                   l.append([i, j])
        bfs(l)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   return -1

        return (c[0]-1 if c[0] >0 else 0)