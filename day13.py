import json, functools

def compare_packet(L, R):
    for i in range(min(len(L), len(R))):
        Li, Ri = L[i], R[i]
        if type(Li) is int and type(Ri) is int:
            diff = Li - Ri
        else:
            diff = compare_packet(Li if type(Li) is list else [Li], Ri if type(Ri) is list else [Ri])
        if diff != 0: 
            return diff
    return len(L)-len(R)

with open('input.txt', 'r') as f:
    lines = [json.loads(line) for line in f.readlines() if len(line.rstrip())>0]

print("Part 1:", sum([i+1 for i in range(len(lines)//2) if compare_packet(lines[i*2], lines[i*2+1]) < 0]))

DIV2, DIV6 = [[2]], [[6]]
all_sorted = sorted(lines + [DIV2, DIV6], key = functools.cmp_to_key(lambda x,y: compare_packet(x,y)))
print("Part 2:", (all_sorted.index(DIV2)+1) * (all_sorted.index(DIV6)+1))