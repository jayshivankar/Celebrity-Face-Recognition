# Checks if a process (pid) is alive on Windows 

### pip install subprocess-alive

#### Tested against Windows 10 / Python 3.10 / Anaconda


```python

from subprocess_alive import is_process_alive
import subprocess
from time import perf_counter
p = subprocess.Popen("ping 8.8.8.8", shell=True)

start = perf_counter()
while is_process_alive(p.pid):
    print(f"{p.pid} is alive", end="\r")
print(f"{p.pid} is not alive - execution time: {perf_counter()-start}")

start = perf_counter()
p = subprocess.Popen("ping 8.8.8.8", shell=False)
while is_process_alive(p.pid):
    print(f"{p.pid} is alive", end="\r")
print(f"{p.pid} is not alive - execution time: {perf_counter()-start}")



#output
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=9ms TTL=119
Reply from 8.8.8.8: bytes=32 time=11ms TTL=119
Reply from 8.8.8.8: bytes=32 time=9ms TTL=119
Reply from 8.8.8.8: bytes=32 time=10ms TTL=119
Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 9ms, Maximum = 11ms, Average = 9ms
18404 is not alive - execution time: 3.170662900000025
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=10ms TTL=119
Reply from 8.8.8.8: bytes=32 time=9ms TTL=119
Reply from 8.8.8.8: bytes=32 time=10ms TTL=119
Reply from 8.8.8.8: bytes=32 time=9ms TTL=119
Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 9ms, Maximum = 10ms, Average = 9ms
6788 is not alive - execution time: 3.1898495000023104

```