# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
from visual import Visual
from sorting import Sorting
import numpy as np
from matplotlib import pyplot as plt
import heapq
import concurrent.futures
import pandas as pd

# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import tkinter

from visual import Visual
from sorting import Sorting
import numpy as np
from matplotlib import pyplot as plt
import heapq
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sort = Sorting()
visual = Visual()

figAge_B = Figure((4, 4), dpi=100)
axAge_B = figAge_B.add_subplot(111)
figMF_B = Figure((4, 4), dpi=100)
axMF_B = figMF_B.add_subplot(111)
figBMI_B = Figure((4, 4), dpi=100)
axBMI_B = figBMI_B.add_subplot(111)
figSmoker_B = Figure((4, 4), dpi=100)
axSmoker_B = figSmoker_B.add_subplot(111)
figRegion_B = Figure((4, 4), dpi=100)
axRegion_B = figRegion_B.add_subplot(111)
figNumOfChildren_B = Figure((4, 4), dpi=100)
axNumOfChildren_B = figNumOfChildren_B.add_subplot(111)
figMed_B = Figure((4, 4), dpi=100)
axMed_B = figMed_B.add_subplot(111)

figAge_L = Figure((4,4), dpi=100)
axAge_L = figAge_L.add_subplot(111)
figBMI_L = Figure((4,4), dpi=100)
axBMI_L = figBMI_L.add_subplot(111)
figNumOfChildren_L = Figure((4,4), dpi=100)
axNumOfChildren_L = figNumOfChildren_L.add_subplot(111)

figAge_P = Figure((4,4), dpi=100)
axAge_P = figAge_P.add_subplot(111)
figMF_P = Figure((4,4), dpi=100)
axMF_P = figMF_P.add_subplot(111)
figBMI_P = Figure((4,4), dpi=100)
axBMI_P = figBMI_P.add_subplot(111)
figSmoker_P = Figure((4,4), dpi=100)
axSmoker_P = figSmoker_P.add_subplot(111)
figRegion_P = Figure((4,4), dpi=100)
axRegion_P = figRegion_P.add_subplot(111)
figNumOfChildren_P = Figure((4,4), dpi=100)
axNumOfChildren_P = figNumOfChildren_P.add_subplot(111)
figMed_P = Figure((4,4), dpi=100)
axMed_P = figMed_P.add_subplot(111)

class Thread:
    def callSortFunction(self, data, numOfThreads, functionName):
        threads = []
        sortedMedChargesSelection = []
        sortedMedChargesInsertion = []
        # sortedMedChargesMerge = []
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
            #elif functionName == 'Merge Sort':
                #thread = threading.Thread(target=sort.mergeSort, args=(dataSplit[i], sortedMedChargesMerge,))
                #thread.daemon = True
                #thread.start()
                #threads.append(thread)
        for thread in threads:
            thread.join()

        if functionName == 'Selection Sort':
            #print("Before", sortedMedChargesSelection)
            #print("Length", len(sortedMedChargesSelection))
            sortedMedChargesSelection = list(heapq.merge(*sortedMedChargesSelection))
            #print("After", sortedMedChargesSelection)
            #print("Length", len(sortedMedChargesSelection))

        if functionName == 'Insertion Sort':
            #print("Before", sortedMedChargesInsertion)
            #print("Length", len(sortedMedChargesInsertion))
            sortedMedChargesInsertion = list(heapq.merge(*sortedMedChargesInsertion))
            #print("After", sortedMedChargesInsertion)
            #print("Length", len(sortedMedChargesInsertion))

        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running '{functionName}' sorting function -------")
        print("Execution Time: ", end - start)
        if functionName == 'Selection Sort':
            print("Selection Sort: ", sortedMedChargesSelection)
        elif functionName == 'Insertion Sort':
            print("Insertion Sort: ", sortedMedChargesInsertion)
        #elif functionName == 'Merge Sort':
            #print("Merge Sort: ", sortedMedChargesMerge)

    def callVisualFunction(self, data, numOfThreads, functionName):
        threads = []
        start = time.perf_counter_ns()
        # print("DATA SPLIT", dataSplit)
        for i in range(numOfThreads):
            if functionName == 'Pie Chart':
                thread = threading.Thread(target=visual.drawAllPieGraphs, args=(data, axAge_P, axMF_P, axBMI_P, axSmoker_P, axRegion_P, axNumOfChildren_P, axMed_P,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            if functionName == 'Line Chart':
                thread = threading.Thread(target=visual.drawAllLineGraphs, args=(data, axAge_L, axBMI_L, axNumOfChildren_L,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
            elif functionName == 'Bar Chart':
                thread = threading.Thread(target=visual.drawAllBarGraphs, args=(data, axAge_B, axMF_B, axBMI_B, axSmoker_B, axRegion_B, axNumOfChildren_B, axMed_B,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        # Add Figures to tkinter in main
        # plt.show()
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running {functionName} function -------")
        print("Execution Time: ", end - start)

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
        chunks = self.dataChunk(data, numOfThreads)
        def threadSearch(chunk):
            for idx, row in chunk.iterrows():
                if str(row[searchBy]) == str(searchInfo):
                    lock.acquire()
                    foundElements.append(row)
                    lock.release()

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            for chunk in chunks:
                executor.submit(threadSearch, chunk)


        return pd.DataFrame(foundElements)

    '''
    def binarySearch(self,data, numOfThreads, searchBy, searchInfo):
        sortedData = thread.callSortFunction(data, numOfThreads, "Insertion Sort")
        low = 0
        high = len(sortedData) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if sortedData[mid] < x:
                low = mid + 1
            elif sortedData[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1'''

    def multitBinarySearch(self, data, numOfThreads, searchBy, searchInfo):
        foundElements = []
        lock = threading.Lock()

        # Binary requires sorted data
        sortedData = data.sort_values(by=searchBy).reset_index(drop=True)

        chunks = self.dataChunk(sortedData, numOfThreads)

        def threadSearch(chunk):
            low = 0
            high = len(chunk) - 1

            while low <= high:
                mid = (low + high) // 2
                value = chunk.loc[mid, searchBy]

                if str(value) < str(searchInfo):
                    low = mid + 1
                elif str(value) > str(searchInfo):
                    high = mid - 1
                else:
                    # Lock before modifying shared list
                    lock.acquire()
                    foundElements.append(chunk.iloc[mid])
                    lock.relase ()
                    return  # exit thread

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            executor.map(threadSearch, chunks)

        return pd.DataFrame(foundElements)


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""
#https://www.geeksforgeeks.org/dsa/linear-search-using-multi-threading/
#https://www.geeksforgeeks.org/python/python-program-for-binary-search/
#https://www.geeksforgeeks.org/dsa/binary-search-using-pthread/
