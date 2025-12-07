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

sort = Sorting()
visual = Visual()

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
        if functionName == 'Bar Chart':
            figAge_B, axAge_B = plt.subplots()
            figMF_B, axMF_B = plt.subplots()
            figBMI_B, axBMI_B = plt.subplots()
            figSmoker_B, axSmoker_B = plt.subplots()
            figRegion_B, axRegion_B = plt.subplots()
            figNumOfChildren_B, axNumOfChildren_B = plt.subplots()
            figMed_B, axMed_B = plt.subplots()
        elif functionName == 'Line Chart':
            figAge_L, axAge_L = plt.subplots()
            figBMI_L, axBMI_L = plt.subplots()
            figNumOfChildren_L, axNumOfChildren_L = plt.subplots()
        elif functionName == 'Pie Chart':
            figAge_P, axAge_P = plt.subplots()
            figMF_P, axMF_P = plt.subplots()
            figBMI_P, axBMI_P = plt.subplots()
            figSmoker_P, axSmoker_P = plt.subplots()
            figRegion_P, axRegion_P = plt.subplots()
            figNumOfChildren_P, axNumOfChildren_P = plt.subplots()
            figMed_P, axMed_P = plt.subplots()

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
        plt.show()
        end = time.perf_counter_ns()
        print(f"-------- {numOfThreads} Threads running {functionName} function -------")
        print("Execution Time: ", end - start)

    def dataChunk(self, data, numOfThreads):
        dataChunks = np.array_split(data, numOfThreads)
        return dataChunks


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""