# Uses python3
import sys
# import time
# test: 226553150 1023473145  46374212988031350
input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

if a == 0 and b == 0:
    print("the two num can't all be zero!")
if a < 0 or a > 2*10**9:
    print("input data out of range!")
if b < 0 or b > 2*10**9:
    print("input data out of range!")


def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


def lcm(p, q):
    return p*q // gcd(p, q)


print(lcm(a, b))