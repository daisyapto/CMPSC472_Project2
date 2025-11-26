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

def main():
    interface = tk.Tk()
    interface.geometry("800x600")
    interface.title("Medical Insurance Database")
    interface.configure(bg='lightblue')
    interface.attributes('-topmost', True)

    options = ['Pie', 'Line', 'Bar']
    start = tk.StringVar(interface)
    graphLabel = tk.Label(interface, text="Enter the type of graph: ", bg='lightblue', fg='black', font=('arial', 16))
    graphLabel.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    graph = tk.OptionMenu(interface, start, *options)
    graph.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    options1 = ['Selection', 'Merge']
    start1 = tk.StringVar(interface)
    graphLabel1 = tk.Label(interface, text="Enter the sorting method: ", bg='lightblue', fg='black', font=('arial', 16))
    graphLabel1.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    graph1 = tk.OptionMenu(interface, start1, *options1)
    graph1.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    threadLabel = tk.Label(interface, text="Enter the number of threads: ", bg='lightblue', fg='black', font=('arial', 16))
    threadLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    thread = tk.Entry(interface, width=2)
    thread.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)







    interface.mainloop()


if __name__ == '__main__':
    main()