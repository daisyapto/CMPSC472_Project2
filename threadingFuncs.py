# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
import pandas as pd
import concurrent.futures
from visual import Visual
from sorting import Sorting
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
    def callSortFunction(self, data, numOfThreads, sortBY, functionName):
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
                thread = threading.Thread(target=sort.selectionSort, args=(dataSplit[i], sortBY, sortedMedChargesSelection,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            if functionName == 'Insertion Sort':
                thread = threading.Thread(target=sort.insertionSort, args=(dataSplit[i],sortBY, sortedMedChargesInsertion,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            '''elif functionName == 'Selection Sort': mergerSort???
                thread = threading.Thread(target=sort.mergeSort, args=(dataSplit[i],sortBY, sortedMedChargesMerge,))
                thread.daemon = True
                thread.start()
                threads.append(thread)'''
        for thread in threads:
            thread.join()

        if functionName == 'Selection Sort':
            #print("Before", sortedMedChargesSelection)
            #print("Length", len(sortedMedChargesSelection))
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
            #print("After", sortedMedChargesSelection)
            #print("Length", len(sortedMedChargesSelection))



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

        sorted_df = pd.DataFrame(sortedMedChargesSelection, columns=data.columns)
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running '{functionName}' sorting function -------")
        print("Execution Time: ", end - start)
        if functionName == 'Selection Sort':
            print("Selection Sort: ", sortedMedChargesSelection)
            return sortedMedChargesSelection
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

    def lineSearch(self, data, searchBy, searchInfo): # No thread use
        foundElements = []
        for idx, row in data.iterrows():
            if row[searchBy] == searchInfo:
                foundElements.append(row)
        return pd.DataFrame(foundElements)


    def multitLinearSearch(self, data, numOfThreads, searchBy, searchInfo): # Thread use
        rows = len(data)
        foundElements =[]
        lock = threading.Lock()
        chunks = self.dataChunk( data, numOfThreads)
        def threadSearch(chunk):
            for idx, row in chunk.iterrows():
                if row[searchBy] == searchInfo:
                    lock.acquire()
                    foundElements.append(row)
                    lock.release()

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            for chunk in chunks:
                executor.submit(threadSearch, chunk)
        return pd.DataFrame(foundElements)


    def multitBinarySearch(self, data, numOfThreads, searchBy, searchInfo):
        foundElements = []
        foundElementss= []
        res = Sorting.selectionSort(self, data, numOfThreads, searchBy,foundElements)
        low = 0
        high = len(res) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if res[mid] < searchInfo:
                low = mid + 1
            elif res[mid] > searchInfo:
                high = mid - 1
            else:
                foundElementss.append(mid)



"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""
#https://www.geeksforgeeks.org/dsa/linear-search-using-multi-threading/
#https://www.geeksforgeeks.org/python/python-program-for-binary-search/
