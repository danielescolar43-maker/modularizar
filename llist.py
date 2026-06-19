class llist:
    def __init__(self, *vals, first=None, rest=None):
        if first is not None and rest is not None:
            self.__size = rest.size + 1
            self.value = first
            self.rest = rest
        elif not vals:
            self.__size = 0
        else:
            first, *others = vals
            self.value = first
            self.rest = llist(*others)
            self.__size = 1 + self.rest.size

    @property
    def size(self):
        return self.__size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError(f"Index '{idx}' out of bound for llist with size {self.size}")
        if idx == 0:
            return self.value
        return self.rest.__getitem__(idx - 1)

    def __setitem__(self, idx, value):
        if idx < 0 or idx >= self.size:
            raise IndexError(f"Index out of bound for llist with size {self.size}")
        if idx == 0:
            self.value = value
        else:
            self.rest.__setitem__(idx - 1, value)

    def swap(self, i, j):
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            raise IndexError(f"Invalid index for list with size: {self.size}")
        self[i], self[j] = self[j], self[i]

    def insert(self, idx, value):
        if idx < 0 or idx > self.size:
            raise IndexError(f"Index out of bound for llist with size {self.size}")
        if idx == 0:
            if self.size != 0:
                self.rest = llist(first=self.value, rest=self.rest)
            else:
                self.rest = llist()
            self.value = value
            self.__size += 1
        else:
            self.rest.insert(idx - 1, value)
            self.__size += 1

    def append(self, value):
        self.insert(self.size, value)

    def __str__(self):
        as_str = "["
        for i in range(self.size):
            as_str += f"{self[i]}, "
        if as_str.endswith(" "):
            as_str = as_str[:-2]
        as_str += "]"
        return as_str
