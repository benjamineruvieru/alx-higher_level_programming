#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) == 'e' or chr(c) == 'q':
        continue
    print("{:c}".format(c), end="")
