liters = "ABCDEFGI123456YTRE12313231248Q11WF"

for liter in liters:
    print(liter, end=" ")

print("\n----------------")

d = len(liters)

for i in range(0, d, 3):
    print(liters[i], end=" ")
print()

print(d)
i = 0
while i < d:
    print(liters[i], end=" ")
    if liters[i] == '6':
        break
    i = i + 1

print("\n----------------")

while i < d:
    if liters[i] == '6':
        i = i + 1
        continue
    else:
        print(liters[i], end=" ")
    i = i + 1

print("\n----------------")

while i < d:
    if liters[i].isalpha():
        i = i + 1
        continue
    else:
        print(liters[i], end=" ")
    i = i + 1