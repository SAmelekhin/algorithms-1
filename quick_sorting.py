from typing import Any, List


def quicksort(array: List[Any]) -> List[Any]:

    def _partition(start: int, end: int) -> int:
        count = start - 1
        pivot = array[end]
        step = start
        while step < end:
            if array[step] < pivot:
                count += 1
                array[count], array[step] = array[step], array[count]
            step += 1
        array[count + 1], array[end] = array[end], array[count + 1]
        return count + 1

    def _quicksort(elements: List[Any], start: int, end: int) -> None:
        if start > end:
            return
        pivot_ind = _partition(start, end)
        _quicksort(elements, start, pivot_ind - 1)
        _quicksort(elements, pivot_ind + 1, end)

    _quicksort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    class Participant:
        def __init__(self, name: str, tasks: str, penalties: str) -> None:
            self.name = name
            self.tasks = int(tasks)
            self.penalties = int(penalties)

        def __lt__(self, prev: 'Participant') -> bool:
            if self.tasks == prev.tasks:
                if self.penalties == prev.penalties:
                    return self.name < prev.name
                return self.penalties < prev.penalties
            return self.tasks > prev.tasks

        def __str__(self) -> str:
            return self.name

    print(
        *quicksort(
            [Participant(*input().split()) for _ in range(int(input()))]
            ),
        sep='\n'
        )
