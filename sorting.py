# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading
import pandas as pd
class Sorting:

    def __init__(self):
        self.lock = threading.Lock()

    def selectionSort(self, data, sortBY, globalList): # i changed selection to test stuff, i think slectiono might be okay its how were combine the lists at the end
        # i think there is pd.DataFrame(data) build in fucntion
        charges = data.values.tolist()
        d = data.columns.get_loc(sortBY)
        for i in range (len(charges)):
            min_index = i
            for j in range (i+1, len(charges)):
                if charges[j][d] < charges[i][d]:
                    min_index = j
            charges[i], charges[min_index] = charges[min_index], charges[i]

        self.lock.acquire()
        globalList.extend([charges])
        self.lock.release()

    # Reference: https://www.w3schools.com/dsa/dsa_algo_insertionsort.php
    def insertionSort(self, data, sortBY, globalList):
        charges = list(data[sortBY])
        for i in range(1, len(charges)):
            insertValue = i
            currentCharge = charges.pop(i)
            for j in range (i-1, 0):
                if charges[j] <= currentCharge:
                    insertValue = j
            charges.insert(insertValue, currentCharge)

        self.lock.acquire()
        globalList.extend([charges])
        self.lock.release()

    def listMerging(self, list1, list2):
        # Had an idea
        # Was having an issue where selection sort was return two sorted halves when 2 threads were used for example [1, 2, 4, 3, 5, 6], so it reminded of the merge mergesort function
        # Used it in selection sort to produce the proper results
        # Note -- does not fully work yet
        result = []
        for i in range(min(len(list1), len(list2))):
            if list1[i] <= list2[i]:
                result.append(list1[i])
                result.append(list2[i])
            elif list1[i] > list2[i]:
                result.append(list2[i])
                result.append(list1[i])
        return result

    """ Unsure if using merge sort
        def merge(self, data, left, middle, right):
            left = 0

        def mergeSort(self, data, globalList):
            charges=1 # Placeholder
            #...
            self.lock.acquire()
            globalList.extend([charges])
            self.lock.release()
        """
