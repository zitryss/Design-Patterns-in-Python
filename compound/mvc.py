"""
Separate the areas of responsibility to maintain loose coupling and for
the maintainability of the software.
"""


class Model:
    """
    Provide access to data and business logic.
    """

    def some_operation(self):
        return None


class View:
    """
    Represent the user interface.
    """

    def some_operation(self, arg):
        pass


class Controller:
    """
    Glue Model and View together.
    """

    def __init__(self):
        self._model = Model()
        self._view = View()

    def some_operation(self):
        data = self._model.some_operation()
        self._view.some_operation(data)


def main():
    controller = Controller()
    controller.some_operation()


if __name__ == "__main__":
    main()
