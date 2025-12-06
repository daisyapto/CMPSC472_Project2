# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
from visual import Visual
from sorting import Sorting
import numpy as np

sortedMedChargesSelection = []
sortedMedChargesInsertion = []
sortedMedChargesMerge = []

class Thread:
    def callSortFunction(self, data, numOfThreads, function):
        threads = []
        global sortedMedChargesSelection
        global sortedMedChargesInsertion
        global sortedMedChargesMerge
        start = time.perf_counter_ns()
        dataSplit = self.dataChunk(data, numOfThreads)
        for item in dataSplit:
            print("Data Chunk ", item)
        # print("DATA SPLIT", dataSplit)
        for i in range(numOfThreads):
            thread = threading.Thread(target=function, args=(dataSplit[i], sortedMedChargesSelection))
            thread.daemon = True
            thread.start()
            threads.append(thread)
            """ Getting error when trying to check which function is being passed, probably in the if statement
            if function == Sorting.insertionSort:
                thread = threading.Thread(target=function, args=(dataSplit[i], sortedMedChargesInsertion))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            elif function == Sorting.mergeSort:
                thread = threading.Thread(target=function, args=(dataSplit[i], sortedMedChargesMerge))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            """
        for thread in threads:
            thread.join()
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running {function} sorting function -------")
        print("Execution Time: ", end - start)
        print("---------")
        print("Selection Sort: ", sortedMedChargesSelection)
        print("Insertion Sort: ", sortedMedChargesInsertion)
        print("Merge Sort: ", sortedMedChargesMerge)

    """
    def callVisualFunction(self, data, numOfThreads, function):
        threads = []
        start = time.perf_counter_ns()
        dataSplit = self.dataChunk(data, numOfThreads)
        # print("DATA SPLIT", dataSplit)
        for i in range(numOfThreads):
            thread = threading.Thread(target=function, args=(dataSplit[i],))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running {function} function -------")
        print("Execution Time: ", end - start)
    """

    def dataChunk(self, data, numOfThreads):
        dataChunks = np.array_split(data, numOfThreads)
        return dataChunks


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""
