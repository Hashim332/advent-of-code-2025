instructions = [
    int(line.strip().replace("L", "-").replace("R", "")) for line in open("input.txt")
]
dial = 50
count = 0

for turn in instructions:
    if turn < 0:
        div, mod = divmod(turn, -100)
        count += div
        if dial != 0 and dial + mod <= 0:
            count += 1
    else:
        div, mod = divmod(turn, 100)
        count += div
        if dial + mod >= 100:
            count += 1

    dial = (dial + turn) % 100

print(count)
