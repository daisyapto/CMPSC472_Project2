# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
import tkinter

from visual import Visual
from sorting import Sorting
import numpy as np
import heapq
from matplotlib.figure import Figure
import pandas as pd
import concurrent.futures

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
        print(f"Execution Time: {end-start:,} ns")
        if functionName == 'Selection Sort':
            print("Selection Sort: ", sortedMedChargesSelection)
        elif functionName == 'Insertion Sort':
            print("Insertion Sort: ", sortedMedChargesInsertion)
        #elif functionName == 'Merge Sort':
            #print("Merge Sort: ", sortedMedChargesMerge)
        return (end - start), sortedMedChargesSelection, sortedMedChargesInsertion

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
        print(f"Execution Time: {end-start:,} ns")
        return (end - start)

    def dataChunk(self, data, numOfThreads):
        dataChunks = np.array_split(data, numOfThreads)
        return dataChunks

    def multitLinearSearch(self, data, numOfThreads, searchBy, searchInfo):
        foundElements = []
        lock = threading.Lock()
        chunks = self.dataChunk(data, numOfThreads)
        is_numeric = searchBy in ["age", "bmi", "charges"] # if numeric

        def threadSearch(chunk):
            localFound = []

            if is_numeric:
                search_val = float(searchInfo)
                if searchBy == "charges":
                    search_lower = search_val * 1000
                    search_upper = search_lower + 10000
                else:
                    search_lower = search_val
                    search_upper = search_val + 1.0

                for idx in range(len(chunk)):
                    val = float(chunk.iloc[idx][searchBy])
                    if search_lower <= val < search_upper:
                        localFound.append(chunk.iloc[idx])
            else:
                for idx in range(len(chunk)):
                    if str(chunk.iloc[idx][searchBy]) == searchInfo:
                        localFound.append(chunk.iloc[idx])

            if localFound:
                lock.acquire()
                foundElements.extend(localFound)
                lock.release()

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            executor.map(threadSearch, chunks)

        if foundElements:
            return pd.DataFrame(foundElements)
        else:
            return pd.DataFrame()

    def multitBinarySearch(self, data, numOfThreads, searchBy, searchInfo):
        foundElements = []
        lock = threading.Lock()

        sortedData = data.sort_values(by=searchBy).reset_index(drop=True)
        chunks = self.dataChunk(sortedData, numOfThreads)
        is_numeric = searchBy in ["age", "bmi", "charges"]

        def threadSearch(chunk):
            if len(chunk) == 0:
                return

            localFound = []

            if is_numeric:
                search_val = float(searchInfo)

                if searchBy == "charges":
                    search_lower = search_val * 1000
                    search_upper = search_lower + 10000
                else:
                    search_lower = search_val
                    search_upper = search_val + 1.0

                temp_low, temp_high = 0, len(chunk) - 1
                first_idx = -1

                while temp_low <= temp_high:
                    mid = (temp_low + temp_high) // 2
                    mid_val = float(chunk.iloc[mid][searchBy])

                    if mid_val >= search_lower:
                        first_idx = mid
                        temp_high = mid - 1
                    else:
                        temp_low = mid + 1

                if first_idx != -1:
                    idx = first_idx
                    while idx < len(chunk):
                        val = float(chunk.iloc[idx][searchBy])
                        if val < search_upper:
                            localFound.append(chunk.iloc[idx])
                            idx += 1
                        else:
                            break

            else:
                search_str = str(searchInfo)
                low, high = 0, len(chunk) - 1

                while low <= high:
                    mid = (low + high) // 2
                    value = str(chunk.iloc[mid][searchBy])

                    if value < search_str:
                        low = mid + 1
                    elif value > search_str:
                        high = mid - 1
                    else:
                        left = mid
                        while left >= 0 and str(chunk.iloc[left][searchBy]) == search_str:
                            localFound.append(chunk.iloc[left])
                            left -= 1

                        right = mid + 1
                        while right < len(chunk) and str(chunk.iloc[right][searchBy]) == search_str:
                            localFound.append(chunk.iloc[right])
                            right += 1
                        break

            if localFound:
                lock.acquire()
                foundElements.extend(localFound)
                lock.release()

        with concurrent.futures.ThreadPoolExecutor(max_workers=numOfThreads) as executor:
            executor.map(threadSearch, chunks)

        if foundElements:
            return pd.DataFrame(foundElements)
        else:
            return pd.DataFrame()


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""
