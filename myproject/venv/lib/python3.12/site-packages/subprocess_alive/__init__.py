import comtypes.client


def is_process_alive(pid: int) -> bool:
    r"""
    Checks if a process with the given process ID is currently running.

    Args:
        pid (int): The process ID to check.

    Returns:
        bool: True if the process is running, False otherwise.
    """
    WMI = comtypes.client.CoGetObject("winmgmts:")
    processes = WMI.InstancesOf("Win32_Process")
    if [True for pp in processes if pp.Properties_("ProcessID").Value == pid]:
        return True
    return False
