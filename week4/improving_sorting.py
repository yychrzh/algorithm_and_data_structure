# Uses python3
import sys
import random


# < x, = x, > x
def partition3(a, l, r):
    i, k, j = l, l+1, r
    x = a[l]

    while k <= j:
        if a[k] < x:
            a[i], a[k] = a[k], a[i]
            i += 1
            k += 1
        elif a[k] == x:
            k += 1
        else:
            while a[j] > x:
                j -= 1
                if j < k:
                    # break
                    return i, j
            if a[j] == x:
                a[k], a[j] = a[j], a[k]
                k += 1
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                a[j], a[k] = a[k], a[j]
                i += 1
                k += 1
                j -= 1
    return i, j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    i, j = partition3(a, l, r)
    randomized_quick_sort(a, l, i - 1)
    randomized_quick_sort(a, j + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')