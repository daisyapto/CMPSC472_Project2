# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

class Sorting:

    def selectionSort(self, data):
        charges = list(data['charges'])
        for i in range (len(charges)):
            for j in range (i+1, len(charges)):
                if charges[j] < charges[i]:
                    charges[j], charges[i] = charges[i], charges[j]
        return charges

    def insertionSort(self, data):
        charges = data['charges']
        for i in range (len(charges)):
            for j in range (len(charges)-1, 0):
                if charges[j] > charges[i]:
                    charges[j] = None # Still working on this

    def merge(self, left, right):
        x=1 # Placeholder

    def mergeSort(self, data):
        x=1 # Placeholder