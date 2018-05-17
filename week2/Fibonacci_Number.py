# Uses python3

# read data from screen:
input_num = int(input())
if input_num < 0 or input_num > 45:
    print("input out of range!")

fib_list = [0]*(input_num+1)
if input_num > 0:
    fib_list[1] = 1


def fibonacci(n):
    if n <= 1:
        return n
    elif fib_list[n] != 0:
        return fib_list[n]
    else:
        fib_list[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_list[n]

data = fibonacci(input_num)
print(data)