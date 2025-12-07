# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import threading

class Sorting:

    def __init__(self):
        self.lock = threading.Lock()

    def selectionSort(self, data, globalList):
        charges = list(data['charges'])
        for i in range (len(charges)):
            for j in range (i+1, len(charges)):
                if charges[j] < charges[i]:
                    charges[j], charges[i] = charges[i], charges[j]

        self.lock.acquire()
        globalList.extend([charges])
        self.lock.release()

    # Reference: https://www.w3schools.com/dsa/dsa_algo_insertionsort.php
    # Haven't tried optimized solution at link but this was the basic implementation I used to modify the bug
    def insertionSort(self, data, globalList):
        charges = list(data['charges']) # Convert dataframe column into standard list
        for i in range(1, len(charges)):
            insertValue = i # Insert at i (not moving) when element is already larger than everything before it
            currentCharge = charges.pop(i) # Extract current element
            for j in range (i-1, -1, -1): # Iterate backwards from 1 position behind current position in list
                if charges[j] > currentCharge: # Compare through all elements behind it
                    insertValue = j # Update insertion value every time the element is smaller than an element behind it
            charges.insert(insertValue, currentCharge) # Insert with most updated insertValue at the end of loop

        self.lock.acquire()
        globalList.extend([charges])
        self.lock.release()

    """ No longer needed, using heapq merge instead 
    def listMerging(self, list1, list2):
        # Had an idea
        # Was having an issue where selection sort was return two sorted halves when 2 threads were used for example [1, 2, 4, 3, 5, 6], so it reminded of the merge mergesort function
        # Used it in selection sort to produce the proper results
        # Note -- does not fully work yet
        result = []
        print(len(list1))
        print(len(list2))
        for i in range(min(len(list1), len(list2))):
            if list1[i] <= list2[i]:
                result.append(list1[i])
                result.append(list2[i])
            elif list1[i] > list2[i]:
                result.append(list2[i])
                result.append(list1[i])
        return result
    """

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