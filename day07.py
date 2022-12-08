import re

with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

curr_dir = []
contents = {}

for line in lines:
    if line == '$ ls':
        dir_key = "/".join(curr_dir)
    elif line.startswith('$ cd '):
        next_dir = line.split()[2]
        if next_dir == '/':
            curr_dir = []
        elif next_dir == '..':
            curr_dir.pop()
        else:
            curr_dir.append(next_dir)
    else:
        sz = line.split()[0]
        contents[dir_key] = contents.get(dir_key, []) + [0 if sz =='dir' else int(sz)]

dir_sizes = {k+'/': sum(lv) for k, lv in contents.items()}
cum_dir_sizes = {root:sum([v for subdir,v in dir_sizes.items() if subdir.startswith(root) or root == '/']) for root in dir_sizes} 

part1 = sum([v for v in cum_dir_sizes.values() if v <= 100000])
print("Part 1:", part1)

need_to_delete = sum(dir_sizes.values()) - 40000000
part2 = min([v for v in cum_dir_sizes.values() if v > need_to_delete])
print("Part 2:", part2)
