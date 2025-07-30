def aplusb(a: int, b:int) -> int:
    sum = int(a) + int(b)
    print(sum)

test = input().split()
aplusb(test[0], test[1])