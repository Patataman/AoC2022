# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

import sys

with open(sys.argv[1]) as fd:
    bags = fd.read().strip().split("\n")

# i'm lazy
min_priority_uppercase = ord("A") - 27
min_priority_lowercase = ord("a") - 1
total_priority = 0

for cO in range(0, len(bags), 3):
    first = set(bags[cO])
    second = set(bags[cO+1])
    third = set(bags[cO+2])

    same_item = (first & second & third).pop()
    if ord(same_item) >= ord("a"):
        total_priority += ord(same_item) - min_priority_lowercase
    elif ord(same_item) < ord("a"):
        total_priority += ord(same_item) - min_priority_uppercase

print(total_priority)
