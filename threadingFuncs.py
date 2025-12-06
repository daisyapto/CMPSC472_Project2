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
sort = Sorting()

class Thread:
    def callSortFunction(self, data, numOfThreads, functionName):
        threads = []
        global sortedMedChargesSelection
        global sortedMedChargesInsertion
        global sortedMedChargesMerge
        start = time.perf_counter_ns()
        dataSplit = self.dataChunk(data, numOfThreads)
        # for item in dataSplit:
            # print("Data Chunk ", item)
        # print("DATA SPLIT", dataSplit)
        for i in range(numOfThreads):
            if functionName == 'Selection Sort':
                thread = threading.Thread(target=sort.selectionSort, args=(dataSplit[i], sortedMedChargesSelection,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            if functionName == 'Insertion Sort':
                thread = threading.Thread(target=sort.insertionSort, args=(dataSplit[i], sortedMedChargesInsertion,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            elif functionName == 'Selection Sort':
                thread = threading.Thread(target=sort.mergeSort, args=(dataSplit[i], sortedMedChargesMerge,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()




        if functionName == 'Selection Sort':
            print("Before", sortedMedChargesSelection)
            print("Length", len(sortedMedChargesSelection))
            if numOfThreads == 2:
                sortedMedChargesSelection = sort.listMerging(sortedMedChargesSelection[0], sortedMedChargesSelection[1])
            if numOfThreads == 4:
                # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
                sortedMedChargesSelection1 = sort.listMerging(sortedMedChargesSelection[0], sortedMedChargesSelection[1])
                sortedMedChargesSelection2 = sort.listMerging(sortedMedChargesSelection[2], sortedMedChargesSelection[3])
                sortedMedChargesSelection = sort.listMerging(sortedMedChargesSelection1, sortedMedChargesSelection2)
            if numOfThreads == 8:
                # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
                # Must merge 2 lists at a time, unsure how to modify the listMerging function to merge k lists
                sortedMedChargesSelection1 = sort.listMerging(sortedMedChargesSelection[0], sortedMedChargesSelection[1])
                sortedMedChargesSelection2 = sort.listMerging(sortedMedChargesSelection[2], sortedMedChargesSelection[3])
                sortedMedChargesSelection3 = sort.listMerging(sortedMedChargesSelection[4], sortedMedChargesSelection[5])
                sortedMedChargesSelection4 = sort.listMerging(sortedMedChargesSelection[6], sortedMedChargesSelection[7])

                sortedMedChargesSelection1_2 = sort.listMerging(sortedMedChargesSelection1, sortedMedChargesSelection2)
                sortedMedChargesSelection3_4 = sort.listMerging(sortedMedChargesSelection3, sortedMedChargesSelection4)

                sortedMedChargesSelection = sort.listMerging(sortedMedChargesSelection1_2, sortedMedChargesSelection3_4)
            if numOfThreads == 16:
                x=1 # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
            print("After", sortedMedChargesSelection)
            print("Length", len(sortedMedChargesSelection))



        if functionName == 'Insertion Sort':
            print("Before", sortedMedChargesInsertion)
            print("Length", len(sortedMedChargesInsertion))
            if numOfThreads == 2:
                sortedMedChargesInsertion = sort.listMerging(sortedMedChargesInsertion[0], sortedMedChargesInsertion[1])
            if numOfThreads == 4:
                # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
                sortedMedChargesInsertion1 = sort.listMerging(sortedMedChargesInsertion[0], sortedMedChargesInsertion[1])
                sortedMedChargesInsertion2 = sort.listMerging(sortedMedChargesInsertion[2], sortedMedChargesInsertion[3])
                sortedMedChargesInsertion = sort.listMerging(sortedMedChargesInsertion1, sortedMedChargesInsertion2)
            if numOfThreads == 8:
                # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
                # Must merge 2 lists at a time, unsure how to modify the listMerging function to merge k lists
                sortedMedChargesInsertion1 = sort.listMerging(sortedMedChargesInsertion[0], sortedMedChargesInsertion[1])
                sortedMedChargesInsertion2 = sort.listMerging(sortedMedChargesInsertion[2], sortedMedChargesInsertion[3])
                sortedMedChargesInsertion3 = sort.listMerging(sortedMedChargesInsertion[4], sortedMedChargesInsertion[5])
                sortedMedChargesInsertion4 = sort.listMerging(sortedMedChargesInsertion[6], sortedMedChargesInsertion[7])

                sortedMedChargesInsertion1_2 = sort.listMerging(sortedMedChargesInsertion1, sortedMedChargesInsertion2)
                sortedMedChargesInsertion3_4 = sort.listMerging(sortedMedChargesInsertion3, sortedMedChargesInsertion4)

                sortedMedChargesInsertion = sort.listMerging(sortedMedChargesInsertion1_2, sortedMedChargesInsertion3_4)
            if numOfThreads == 16:
                x=1 # Unsure how to efficiently merge when there are more chunks than 2, this seems inefficient but it does seem to work (?)
            print("After", sortedMedChargesInsertion)
            print("Length", len(sortedMedChargesInsertion))




        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running '{functionName}' sorting function -------")
        print("Execution Time: ", end - start)
        if functionName == 'Selection Sort':
            print("Selection Sort: ", sortedMedChargesSelection)
        elif functionName == 'Insertion Sort':
            print("Insertion Sort: ", sortedMedChargesInsertion)
        elif functionName == 'Merge Sort':
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
