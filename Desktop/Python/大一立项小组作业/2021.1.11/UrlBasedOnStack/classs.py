class Empty(Exception):
    pass

class ArrayStack():
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def openWeb(self,e):
        self._data.append(e)

    def lastWebName(self):
        if self.is_empty():
            raise Empty('This is the first web.')
        return self._data[-1]

    def backWeb(self):
        if self.is_empty():
            raise Empty('This is the first web.')
        return self._data.pop()

    def __str__(self):
        return self._data