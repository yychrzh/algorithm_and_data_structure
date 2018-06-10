# Uses python3
import sys

"""
def majorityElement(data_nums):
    major = data_nums[0]
    cnt = 0
    for i in range(len(data_nums)):
        if 0 == cnt:
            cnt = 1
            major = data_nums[i]
        elif major == data_nums[i]:
            cnt += 1
        else:
            cnt -= 1
    return major, cnt
"""


def divide_and_conquer(nums):
    if len(nums) <= 1:
        return nums[0]

    mid = int(len(nums) / 2)
    x = divide_and_conquer(nums[0:mid])
    y = divide_and_conquer(nums[mid:])
    if x == y:
        return x
    else:
        countX = 0
        countY = 0
        for i in range(len(nums)):
            if x == nums[i]:
                countX += 1
            elif y == nums[i]:
                countY += 1
        if countX > countY:
            return x
        else:
            return y


if __name__ == '__main__':
    # read data nums
    n = [int(x) for x in input().split()][0]
    # read data
    data_list = [int(x) for x in input().split()]
    if len(data_list) != n:
        print("input error !")
    major = divide_and_conquer(data_list)
    count = 0
    for i in range(len(data_list)):
        if major == data_list[i]:
            count += 1
    if count > n/2:
        print(1)
    else:
        print(0)