import numpy as np

def shortest_path(grid, start, goal):
    parent = {}
    searched = np.zeros(grid.shape, dtype=bool)
    searched[start] = True
    frontier = [(0, start)]

    xmax, ymax = grid.shape
    while len(frontier) > 0:
        frontier.sort(key=lambda x: x[0], reverse=True)
        currnode = frontier.pop()
        steps, (x, y) = currnode
        for xd, yd in [[0,-1], [-1,0], [1,0], [0,1]]:
            next = (x+xd, y+yd)
            if 0 <= next[0] < xmax and 0 <= next[1] < ymax and grid[next] <= grid[x][y]+1:
                if next == goal:
                    route = [currnode]
                    while currnode in parent:
                        currnode = parent[currnode]
                        route.append(currnode)
                    return len(route)

                if not searched[next]:
                    searched[next] = True
                    nextnode = (steps+1, next)
                    frontier.append(nextnode)
                    parent[nextnode] = currnode
    return None

### MAIN ###############################################################################

with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

xmax = len(lines[0])
ymax = len(lines)
grid = np.empty((xmax,ymax),dtype=int)
for y in range(ymax): grid[:,y] = [ord(c) for c in lines[y]]

start = list(zip(*np.where(grid == ord('S'))))[0]
goal  = list(zip(*np.where(grid == ord('E'))))[0]
grid[start] = ord('a')
grid[goal] = ord('z')

part1 = shortest_path(grid, start, goal)
print("Part 1:", part1)

all_starts = list(zip(*np.where(grid == ord('a'))))
all_paths = [shortest_path(grid, start, goal) for start in all_starts]
print("Part 2:", min([x for x in all_paths if x != None]))
