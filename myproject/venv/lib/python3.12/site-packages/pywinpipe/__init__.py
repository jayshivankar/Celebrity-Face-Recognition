import ctypes
from ctypes import LibraryLoader, WinDLL
from time import sleep
windll = LibraryLoader(WinDLL)
user32 = windll.user32
kernel32 = windll.kernel32

PIPE_ACCESS_DUPLEX = 0x00000003
PIPE_TYPE_MESSAGE = 0x00000004
PIPE_READMODE_MESSAGE = 0x00000002
PIPE_WAIT = 0x00000000

INVALID_HANDLE_VALUE = -1

class Write2Pipe:
    r"""
    A class for writing messages to a named pipe.

    Methods:
    - __init__: Initializes the Write2Pipe instance and creates a named pipe.
    - __enter__: Enters a context manager and returns the Write2Pipe instance.
    - __exit__: Exits the context manager and closes the named pipe.
    - write_message: Writes a message to the named pipe.
    - close_pipe: Closes the named pipe.

    """
    def __init__(
        self,
        pipename=r"\\.\pipe\example",
        nMaxInstances=1,
        nOutBufferSize=65536,
        nInBufferSize=65536,
        timeout=0,
            block_or_nonblock='block',
    ):
        r"""
        Initializes the Write2Pipe instance and creates a named pipe.

        Args:
        - pipename (str): The name of the named pipe to be created. Defaults to "\\.\pipe\example".
        - nMaxInstances (int): The maximum number of instances that can connect to the named pipe. Defaults to 1.
        - nOutBufferSize (int): The size of the output buffer for the named pipe. Defaults to 65536.
        - nInBufferSize (int): The size of the input buffer for the named pipe. Defaults to 65536.
        - timeout (int): The timeout value for waiting on the named pipe connection. Defaults to 0 (no timeout).
        - block_or_nonblock (str): valid options block/unblock Defaults to block.

        Note: The nMaxInstances, nOutBufferSize, and nInBufferSize parameters should match the corresponding values used when creating the named pipe.
        """
        self.nMaxInstances = nMaxInstances
        self.nOutBufferSize = nOutBufferSize
        self.nInBufferSize = nInBufferSize
        self.pipename = pipename
        self.timeout = timeout
        self.pipe = kernel32.CreateNamedPipeW(
            self.pipename,
            PIPE_ACCESS_DUPLEX,
            PIPE_TYPE_MESSAGE | PIPE_READMODE_MESSAGE | 0x00000001 if block_or_nonblock=='unblock' else 0x00000000,
            self.nMaxInstances,
            self.nOutBufferSize,
            self.nInBufferSize,
            0,
            None,
        )
        print("Waiting for client[s]")
        ctypes.windll.kernel32.ConnectNamedPipe(self.pipe, None)
        print("Client[s] connected")

    def __enter__(self):
        """
        Enters a context manager and returns the Write2Pipe instance.

        Returns:
        - Write2Pipe: The Write2Pipe instance itself.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exits the context manager and closes the named pipe.

        Args:
        - exc_type (type): The type of the exception raised, if any.
        - exc_value (Exception): The exception instance raised, if any.
        - traceback (traceback): The traceback object associated with the exception, if any.
        """
        try:
            self.close_pipe()
        except Exception as fe:
            print(fe)

    def write_message(self, data):
        """
        Writes a message to the named pipe.

        Args:
        - data (bytes): The message to be written to the named pipe.

        """
        bytes_written = ctypes.c_ulong(0)
        ctypes.windll.kernel32.WriteFile(
            self.pipe, data, len(data), ctypes.byref(bytes_written), None
        )

    def close_pipe(self):
        """
        Closes the named pipe.
        """
        ctypes.windll.kernel32.CloseHandle(self.pipe)


class ReadFromPipe:
    r"""
    A class for reading messages from a named pipe.

    Methods:
    - __init__: Initializes the ReadFromPipe instance and connects to the named pipe.
    - __enter__: Enters a context manager and returns the ReadFromPipe instance.
    - __exit__: Exits the context manager and closes the named pipe.
    - read_message: Reads a message from the named pipe.
    - close_pipe: Closes the named pipe.

    """
    def __init__(self, pipename=r"\\.\pipe\example"):
        r"""
        Initializes the ReadFromPipe instance and connects to the named pipe.

        Args:
        - pipename (str): The name of the named pipe to connect to. Defaults to "\\.\pipe\example".
        """
        while True:
            try:
                self.pipename = pipename
                self.handle = ctypes.windll.kernel32.CreateFileW(
                    self.pipename,
                    ctypes.c_ulong(
                        0x80000000 | 0x40000000
                    ),  # GENERIC_READ | GENERIC_WRITE
                    0,
                    None,
                    ctypes.c_ulong(3),  # OPEN_EXISTING
                    0,
                    None,
                )
                self.mode = ctypes.c_ulong(PIPE_READMODE_MESSAGE )
                self.res = ctypes.windll.kernel32.SetNamedPipeHandleState(
                    self.handle, ctypes.byref(self.mode), None, None
                )
                break
            except Exception as fe:
                print(fe)
                continue

    def __enter__(self):
        """
        Enters a context manager and returns the ReadFromPipe instance.

        Returns:
        - ReadFromPipe: The ReadFromPipe instance itself.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        r"""
        Exits the context manager and closes the named pipe.

        Args:
        - exc_type (type): The type of the exception raised, if any.
        - exc_value (Exception): The exception instance raised, if any.
        - traceback (traceback): The traceback object associated with the exception, if any.
        """
        try:
            self.close_pipe()
        except Exception as fe:
            print(fe)

    def read_message(self, buffer_size=65536, sleep_when_error=1):
        r"""
        Reads a message from the named pipe.

        Args:
        - buffer_size (int): The size of the buffer used for reading the message. Defaults to 65536.
        - sleep_when_error (int): The sleep duration in seconds when encountering an error while reading. Defaults to 1.

        Yields:
        - tuple: A tuple containing the received message (str) and the length of the message (int).

        Note: The received message may be truncated if its length exceeds the buffer size.
        """
        while True:
            try:
                resp = (ctypes.c_char * buffer_size)()
                bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadFile(
                    self.handle,
                    resp,
                    buffer_size,
                    ctypes.byref(bytes_read),
                    None,
                )
                yield resp.value, bytes_read.value # value, and len of values read
            except Exception as e:
                print("Pipe not found, waiting ...")
                sleep(sleep_when_error)

    def close_pipe(self):
        """
        Closes the named pipe.
        """
        ctypes.windll.kernel32.CloseHandle(self.handle)

