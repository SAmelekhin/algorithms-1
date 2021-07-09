class DequeIsFullError(Exception):
    pass


class DequeIsEmptyError(Exception):
    pass


class Deque:
    def __init__(self, n: int):
        self.__deque_list = [None] * n
        self.__max_n = n
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def calc_index(self, var: int, val: int) -> int:
        if val:
            return (var + 1) % self.__max_n
        else:
            return (var - 1) % self.__max_n

    def push_front(self, value: int):
        if self.__size == self.__max_n:
            raise DequeIsFullError
        self.__deque_list[self.__front - 1] = value
        self.__front = self.calc_index(self.__front, 0)
        self.__size += 1

    def push_back(self, value: int):
        if self.__size == self.__max_n:
            raise DequeIsFullError
        self.__deque_list[self.__back] = value
        self.__back = self.calc_index(self.__back, 1)
        self.__size += 1

    def pop_front(self):
        if self.__is_empty():
            raise DequeIsEmptyError
        front = self.__deque_list[self.__front]
        self.__deque_list[self.__front] = None
        self.__front = self.calc_index(self.__front, 1)
        self.__size -= 1
        return front

    def pop_back(self):
        if self.__is_empty():
            raise DequeIsEmptyError
        back = self.__deque_list[self.__back - 1]
        self.__deque_list[self.__back - 1] = None
        self.__back = self.calc_index(self.__back, 0)
        self.__size -= 1
        return back


def command_handler(deque):
    cmd, *args = input().split()
    try:
        return getattr(deque, cmd)(*args)
    except AttributeError:
        raise ValueError('Invalid value')
    except (DequeIsFullError, DequeIsEmptyError):
        return 'error'


def main():
    num_cmd = int(input())
    deque = Deque(int(input()))
    for _ in range(num_cmd):
        result = command_handler(deque)
        if result:
            print(result)


if __name__ == '__main__':
    main()
