# Uses python3
import sys


# Task: The goal in this problem is to fnd the minimum number of coins needed to
#  change the input value (an integer) into coins with denominations 1, 5, and 10.


def read_data_from_screen(data_n, data_range):
    input_data = []
    input = sys.stdin.read()
    tokens = input.split()
    for i in range(data_n):
        data = int(tokens[i])
        if data < data_range[i][0] or data > data_range[i][1]:
            raise Exception("input out of range!")
        input_data.append(data)
    return input_data


def change_money(value):
    num_10 = value // 10
    rem_10 = value % 10
    num_5 = rem_10 // 5
    num_1 = rem_10 % 5
    return num_10 + num_5 + num_1


if __name__ == '__main__':
    [money_value] = read_data_from_screen(1, [[1, 1e3]])
    print(change_money(money_value))