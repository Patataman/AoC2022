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

for bag in bags:
    first_half = set(bag[0:len(bag)//2])
    second_half = set(bag[len(bag)//2:])

    same_item = (first_half & second_half).pop()
    if ord(same_item) >= ord("a"):
        total_priority += ord(same_item) - min_priority_lowercase
    elif ord(same_item) < ord("a"):
        total_priority += ord(same_item) - min_priority_uppercase

print(total_priority)
