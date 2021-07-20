from typing import List


def broken_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid

        if arr[mid] <= arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr,  5) == 6
