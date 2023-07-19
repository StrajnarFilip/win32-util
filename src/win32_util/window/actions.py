from ctypes import windll
from typing import Union
from win32_util.thread import current_thread_id, thread_id_of_window


def find_window_w(class_name: Union[str, None],
                  window_name: Union[str, None]) -> int:
    """
    Calls `FindWindowW`. from `winuser.h`.
    You can set either (but not both) to `None`.
    Returns window handle.
    
    More information on:
    https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
    """
    return windll.User32.FindWindowW(class_name, window_name)


def get_foreground_window() -> int:
    return windll.User32.GetForegroundWindow()


def set_foreground_window(window_handle: int):
    """
    Sets the window to foreground. Pass in window handle.
    """
    current_foreground_window = get_foreground_window()

    if current_foreground_window == window_handle:
        # Cancle if it's already in foreground.
        return

    current_thread: int = current_thread_id()
    window_thread_id = thread_id_of_window(current_foreground_window)
    windll.User32.AttachThreadInput(window_thread_id, current_thread, True)
    windll.User32.BringWindowToTop(window_handle)
    windll.User32.ShowWindow(window_handle, 5)
    windll.User32.AttachThreadInput(window_thread_id, current_thread, False)


def minimize_window(window_handle: int) -> int:
    return windll.User32.CloseWindow(window_handle)


def destroy_window(window_handle: int) -> int:
    return windll.User32.DestroyWindow(window_handle)
