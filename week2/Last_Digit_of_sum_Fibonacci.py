# Uses python3
import time


# read data from screen:
input_num = int(input())

if input_num < 0 or input_num > 10**14:
    print("input out of range!")

# start_time = time.time()
fib_list = [0] * (input_num + 1)
fib_list[0] = 0
if input_num > 0:
    fib_list[1] = 1

product = 0
for i in range(input_num + 1):
    if i > 1:
        fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % 10
    product = (product + fib_list[i]) % 10
print(product)
# end_time = time.time() - start_time
# print(end_time)