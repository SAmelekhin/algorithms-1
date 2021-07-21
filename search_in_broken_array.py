from typing import Any, List, Tuple, Union


def broken_search(elements: Union[List[Any], Tuple[Any]], target: Any) -> Any:
    left, right = 0, len(elements) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == elements[mid]:
            return mid
        if elements[mid] <= elements[right]:
            if elements[mid] < target <= elements[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if elements[left] <= target < elements[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr,  5) == 6
