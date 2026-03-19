import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

rooms = 0
directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            rooms += 1
            q = deque([(i,j)])
            grid[i][j] = '#'

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
                        grid[nr][nc] = '#'
                        q.append((nr,nc))

print(rooms)