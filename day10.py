f = open('input.txt', 'r')

regX = 1
pend = 0
signal = 0
screen = [' '] * 241

for cyc in range(1,241):
    if cyc % 40 == 20:
        signal += cyc * regX

    if abs(((cyc-1)%40)-regX) <= 1: screen[cyc] = '\N{FULL BLOCK}'

    if pend != 0:
        regX += pend
        pend = 0
    else:
        line = f.readline()
        if line.startswith('addx '):
            pend = int(line.split()[1])

print(f"Part 1: {signal}")

print("Part 2:\n")
for row in range(6):
    print(''.join(screen[row*40+1:row*40+40]))
