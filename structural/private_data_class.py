"""
Control write access to class attributes.
Separate data from methods that use it.
Encapsulate class data initialization.
"""


class DataClass:
    """
    Hide all the attributes.
    """

    def __init__(self, value):
        vars(self).update({"value": value})

    def __setattr__(self, name, value):
        raise AttributeError


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    def __init__(self, value):
        self._data = DataClass(value)


def main():
    m2 = MainClass("test")
    assert m2._data.value == "test"


if __name__ == "__main__":
    main()
