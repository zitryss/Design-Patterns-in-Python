class ValueObject:

    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return vars(self) == vars(other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return vars(self) != vars(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(vars(self).values()))

    @classmethod
    def operation(cls, value):
        return cls(value)


def main():
    value_object1 = ValueObject(0)
    value_object2 = ValueObject(0)
    assert value_object1 == value_object2
    assert id(value_object1) != id(value_object2)


if __name__ == "__main__":
    main()
