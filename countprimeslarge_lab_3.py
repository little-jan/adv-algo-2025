def divconq(lst, left, right, counter):
    if right - left <= 5:
        for i in range(left, right + 1):
            if isprime(lst[i]):
                counter[0] += 1
        return
    else:
        mid = (left + right) // 2
        divconq(lst, left, mid, counter)
        divconq(lst, mid + 1, right, counter)

def isprime(val):
    match val:
        case 0 | 1:
            return False
        case 2 | 3:
            return True
        case _:
            i = 2
            while i * i <= val:
                if val % i == 0:
                    return False
                i += 1
            return True

def countprimes(num: int) -> int:
    num = int(num)
    counter = [0]
    lst = list(range(1, num + 1))
    divconq(lst, 0, len(lst) -1, counter)
    return counter[0]

test = input()
test = int(test)
print(countprimes(test))
