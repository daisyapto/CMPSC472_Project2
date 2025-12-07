# Main: run specific sorting and displays on n threads based on user input
# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import time
import matplotlib
import tkinter as tk
from tkinter import ttk
import pandas as pd
import threading
from sorting import Sorting
from visual import Visual
from threadingFuncs import Thread

sort = Sorting()
visual = Visual()
thread = Thread()

def submitAndProcess(start, start1, start2):
    graphDisplay = start.get()
    sortMethod = start1.get()
    threadCount = int(start2.get())
    #print(graphDisplay)
    #print(sortMethod)
    #print(threadCount)

    data = pd.read_csv("Train_Data.csv")
    data = data.drop_duplicates()
    print("Has duplicates in charges?: ", data.duplicated(keep=False))
    #print(data.head())
    #print("Min", min(data['charges']))
    #print("Max", max(data['charges']))


    if graphDisplay == 'Pie Chart':
        thread.callVisualFunction(data, threadCount, 'Pie Chart')
    elif graphDisplay == 'Line Chart':
        thread.callVisualFunction(data, threadCount, 'Line Chart')
    elif graphDisplay == 'Bar Chart':
        thread.callVisualFunction(data, threadCount, 'Bar Chart')

    if sortMethod == 'Selection Sort':
        thread.callSortFunction(data, threadCount, 'Selection Sort')
    elif sortMethod == 'Insertion Sort':
        thread.callSortFunction(data, threadCount, 'Insertion Sort')
    #elif sortMethod == 'Merge Sort':
        #thread.callSortFunction(data, threadCount, 'Merge Sort')

def main():
    interface = tk.Tk()
    interface.geometry("800x600")
    interface.title("Medical Insurance Database")
    interface.configure(bg='lightblue')
    interface.attributes('-topmost', True)

    options = ['Pie Chart', 'Line Chart', 'Bar Chart']
    start = tk.StringVar(interface)
    graphLabel = tk.Label(interface, text="Choose visualization of data: ", bg='lightblue', fg='black', font=('arial', 16))
    graphLabel.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    graph = tk.OptionMenu(interface, start, *options)
    graph.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    options1 = ['Selection Sort', 'Insertion Sort']
    start1 = tk.StringVar(interface)
    sortingLabel = tk.Label(interface, text="Choose sorting method for medical insurance charges: ", bg='lightblue', fg='black', font=('arial', 16))
    sortingLabel.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    sorting = tk.OptionMenu(interface, start1, *options1)
    sorting.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    options2 = [2, 4, 8, 16]
    start2 = tk.StringVar(interface)
    threadLabel = tk.Label(interface, text="Choose number of threads for the above operations: ", bg='lightblue',fg='black', font=('arial', 16))
    threadLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    thread = tk.OptionMenu(interface, start2, *options2)
    thread.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

    submit = tk.Button(interface, text="Submit", bg='lightblue', fg='black', command=lambda: submitAndProcess(start, start1, start2))
    submit.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    interface.mainloop()

if __name__ == '__main__':
    main()