from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_island = 0
        if len(grid) == 0 or not grid:
            return 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    num_of_island += self.bfs(grid, i, j)
                    # num_of_island += self.dfs(grid, i, j)
        return num_of_island

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1':
            return 0

        grid[i][j] = '#'

        self.dfs(grid, i + 1, j)  # down
        self.dfs(grid, i - 1, j)  # up
        self.dfs(grid, i, j + 1)  # right
        self.dfs(grid, i, j - 1)  # left

        return 1

    def bfs(self, grid, i, j):
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1':
                continue
            grid[i][j] = '#'
            q.append((i + 1, j))
            q.append((i - 1, j))
            q.append((i, j + 1))
            q.append((i, j - 1))
        return 1


if __name__ == '__main__':
    island1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    island2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    island3 = [
        ['1', '0', '0', '0', '0'],
        ['0', '1', '0', '0', '0'],
        ['0', '0', '1', '1', '0'],
        ['1', '0', '0', '1', '1'],
    ]
    island4 = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    s = Solution()
    print(s.numIslands(island1))  # 1
    print(s.numIslands(island2))  # 3
    print(s.numIslands(island3))  # 4
    print(s.numIslands(island4))  # 0
