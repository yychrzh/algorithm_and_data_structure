# Uses python3
import sys
# import time


input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
m = int(tokens[1])

# start_time = time.time()
if n < 1 or n > 1*10**18:
    print("input data out of range!")
if m < 2 or m > 1*10**5:
    print("input data out of range!")


fib_list = [0, 1]


def fibonacci(n):
    if len(fib_list) < (n + 1):
        fib_list.append(0)
    if n <= 1:
        return n
    elif fib_list[n] != 0:
        return fib_list[n]
    else:
        fib_list[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_list[n]


def pisano_period(p):
    pisano_list = []
    i = 0
    mod_num = 0
    while True:
        last_mode_num = mod_num
        mod_num = fibonacci(i) % p
        pisano_list.append(mod_num)
        if mod_num == 1 and (last_mode_num + mod_num) == p:
            return pisano_list
        i += 1


p_list = pisano_period(m)
index = n % len(p_list)
product = p_list[index]
print(product)
# end_time = time.time() - start_time
# print(end_time)