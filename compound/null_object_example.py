"""
Chain of Responsibility + Null Object implementation.
"""

import abc


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self):
        pass


class ConcreteHandler1(Handler):

    def handle_request(self):
        if True:  # if can_handle:
            pass
        else:
            self._successor.handle_request()


class ConcreteHandler2(Handler):

    def handle_request(self):
        if False:  # if can_handle:
            pass
        else:
            self._successor.handle_request()


class NullHandler(Handler):

    def handle_request(self):
        pass  # do_nothing


def main():
    null_handler = NullHandler()
    concrete_handler_1 = ConcreteHandler1(null_handler)
    concrete_handler_2 = ConcreteHandler2(concrete_handler_1)
    concrete_handler_2.handle_request()


if __name__ == "__main__":
    main()
