# Main: run specific sorting and displays on n threads based on user input
# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import tkinter as tk
import pandas as pd
from sorting import Sorting
from visual import Visual
from threadingFuncs import Thread
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threadingFuncs import (figAge_B, figMF_B, figBMI_B, figSmoker_B, figRegion_B, figNumOfChildren_B, figMed_B,
    figAge_L, figBMI_L, figNumOfChildren_L,
    figAge_P, figMF_P, figBMI_P, figSmoker_P, figRegion_P, figNumOfChildren_P, figMed_P)

barGraphFigures = [figAge_B, figMF_B, figBMI_B, figSmoker_B, figRegion_B, figNumOfChildren_B, figMed_B]
lineGraphFigures = [figAge_L, figBMI_L, figNumOfChildren_L]
pieGraphFigures = [figAge_P, figMF_P, figBMI_P, figSmoker_P, figRegion_P, figNumOfChildren_P, figMed_P]
displayRow = 4
displayCol = 0
displayCount = 0

sort = Sorting()
visual = Visual()
thread = Thread()

def displayGraph(interface, figureList, r, c, co): # r = row, c = col, co = counter; simple variable names because when using the global variables, had glitches with multiple function calls
    for item in figureList:
        canvas = FigureCanvasTkAgg(item, master=interface)
        canvasWidget = canvas.get_tk_widget()
        if co == 4:
            r += 1
        if co == 4:
            c = 0
        canvasWidget.grid(row=r, column=c, padx=10, pady=10, sticky=tk.W)
        c += 1
        co += 1

def submitAndProcess(interface, start, start1, start2):
    graphDisplay = start.get()
    sortMethod = start1.get()
    threadCount = int(start2.get())
    #print(graphDisplay)
    #print(sortMethod)
    #print(threadCount)

    data = pd.read_csv("Train_Data.csv")
    data = data.drop_duplicates()
    #print("Has duplicates in charges?: ", data.duplicated(keep=False))
    #print(data.head())
    #print("Min", min(data['charges']))
    #print("Max", max(data['charges']))


    if graphDisplay == 'Pie Chart':
        thread.callVisualFunction(data, threadCount, 'Pie Chart')
        displayGraph(interface, pieGraphFigures, displayRow, displayCol, displayCount)
    elif graphDisplay == 'Line Chart':
        thread.callVisualFunction(data, threadCount, 'Line Chart')
        displayGraph(interface, lineGraphFigures, displayRow, displayCol, displayCount)
    elif graphDisplay == 'Bar Chart':
        thread.callVisualFunction(data, threadCount, 'Bar Chart')
        displayGraph(interface, barGraphFigures, displayRow, displayCol, displayCount)

    if sortMethod == 'Selection Sort':
        thread.callSortFunction(data, threadCount, 'Selection Sort')
    elif sortMethod == 'Insertion Sort':
        thread.callSortFunction(data, threadCount, 'Insertion Sort')
    #elif sortMethod == 'Merge Sort':
        #thread.callSortFunction(data, threadCount, 'Merge Sort')

def main():
    interface = tk.Tk()
    interface.title("Medical Insurance Database")
    interface.configure(bg='lightblue')
    interface.geometry("1600x1200")
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
    threadLabel = tk.Label(interface, text="Choose number of threads for the above operations: ", bg='lightblue', fg='black', font=('arial', 16))
    threadLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    thread = tk.OptionMenu(interface, start2, *options2)
    thread.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

    submit = tk.Button(interface, text="Submit", bg='lightblue', fg='black', command=lambda: submitAndProcess(interface, start, start1, start2))
    submit.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    interface.mainloop()

if __name__ == '__main__':
    main()
