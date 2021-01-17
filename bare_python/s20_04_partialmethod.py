#!python3

from functools import partialmethod


class A:

    def __init__(self, msg: str) -> None:
        self._msg = msg

    def show_message(self) -> None:
        print(self._msg)

    def update_message(self, msg: str) -> None:
        self._msg = msg

    default_message = partialmethod(
        update_message, "DEFAULT_MESSAGE_RIGHT_HERE_RIGHT_NOW")


a = A("Anne had three apples.")
a.show_message()

a.update_message("Anne had no more apples!")
a.show_message()

a.default_message()
a.show_message()
