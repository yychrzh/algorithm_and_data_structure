# Uses python3
import sys


# Task: The goal in this problem is to fnd the minimum number of coins needed to
#  change the input value (an integer) into coins with denominations 1, 5, and 10.


def read_one_line_data(data_range):
    input_data = [int(x) for x in input().split()]
    for i in range(len(input_data)):
        if input_data[i] < data_range[i][0] or input_data[i] > data_range[i][1]:
            raise Exception("input out of range!")
    return input_data


def change_money(value):
    num_10 = value // 10
    rem_10 = value % 10
    num_5 = rem_10 // 5
    num_1 = rem_10 % 5
    return num_10 + num_5 + num_1


if __name__ == '__main__':
    [money_value] = read_one_line_data([[1, 1e3]])
    print(change_money(money_value))