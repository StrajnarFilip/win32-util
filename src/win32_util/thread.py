from ctypes import windll
from typing import Union


def current_thread_id() -> int:
    return windll.Kernel32.GetCurrentThreadId()


def thread_id_of_window(window_handle: int,
                        process_identifier: Union[int, None] = None) -> int:
    """
    `window_handle` is a handle to the window.

    `process_identifier` is a pointer to a variable that receives the process identifier.

    More information on: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
    """
    return windll.User32.GetWindowThreadProcessId(window_handle,
                                                  process_identifier)
