from typing import Any


class DynamicArray:
    def __init__(self, datatype):
        '''
        :param datatype: expects arguments like type(5.0)
        '''
        self.__datatype = datatype
        self.__size = 0
        self.__capacity = 1
        self.array = self.__make_array(self.__capacity)

    @staticmethod
    def __make_array(new_capacity):
        new_array = [None] * new_capacity
        return new_array

    def __reallocate(self):
        new_capacity = self.__capacity * 2
        new_array = self.__make_array(new_capacity)
        for i in range(self.__size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.__capacity = new_capacity
        return self.array

    def append(self, value):
        if isinstance(value, self.__datatype):
            if self.__size == self.__capacity:
                self.__reallocate()
            self.array[self.__size] = value
            self.__size += 1
        else:
            raise ValueError(f'Value type must be {self.__datatype}')

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
                if key < 0:
                    key = self.__size - key
                self.array[key] = value
            else:
                raise ValueError(f'Value type must be {self.__datatype}')

    def __delitem__(self, key):
        if self.__index_checking(key):
            if key < 0:
                key = self.__size - key
            self.array[key] = None

    def __getitem__(self, key):
        if self.__index_checking(key):
            if key < 0:
                key = self.__size + key
            return self.array[key]

    def __str__(self):
        out = '['
        for i in range(self.__size - 1):
            out += str(self.array[i]) + ', '
        out += str(self.array[self.__size - 1]) + ']'
        return out

    def __len__(self):
        return self.__size

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__size

    @property
    def datatype(self):
        return self.__datatype


myarray = DynamicArray(type(1))
for i in range(9):
    myarray.append(i)

print(myarray)
for i in range(len(myarray)-1, -1, -1):
    print(myarray[i], end='\t')
print()
print(f'size = {myarray.size}')
print(f'capacity = {myarray.capacity}')
print(f'data type = {myarray.datatype}')
