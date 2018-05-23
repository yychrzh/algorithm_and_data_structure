# Uses python3
import sys


def read_one_line_data(data_range):
    input_data = [int(x) for x in input().split()]
    for i in range(len(input_data)):
        if input_data[i] < data_range[i][0] or input_data[i] > data_range[i][1]:
            raise Exception("input out of range!")
    return input_data


# sort from max to min
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


def max_revenue(ads, slots):
    sort_ads, _ = bubble_Sort(ads)
    sort_slots, _ = bubble_Sort(slots)
    revenue = 0
    for i in range(len(ads)):
        revenue += sort_ads[i] * sort_slots[i]
    return revenue


if __name__ == '__main__':
    # get the number of ads and slots:
    [num] = read_one_line_data([[1, 1e3]])
    # get the sequences of ads:
    ads_profit = read_one_line_data([[-1e5, 1e5] for _ in range(num)])
    # get the sequences of slots:
    slots_click = read_one_line_data([[-1e5, 1e5] for _ in range(num)])
    print(max_revenue(ads_profit, slots_click))