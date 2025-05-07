# A "killable" sleep function for kthread


https://pypi.org/project/kthread/

**From kthread's pypi site:**
*Assuming that the thread is not blocked by an operating system call (such as sleep, accept, or recv), the thread will forcefully quit.*


```python
pip install kthread-sleep 
import kthread
import sys
from kthread_sleep import sleep
def func():
    try:
        sleep(2000000)
    finally:
        sys.stdout.write("Greetings from Vice City!\n")
        sys.stdout.flush()

t = kthread.KThread(target = func, name = "KillableThread1")
t.start()
sleep(.1)
print(t.is_alive())
t.kill()
sleep(.1)
print(t.is_alive())

True
Greetings from Vice City!
False


```



