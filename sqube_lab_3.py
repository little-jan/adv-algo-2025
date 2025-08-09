def cubed(val):
    return val ** 3

def squared(val):
    return val ** 2

def squbed(val):
    return val ** 6

def number(low: int, high: int) -> str:
    square_result = 0
    cube_result = 0
    sqube_result = 0

    squares = 0
    cubes = 0
    squbes = 0

    base = 1
    while True:
        square_result = squared(base)
        if square_result > high:
            break
        if square_result >= low:
            squares += 1
        base += 1

    base = 1
    while True:
        cube_result = cubed(base)
        if cube_result > high:
            break
        if cube_result >= low:
            cubes += 1
        base += 1

    base = 1
    while True:
        sqube_result = squbed(base)
        if sqube_result > high:
            break
        if sqube_result >= low:
            squbes += 1
        base += 1

    return f"{squares} {cubes} {squbes}"

low, high = map(int, input().split())
print(number(low, high))
