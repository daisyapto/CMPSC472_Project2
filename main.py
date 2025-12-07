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

def submitAndProcess(start, start1, start2, start3, start4):
    graphDisplay = start.get()
    sortMethod = start1.get()
    threadCount = int(start2.get())
    searchColumn = start3.get()
    searchValue = start4.get()
    print(graphDisplay)
    print(sortMethod)
    print(threadCount)
    print(searchColumn)
    print(searchValue)

    data = pd.read_csv("Train_Data.csv")
    #print(data.head())
    #print("Min", min(data['charges']))
    #print("Max", max(data['charges']))

    """
    if graphDisplay == 'Pie Chart':
        thread.callFunction(data, threadCount, visual.drawAllPieGraphs)
    elif graphDisplay == 'Line Chart':
        thread.callFunction(data, threadCount, visual.drawAllLineGraphs)
    elif graphDisplay == 'Bar Chart':
        thread.callFunction(data, threadCount, visual.drawAllBarGraphs)"""
    
    if sortMethod == 'Selection Sort':
        thread.callSortFunction(data, threadCount,searchColumn, 'Selection Sort')
    elif sortMethod == 'Insertion Sort':
        thread.callSortFunction(data, threadCount, searchColumn, 'Insertion Sort')
    elif sortMethod == 'Merge Sort':
        thread.callSortFunction(data, threadCount,searchColumn, 'Merge Sort')
        """
    start_time = time.perf_counter()
    thread.multitLinearSearch(data, 2, searchColumn, searchValue)
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    start_time = time.perf_counter()
    thread.multitLinearSearch(data, 16, searchColumn, searchValue)
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
   start_time = time.perf_counter()
    thread.lineSearch(data, "sex","female")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.6f} seconds")"""
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

    options1 = ['Selection Sort', 'Insertion Sort', 'Merge Sort']
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

    options3 = ["age", "sex", "bmi", "smoker", "region", "children", "charges"]
    start3 = tk.StringVar(interface)
    start3.set(options3[0])
    searchLabel = tk.Label(interface, text="Choose search by: ", bg='lightblue', fg='black', font=('arial', 16))
    searchLabel.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    search_dropdown = tk.OptionMenu(interface, start3, *options3)
    search_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

    start4 = tk.StringVar(interface)
    start4.set("Select...")
    suboption_label = tk.Label(interface, text="Choose value: ", bg='lightblue', fg='black', font=('arial', 16))
    suboption_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    sub_option_menu = tk.OptionMenu(interface, start4, "")
    sub_option_menu.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

    # Function to update sub-options dynamically
    def update_suboptions(*args):
        menu = sub_option_menu["menu"]
        menu.delete(0, "end")
        choice = start3.get()
        if choice == "age":
            sub_opts = ["30", "50", "90"]
        elif choice == "sex":
            sub_opts = ["male", "female"]
        elif choice == "smoker":
            sub_opts = ["yes", "no"]
        else:
            sub_opts = ["All"]
        for opt in sub_opts:
            menu.add_command(label=opt, command=lambda value=opt: start4.set(value))
        start4.set(sub_opts[0])

    start3.trace("w", update_suboptions)
    submit = tk.Button(interface, text="Submit", bg='lightblue', fg='black', command=lambda: submitAndProcess(start, start1, start2, start3, start4))
    submit.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

    interface.mainloop()




if __name__ == '__main__':
    main()
