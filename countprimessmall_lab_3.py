def isprime(val):
    match val:
        case 0 | 1:
            return False
        case 2 | 3:
            return True
        case _:
            i = 2
            while i < val:
                if val % i == 0:
                    return False
                i += 1
            return True


def countprimes(num: int) -> int:
    num = int(num)
    counter = 0
    for i in range(num + 1):
        if isprime(i):
            counter += 1

    return counter

test = input()
test = int(test)
print(countprimes(test))
