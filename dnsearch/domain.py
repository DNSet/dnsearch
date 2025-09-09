# coding:utf-8

from string import ascii_letters
from string import digits
from typing import Iterator
from typing import List


class Label():
    VALID_CHARACTERS = ascii_letters + digits + '-'

    def __init__(self, label: str):
        if not label:
            raise ValueError("Empty label")

        for char in label:
            if char not in self.VALID_CHARACTERS:
                raise ValueError(f"Invalid character: {char}")

        self.__value: str = label

    @property
    def value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: object) -> bool:
        return self.value == str(other)


class Name():

    def __init__(self, name: str):
        if name[-1] == '.':
            name = name[:-1]

        self.__labels: List[Label] = [Label(char) for char in name.split('.')]

    def __iter__(self) -> Iterator[Label]:
        return reversed(self.__labels)

    def __len__(self) -> int:
        return len(self.__labels)

    def __str__(self):
        return '.'.join(label.value for label in self.__labels)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __eq__(self, other: object) -> bool:
        name: Name = other if isinstance(other, Name) else Name(str(other))
        return self.like(name) and len(self) == len(name)

    def __lt__(self, other: object) -> bool:
        name: Name = other if isinstance(other, Name) else Name(str(other))
        return self.like(name) and len(self) < len(name)

    def __le__(self, other: object) -> bool:
        name: Name = other if isinstance(other, Name) else Name(str(other))
        return self.like(name) and len(self) <= len(name)

    def __gt__(self, other: object) -> bool:
        name: Name = other if isinstance(other, Name) else Name(str(other))
        return self.like(name) and len(self) > len(name)

    def __ge__(self, other: object) -> bool:
        name: Name = other if isinstance(other, Name) else Name(str(other))
        return self.like(name) and len(self) >= len(name)

    def like(self, other: "Name") -> bool:
        a: List[Label] = list(self)
        b: List[Label] = list(other)
        length: int = min(len(a), len(b))
        return all(a[i] == b[i] for i in range(length))
