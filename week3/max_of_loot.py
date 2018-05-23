# Uses python3
import sys


def read_one_line_data(data_n, data_range):
    # input_data = []
    # input = sys.stdin.read()
    # tokens = input.split()
    input_data = [int(x) for x in input().split()]
    for i in range(len(input_data)):
        if input_data[i] < data_range[i][0] or input_data[i] > data_range[i][1]:
            raise Exception("input out of range!")
    return input_data


# from max to min
def bubble_Sort(data_list):
    nums = [data_list[i] for i in range(len(data_list))]
    nums_index = [i for i in range(len(nums))]
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                nums_index[j], nums_index[j+1] = nums_index[j+1], nums_index[j]
    nums.reverse()
    nums_index.reverse()
    return nums, nums_index


def items_choose(items, max_cap):
    def item_unit(items_info):
        unit = []
        for i in range(len(items_info)):
            unit.append((float(items_info[i][0] / items_info[i][1])))
        return unit

    items_unit = item_unit(items)
    _, index = bubble_Sort(items_unit)  # sort the unit value/weights of the items
    accu_weights, accu_value = 0, 0.0
    rest_cap = max_cap
    for i in range(len(index)):
        if rest_cap > 0:
            if rest_cap >= items[index[i]][1]:
                accu_value += items[index[i]][0]
                rest_cap -= items[index[i]][1]
            else:
                accu_value += float((rest_cap / items[index[i]][1]) * items[index[i]][0])
                rest_cap = 0
                break
    return accu_value


if __name__ == '__main__':
    # get the num of items and the capacity
    [item_num, max_cap] = read_one_line_data(2, [[1, 1e3], [0, 2e6]])
    # print("get input: ", item_num, max_cap)
    # get the value and weights of all items:
    items_info = []
    for i in range(item_num):
        [value, weights] = read_one_line_data(2, [[0, 2e6], [0, 2e6]])
        # print("get item%d: "%i, value, weights)
        items_info.append([value, weights])
    print("{:.4f}".format(items_choose(items_info, max_cap)))