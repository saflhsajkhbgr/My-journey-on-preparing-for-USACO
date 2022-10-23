
def binarySearch(lst, value, low, high):  # low,high是lst的查找范围
    if high < low:
        return -1
    mid = (low + high) / 2
    if lst[mid] > value:
        return binarySearch(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binarySearch(lst, value, mid + 1, high)
    else:
        return mid


lst = [1, 3, 5, 8, 10, 100, 200]


def bi_search(lst, tar):
    low = 0
    high = len(lst)-1
    mid = (low+high)/2
    while low <= high:
        mid = (low+high)//2
        if lst[mid] > tar:
            high = mid-1
        elif lst[mid] < tar:
            low = mid+1
        else:
            return mid
    return -1


print(bi_search(lst, 100))