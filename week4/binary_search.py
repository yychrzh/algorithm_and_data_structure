# Uses python3
import sys


def read_one_line_data(data_range):
    input_data = [int(x) for x in input().split()]
    for i in range(len(input_data)):
        if input_data[i] < data_range[i][0] or input_data[i] > data_range[i][1]:
            raise Exception("input out of range!")
    return input_data


def binarySearch(theValues, target):
    # Start with the entire sequence of elements.
    low = 0
    high = len(theValues) - 1
    # Repeatedly subdivide the sequence in half until the target is found.

    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return mid
        # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
        # Or does it follow the midpoint?
        else:
            low = mid + 1
        # If the sequence cannot be subdivided further, we're done.
    return -1


if __name__ == '__main__':
    # read line1: n , sequence(a0, a1, .., an-1)
    data_1 = [int(x) for x in input().split()]
    # read line2: k , sequence(b0, b1, .., bk-1)
    data_2 = [int(x) for x in input().split()]
    n, k = data_1[0], data_2[0]
    a_s, b_s = data_1[1:], data_2[1:]
    if (n != len(a_s)) or (k != len(b_s)):
        print("data input error !")
    index_list = []
    for i in range(len(b_s)):
        index_list.append(binarySearch(a_s, b_s[i]))
    for i in range(k):
        print(index_list[i], end=" ")
