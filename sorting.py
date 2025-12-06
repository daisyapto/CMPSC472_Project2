# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading

class Sorting:

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()

    def selectionSort(self, data, globalList):
        print("Test, inside selection sort function")
        charges = list(data['charges'])
        for i in range (len(charges)):
            for j in range (i+1, len(charges)):
                if charges[j] < charges[i]:
                    charges[j], charges[i] = charges[i], charges[j]

        self.lock1.acquire()
        globalList.extend(charges)
        self.lock1.release()

    def insertionSort(self, data, globalList):
        charges = data['charges']
        for i in range (len(charges)):
            for j in range (len(charges)-1, 0):
                if charges[j] > charges[i]:
                    charges[j] = None # Still working on this

        self.lock2.acquire()
        globalList.extend([charges])
        self.mergeForNonMergeSortSorting(globalList)
        self.lock2.release()

    def mergeForNonMergeSortSorting(self, dataList):
        # Had an idea
        # Was having an issue where selection sort was return two sorted halves when 2 threads were used for example [1, 2, 4, 3, 5, 6], so it reminded of the merge mergesort function
        # Used it in selection sort to produce the proper results
        # Note -- does not fully work yet
        result = []
        for item in range(1, len(dataList)):
            for i in range(len(dataList[item])):
                if dataList[item][i] > dataList[item][i-1]:
                    result.append(dataList[item][i])




    def merge(self, data, left, middle, right):
        left = 0

    def mergeSort(self, data, globalList):
        charges=1 # Placeholder
        #...
        self.lock3.acquire()
        globalList.extend(charges)
        self.lock3.release()