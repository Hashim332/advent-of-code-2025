current_pos = 50
code = 0
file = open("day-1-data.txt", "r")

for line in file.readlines():
    direction = line[0]
    magnitude = int(line[1:])

    if direction == "R":
        # if the sum of mag and pos > 99 check if mag greater than 99 then do below else just add 1
        if current_pos + magnitude > 99:
            if magnitude > 99:
                code += (current_pos + magnitude) // 100
            else:
                code += 1

        prev_pos = current_pos
        current_pos = (current_pos + magnitude) % 100
        print("prev_pos = ", prev_pos, "change = ", line, "new_pos = ", current_pos)
        print("")

    elif direction == "L":
        if current_pos - magnitude < 0:
            if magnitude > 99:
                code += abs((current_pos - magnitude) // 100)
            else:
                code += 1

        prev_pos = current_pos
        current_pos = (current_pos - magnitude) % 100
        print("prev_pos = ", prev_pos, "change = ", line, "new_pos = ", current_pos)
        print("")

    if current_pos == 0:
        code += 1


print("CODE = ", code)
