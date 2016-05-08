# https://projecteuler.net/problem=3
def prime(num):
    if num < 1:
        return False
    for n in range(0,num):
        if n == 0 or n == 1 or n == num:
            continue
        r = num % n
        if r == 0:
            return False
    return True


def big_to_small_factors(num):
    f = []
    for n in range(2,num):
        f.append(n)

    f.reverse()
    r = []
    for n in f:
        if num % n == 0:
            r.append(n)

    return r

def big_prime_factor(nums=[]):
    for n in nums:
        if prime(n):
            return n
        else:
            continue
    return 0

# 600851475143 is currently to big 
print(big_prime_factor(big_to_small_factors(600851475143)))

