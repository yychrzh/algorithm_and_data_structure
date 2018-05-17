# Uses python3

# read data from screen:
n = int(input())
a = [int(x) for x in input().split()]

product = 0


def find_max_two(data, n):
    max_data = data[0]
    second_data = data[0]
    index = 0
    for i in range(n):
        if max_data < data[i]:
            max_data = data[i]
            index = i
    if index == 0:
        second_data = data[1]
    for i in range(n):
        if i != index and second_data < data[i]:
            second_data = data[i]
    return max_data, second_data


data0, data1 = find_max_two(a, n)
product = data0 * data1
print(product)