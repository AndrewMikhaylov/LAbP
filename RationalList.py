from Rational import Rational


class RationalList(list):
    def __init__(self, iterable):
        super().__init__(self._validate_ratioanl(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self._validate_ratioanl(item))

    def insert(self, index, item):
        super().insert(index, self._validate_ratioanl(item))

    def append(self, item):
        super().append(self._validate_ratioanl(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(self._validate_ratioanl(item) for item in other)

    def __len__(self):
        return super(RationalList, self).__len__()

    def __add__(self, other):
        if isinstance(other, RationalList):
            self.extend(other)
        elif isinstance(other, Rational):
            self.append(other)
        elif isinstance(other, int):
            self.append(int)

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.extend(other)
        elif isinstance(other, Rational):
            self.append(other)
        elif isinstance(other, int):
            self.append(int)

    #ітерація
    def __iter__(self):
        list = self._rearrange_list()
        self.current_index = 0
        return list

    def __next__(self):
        if self.current_index < len(self):
            x = self[self.current_index]
            self.current_index += 1
            return x
        raise StopIteration

    def _rearrange_list(self):
        i=0
        list = self
        list.sort(key=lambda element: element.n)
        return list

    def _validate_ratioanl(self, value):
        if isinstance(value, Rational):
            return value
        raise TypeError(f"Rational value expected, got {type(value).__name__}")


