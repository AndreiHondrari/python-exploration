#!python3

from ut import p

p("Bubble sort")

data = [29, 3, 1, 40, 7, 2, 6, 4, 20, 15, 18, 16]
print(f"initial data: {data}")

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

print(f"sorted data: {data}")
