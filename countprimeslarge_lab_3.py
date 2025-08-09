def isprime(n, primes):
    if n in primes:
        return True
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    if n in small_primes:
        primes[n] = True
        return True
    for p in small_primes:
        if n % p == 0 and n != p:
            return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    test_bases = [3, 5, 7, 11, 13]
    for a in test_bases:
        if a >= n:
            continue

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    primes[n] = True
    return True


def divconq(left, right, counter, primes):
    if right - left <= 200:
        for i in range(left, right + 1):
            if isprime(i + 1, primes):
                counter[0] += 1
        return

    mid = (left + right) // 2
    divconq(left, mid, counter, primes)
    divconq(mid + 1, right, counter, primes)


def countprimes(num):
    if num < 2:
        return 0
    primes = {}
    counter = [0]
    divconq(0, num - 1, counter, primes)
    return counter[0]

test = int(input())
print(countprimes(test))