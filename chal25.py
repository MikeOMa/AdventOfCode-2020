input = [15628416, 11161639]
#input = [5764801, 17807724]
modulo = 20201227


def card_transform_sn(sn=7, loop_size=8):
    k = 1
    for i in range(loop_size):
        k = k * sn
        k = k % modulo
    return k


def prime_factors(n):
    i = 2
    factors = []
    while (i * i) <= n:
        if n % i > 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def euler_toitent(number):
    factors = prime_factors(number)
    unique_factors = set(factors)
    factors_drop1 = factors.copy()
    for factor in unique_factors:
        factors_drop1.remove(factor)
    toitent_value= 1
    for k in factors_drop1:
        toitent_value*=k
    for k in unique_factors:
        toitent_value*=(k-1)
    return toitent_value
assert euler_toitent(12)==2*2

def solve_cong(a, b, m=modulo):
    factors = prime_factors(m)
    toitent = euler_toitent(factors)
### y = x^ ln mod p

def find_ln(goal, sn=7, modulo=modulo):
    value = 1
    for k in range(100000000):
        value= (value*sn)%modulo
        if value == goal:
            return k+1
    return -1

from math import gcd
def get_inv(a,m):
    toit = euler_toitent(m)
    inv = (a^(toit-1)) % m
    return inv
lns = [find_ln(i) for i in input]
ek = [card_transform_sn(pk, ln) for pk, ln in zip(input[::-1], lns)]


print(ek)
