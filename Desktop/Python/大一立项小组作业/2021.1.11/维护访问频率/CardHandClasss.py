class CardHand:

    class _Node:
        __slots__ = '_next', '_element'

        def __init__(self, e):
            self._element = e
            self._next = None

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')

        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._heart = self.Position(self, self._Node(None))
        self._clubs = self.Position(self, self._Node(None))
        self._spades = self.Position(self, self._Node(None))
        self._diamonds = self.Position(self, self._Node(None))
        self._suite = [self._heart, self._clubs, self._spades, self._diamonds]

    def heart(self):
        return self._heart

    def clubs(self):
        return self._clubs

    def spades(self):
        return self._spades

    def diamonds(self):
        return self._diamonds

    def add_card(self, r, s):
        s = self._validate(s)
        temp = self._Node(r)
        temp._next = s._next
        s._next = temp
        return self._make_position(temp)

    def play(self, s):
        s = self._validate(s)
        if s._next == None:
            for i in self._suite:
                temp = self._validate(i)
                if temp._next != None:
                    s = temp
                    break
        if s._next == None:
            raise Exception('Empty List')
        temp = s._next
        s._next = temp._next
        temp._next = None
        return temp

    def __iter__(self):
        for i in self._suite:
            temp = self._validate(i)
            while temp._next != None:
                temp = temp._next
                yield temp._element

    def all_of_suit(self, s):
        res = []
        temp = self._validate(s)
        while temp._next != None:
            temp = temp._next
            res.append(temp._element)
        return res