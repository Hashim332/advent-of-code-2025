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


# I had this on my mac:
# current_pos = 50
count = 0
file = open("day-1-data.txt", "r")

# for line in file.readlines():
#     direction = line[0]
#     magnitude = int(line[1:])

#     if direction == "R":
#         # if the sum of mag and pos > 99 check if mag greater than 99 then do below else just add 1
#         if current_pos + magnitude > 99:
#             if magnitude > 99:
#                 count += (current_pos + magnitude) // 100
#             elif current_pos != 0:
#                 count += 1

#         prev_pos = current_pos
#         current_pos = (current_pos + magnitude) % 100
#         print("prev_pos = ", prev_pos, "change = ", line, "new_pos = ", current_pos)
#         print("count = ", count)
#         print("")

#     else:
#         if current_pos - magnitude < 0:
#             if magnitude > 99:
#                 count += abs((current_pos - magnitude) // 100)
#             elif current_pos != 0:
#                 count += 1

#         prev_pos = current_pos
#         current_pos = (current_pos - magnitude) % 100

#         print("prev_pos = ", prev_pos, "change = ", line, "new_pos = ", current_pos)
#         print("count = ", count)
#         print("")

#     if current_pos == 0:
#         count += 1
#         print("hit zero count = ", count)
#         print("")


# print("code = ", count)


# for line in file.readlines():
#     direction = line[0]
#     magnitude = int(line[1:])

#     if direction == "R":
#         next_number = current_pos + magnitude
#         next_pos = next_number % 100
#         print(f"current pos:{current_pos} rotation:{line} count:{count}")
#         print("")
#         if next_pos == 0:
#             count += 1
#         else:
#             total_cycles = next_number // 100
#             count += total_cycles
#         current_pos = next_pos

#     else:
#         next_number = current_pos - magnitude
#         next_pos = next_number % 100
#         if next_pos == 0:
#             count += 1
#         else:
#             total_cycles = abs(next_number) // 100
#             count += total_cycles
#         current_pos = next_pos
#

for line in file.readlines():
    direction = line[0]
    magnitude = int(line[1:])

    if line[0] == "R":
        turn = int(line[1:])
    elif line[0] == "L":
        turn = -int(line[1:])


print("code = ", count)
