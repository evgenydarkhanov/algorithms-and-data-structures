from typing import Any


class StaticArray:
    def __init__(self, datatype, size):
        '''
        :param datatype: expects arguments like type(5.0)
        :param size: amount of allocated cells. cannot be resized
        '''
        self.__datatype = datatype
        self.__size = size
        self.array = [None] * self.__size

    def __index_checking(self, key: int):
        if isinstance(key, int):
            if abs(key) < self.__size:
                return True
            else:
                raise IndexError('Index out of range')
        else:
            raise IndexError('Index must be integer')

    def __setitem__(self, key: int, value: Any):
        if self.__index_checking(key):
            if isinstance(value, self.__datatype):
                self.array[key] = value
            else:
                raise ValueError(f'Value type must be {self.__datatype}')

    def __delitem__(self, key):
        if self.__index_checking(key):
            self.array[key] = None

    def __getitem__(self, key):
        if self.__index_checking(key):
            return self.array[key]

    def __str__(self):
        out = '['
        for i in range(self.__size - 1):
            out += str(self.array[i]) + ', '
        out += str(self.array[-1]) + ']'
        return out

    def __len__(self):
        return self.__size

    @property
    def size(self):
        return self.__size

    @property
    def datatype(self):
        return self.__datatype


myarray = StaticArray(type(1), 5)
print(myarray)

for i in range(5):
    myarray[i] = 5 - i
print(myarray)
print(myarray[-1], myarray[4])
print(myarray[-2], myarray[3])
print(myarray[-3], myarray[2])

myarray[1] = 10
del myarray[3]
print(myarray)

print(myarray.size)
print(myarray.datatype)
