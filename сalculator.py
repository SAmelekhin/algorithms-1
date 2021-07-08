from operator import add, floordiv, mul, sub
from typing import List

OPERATORS = {
        '+': add,
        '-': sub,
        '/': floordiv,
        '*': mul
        }


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item: int):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('Stack is empty')


def calculator(stack, elem_list: List[str]):
    for elem in elem_list:
        if elem not in OPERATORS:
            stack.push(int(elem))
        else:
            a, b = stack.pop(), stack.pop()
            stack.push(OPERATORS[elem](b, a))

    return stack.pop()


def main():
    stack = Stack()
    elem_list = list(map(str, input().split()))
    print(calculator(stack, elem_list))


if __name__ == '__main__':
    main()
