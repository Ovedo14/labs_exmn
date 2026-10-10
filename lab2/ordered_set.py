#----------------------------------------------------------
# Lab #2: Ordered Set Class
# Implementation of a generic ordered set class and its
# corresponding operations.
#
# Date: 23-Sep-2026
# Authors:
#           A01802924 Cesar Rodriguez
#           A01803272 Oved Cornejo
#----------------------------------------------------------

from collections.abc import Iterable, Iterator
from operator import le
from typing import cast
from unittest import result


class OrderedSet[T]:

    class Node[N]:

        prev: 'OrderedSet.Node[N]'
        info: N
        next: 'OrderedSet.Node[N]'

        # O(1)
        def __init__(self, value: N):
            self.prev = self
            self.info = value
            self.next = self

    __sentinel: 'OrderedSet.Node[T]'
    __count: int

    # O(N)
    def __init__(self, values: Iterable[T] = ()) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0

        for elem in values:
            self.add(elem)

    # O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({list(self) if self else ""})'

    # O(N)
    def __contains__(self, val: object) -> bool:
        for elem in self:
            if elem == val:
                return True
        return False

    # O(1)
    def __len__(self):
        return self.__count

    # O(N)
    def add(self, value: T) -> None:
        if not value in self:
            newNode: OrderedSet.Node[T] = OrderedSet.Node(value)
            newNode.prev = self.__sentinel.prev
            newNode.next = self.__sentinel
            self.__sentinel.prev.next = newNode
            self.__sentinel.prev = newNode
            self.__count += 1

    # O(N)
    def discard(self, val: T) -> None:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == val:
                current.next.prev = current.prev
                current.prev.next = current.next
                self.__count -= 1
                return
            current = current.next

    # O(N)
    def remove(self, val: T) -> None:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == val:
                current.next.prev = current.prev
                current.prev.next = current.next
                self.__count -= 1
                return
            current = current.next
        raise KeyError

    # O(N)
    def __iter__(self) -> Iterator[T]:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield current.info
            current = current.next

    # O(N^2)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(cast(OrderedSet[T], other)):
            return False

        for elem in self:
            if elem not in other:
                return False
        return True

    # O(N) where N = len(self)
    def __le__(self, other: 'OrderedSet[T]') -> bool:
        if self is other:
            return True
        if len(self) > len(other):
            return False

        for elem in self:
            if elem not in other:
                return False
        return True

    # O(N) where N = len(self)
    def __lt__(self, other: 'OrderedSet[T]') -> bool:
        if self is other:
            return False
        if len(self) >= len(other):
            return False

        for elem in self:
            if elem not in other:
                return False
        return True

    # O(N) where N = len(other)
    def __ge__(self, other: 'OrderedSet[T]') -> bool:
        if other is self:
            return True
        if len(self) < len(other):
            return False

        for elem in other:
            if elem not in self:
                return False
        return True

    # O(N) where N = len(other)
    def __gt__(self, other: 'OrderedSet[T]') -> bool:
        if other is self:
            return False
        if len(self) <= len(other):
            return False

        for elem in other:
            if elem not in self:
                return False
        return True

    # O(N) where N is the size of the smaller set
    def isdisjoint(self, other: 'OrderedSet[T]') -> bool:
        if self is other:
            return False

        k: OrderedSet[T] = self if len(self) < len(other) else other
        v: OrderedSet[T] = self if len(self) >= len(other) else other

        for elem in k:
            if elem in v:
                return False
        return True

    # O(N) where N = len(self)
    def __and__(self, other: 'OrderedSet[T]') -> 'OrderedSet[T]':
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    # O(N) where N = len(self)
    def __or__(self, other: 'OrderedSet[T]') -> 'OrderedSet[T]':
        result: OrderedSet[T] = OrderedSet(self)
        for elem in other:
            result.add(elem)
        return result

    # O(N) where N = len(other)
    def __sub__(self, other: 'OrderedSet[T]') -> 'OrderedSet[T]':
        result: OrderedSet[T] = OrderedSet(self)

        for elem in other:
            if elem in result:
                result.remove(elem)
        return result

    # O(N) where N = len(self) + len(other)
    def __xor__(self, other: 'OrderedSet[T]') -> 'OrderedSet[T]':
        return (self - other) | (other - self)

    # O(N^2)
    def clear(self) -> None:
        for elem in self:
            self.discard(elem)

    # O(1)
    def pop(self) -> T:
        if len(self) == 0:
            raise KeyError("pop from an empty set")

        last_node = self.__sentinel.prev
        val = last_node.info

        last_node.prev.next = self.__sentinel
        self.__sentinel.prev = last_node.prev
        self.__count -= 1

        return val


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet([2, 6, 34, 67, 90])
    print(a)
    print(len(a))
    for k in a:
        print(k)
    print(list(a))
    print('\n')

    b: OrderedSet[str] = OrderedSet('hello')

    print(b)
    print(len(b))
    for k in b:
        print(k)
    print(list(b))
    print('\n')