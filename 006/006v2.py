import sys

with open(sys.argv[1]) as fd:
    msg = fd.read().strip()

unique = []

for i, char in enumerate(msg):
    if len(unique) == 14:
        # Evaluate char received
        if len(set(unique)) == 14:
            print(i, unique)
            break
        else:
            del unique[0]

    unique.append(char)
