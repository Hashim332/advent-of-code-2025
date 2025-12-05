input = "492410748-492568208,246-390,49-90,16-33,142410-276301,54304-107961,12792-24543,3434259704-3434457648,848156-886303,152-223,1303-1870,8400386-8519049,89742532-89811632,535853-567216,6608885-6724046,1985013826-1985207678,585591-731454,1-13,12067202-12233567,6533-10235,6259999-6321337,908315-972306,831-1296,406-824,769293-785465,3862-5652,26439-45395,95-136,747698990-747770821,984992-1022864,34-47,360832-469125,277865-333851,2281-3344,2841977-2953689,29330524-29523460"
# ranges = input.split(",")
# invalid = []
# res = 0

# # NOTES:
# # repeatable units only go up to half
# # max repeated subunit is always <= half the "length" of num i.e max repeated subunit for 9 is 3, for 8 it's 4
# # for even nums, just find half, for odd nums smallest subunit is always < than half
# #
# # easiest way to catch them is just check half way (or closest possible subunit if num is odd) and then

# # find largest repeatable subunit
# # find smallest repeatable subunit
# #
# # check if greater or less than limits, add to sum

# for r in ranges:
#     # convert to int, e.g. limits = [232, 234]
#     limits = [int(n) for n in r.split("-")]

#     for num in range(limits[0], limits[1] + 1):
#         half_l = len(str(num)) // 2

#         first_half = str(num)[0:half_l]
#         second_half = str(num)[half_l:]

#         if first_half == second_half:
#             print(first_half, second_half)
#             print(num)
#             res += num


#         # if num is prime, check if its just 1 digit all the way thru

#         # get half the length
#         # see what your repeatable halves are i.e if its between 4600000 and 4700000
#         # it could be 4646 4646 or 4655 4655 or 4671 4671
#         # the largest repeatable subunit is the 1 less than the max subunit (?) (see below )
#         # so really u only need to look for a list of 4 digit numbers i.e from 4600 to 4699
#         # apparently works even without considering odd nums?
#     print(res)


# P2
ranges = input.split(",")
invalid = []
res = 0

for r in ranges:
    # convert range to list of ints, e.g. limits = [232, 234]
    limits = [int(n) for n in r.split("-")]

    # loop between the limits
    for num in range(limits[0], limits[1] + 1):
        # for each num, find all it's factors by finding 1/2 of its length and using modulo down to 1
        # split the string into chunk size = factor
        half_l = len(str(num)) // 2
        factors = []

        # find all factors of the length of nums i.e the size of repeatable chunks
        for x in range(half_l, 0, -1):
            if len(str(num)) % x == 0:
                factors.append(x)

        # factor = chunksize
        for factor in factors:
            # divide num into a list of chunks for each factor
            chunks = [str(num)[i : i + factor] for i in range(0, len(str(num)), factor)]
            # print(
            #     f"num:{num}, len={len(str(num))}, factors of l={factors}, chunks={chunks}"
            # )
            # print("")

            # for a list of chunks to be valid, they must all be the same so I reduce via set()
            if len(set(chunks)) == 1:
                # if len(str(num)) < 4:
                #     print(f"num: {num}, invalid:{chunks} & res:{res}")
                print(f"num: {num}, invalid:{chunks} & res:{res}")
                res += num
                break
                print("updated res = ", res)
                print("")

print(res)
