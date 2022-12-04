import sys

with open(sys.argv[1]) as fd:
    pairs = fd.read().strip().split("\n")

count = 0

for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1 = elf1.split("-")
    elf1_list = set(range(int(elf1[0]), int(elf1[1])+1))
    elf2 = elf2.split("-")
    elf2_list = set(range(int(elf2[0]), int(elf2[1])+1))

    shared_areas = elf1_list & elf2_list
    if len(shared_areas) > 0:
        count += 1

print(count)
