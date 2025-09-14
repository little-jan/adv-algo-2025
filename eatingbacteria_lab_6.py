from heapq import heappush, heappop
import math

def eating(size, food):
    return size + math.ceil(food ** 0.5)

no_bacteria, size, hours = input().split()
no_bacteria, size, hours = int(no_bacteria), int(size), int(hours)

bacterias = list(map(int, input().split()))
bacterias.sort()

i = 0
eaten = 0
heap = []

while eaten < hours and (i < len(bacterias) or heap):
    while i < len(bacterias) and bacterias[i] < size:
        heappush(heap, -bacterias[i])
        i += 1

    if not heap:
        break

    bact = -heappop(heap)
    size = eating(size, bact)
    eaten += 1

print(size)