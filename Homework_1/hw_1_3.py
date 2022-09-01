# problem 3 - creating an intersection of sets

set1 = {3, 5, 2, "me", " ", 636, 12}
set2 = {2, 73, 1, " ", "hello", 12}

print("Set 1:", set1)
print("Set 2:", set2)

set3 = set()

for x in set1:
    for y in set2:
        if x == y:
            set3.add(x)
            continue

print("Common elements in both Sets 1 and 2:", set3)