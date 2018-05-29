# Uses python3
import sys


def read_one_line_data(data_range):
    input_data = [int(x) for x in input().split()]
    for i in range(len(input_data)):
        if input_data[i] < data_range[i][0] or input_data[i] > data_range[i][1]:
            raise Exception("input out of range!")
    return input_data


# sort from max to min
def bubble_Sort(data_list, dir=0):
    nums = [data_list[i] for i in range(len(data_list))]
    nums_index = [i for i in range(len(nums))]
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                nums_index[j], nums_index[j+1] = nums_index[j+1], nums_index[j]
    if dir == 0:
        nums.reverse()
        nums_index.reverse()
    return nums, nums_index


def min_points(seg):
    min_ds = [v[0] for v in seg]
    _, index = bubble_Sort(min_ds, 1)
    points = []
    current_min = seg[index[0]][0]
    current_max = seg[index[0]][1]
    for i in range(len(seg) - 1):
        if seg[index[i+1]][0] > current_max:
            points.append(int((current_min + current_max) / 2))
            current_max = seg[index[i + 1]][1]
        elif seg[index[i+1]][1] < current_max:
            current_max = seg[index[i + 1]][1]
        current_min = seg[index[i + 1]][0]
    points.append(int((current_min + current_max) / 2))
    return points


if __name__ == '__main__':
    # get the number of segments:
    [num] = read_one_line_data([[1, 100]])
    # get the min and max num of a segment
    seg = []
    for i in range(num):
        [min_d, max_d] = read_one_line_data([[0, 10e9], [0, 10e9]])
        if min_d > max_d:
            raise Exception("input error, min_d > max_d !")
        seg.append([min_d, max_d])
    points = min_points(seg)
    print(len(points))
    for i in range(len(points)):
        print(points[i], end=" ")