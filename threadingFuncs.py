# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import time
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


"""
Refer:
https://stackoverflow.com/questions/54237067/how-to-make-tkinter-gui-thread-safe
https://stackoverflow.com/questions/50525849/why-more-number-of-threads-takes-more-time-to-process
https://www.reddit.com/r/learnpython/comments/10qzto6/how_does_tkinter_multithreading_work_and_why/
"""