# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
from visual import Visual
from sorting import Sorting

class Thread:
    def callFunction(self, data, numOfThreads, function):
        threads = []
        start = time.perf_counter_ns()
        for i in range(numOfThreads):
            thread = threading.Thread(target=function, args=(data,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running {function} function -------")
        print("Execution Time: ", end - start)


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""
