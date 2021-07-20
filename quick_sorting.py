from typing import Any, List


class Players:
    def __init__(self, name: str, tasks: int, penalties: int) -> None:
        self.name = name
        self.tasks = tasks
        self.penalties = penalties

    def __lt__(self, prev: 'Players') -> bool:
        if self.tasks == prev.tasks:
            if self.penalties == prev.penalties:
                return self.name < prev.name
            return self.penalties < prev.penalties
        return self.tasks > prev.tasks

    def __str__(self) -> str:
        return self.name


def partition(arr: List[Any], start: int, end: int) -> int:
    count = start - 1
    pivot = arr[end]
    step = start

    while step < end:
        if arr[step] < pivot:
            count += 1
            arr[count], arr[step] = arr[step], arr[count]
        step += 1
    arr[count + 1], arr[end] = arr[end], arr[count + 1]
    return count + 1


def quicksort(arr: List[Any], start=0, end=None) -> None:
    if end is None:
        end = len(arr) - 1

    if start < end:
        pivot_ind = partition(arr, start, end)
        quicksort(arr, start, pivot_ind - 1)
        quicksort(arr, pivot_ind + 1, end)


def main():
    cnt_players: int = int(input())
    players: List[Players] = [0] * cnt_players

    for count in range(cnt_players):
        val_1, val_2, val_3 = input().split()
        players[count] = Players(val_1, int(val_2), int(val_3))

    quicksort(players)

    print(*players, sep='\n')


if __name__ == '__main__':
    main()
