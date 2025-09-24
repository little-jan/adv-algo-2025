input_length = int(input())

blues = []
green = 10 ** 9

for i in range(input_length):
    val,colour = input().split()
    val = int(val)

    if colour == 'G':
        if val < green:
            green = val

    else:
        blues.append(val)

blues.sort()
blue = 0

for j in reversed(range(len(blues))):
    if blues[j] >= green:
        continue
    else:
        blue = blues[j]
        break

print(blue)
