import sys

for line in sys.stdin:
    if line.strip():
        print(" ".join(line.strip().split()))
        print()
