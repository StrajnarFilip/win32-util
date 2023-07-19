from typing import Union
from win32_util.window.actions import *


def window_by_name(class_name: Union[str, None], window_name: Union[str,
                                                                    None]):
    return Win32Window(find_window_w(class_name, window_name))


def window_in_foreground():
    return Win32Window(get_foreground_window())


class Win32Window:

    def __init__(self, window_handle: int):
        self.window_handle = window_handle

    def set_foreground(self):
        set_foreground_window(self.window_handle)

    def minimize(self):
        minimize_window(self.window_handle)

    def destroy(self):
        """
        TODO: Does not appear to work.
        """
        destroy_window(self.window_handle)
