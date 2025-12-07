# Main: run specific sorting and displays on n threads based on user input
# Tkinter visualization of the graphs using matplotlib (visual.py)
# Threading functions and timing (threadingFuncs.py)
# Sorting functions: selection, merge, and xyz based on user input to compare time took to sort for n threads (sorting.py)

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from sorting import Sorting
from visual import Visual
from threadingFuncs import Thread
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
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

data = pd.read_csv("Train_Data.csv")
data = data.drop_duplicates()

def on_filter_toggle(filter_name, filter_vars, filter_dropdowns):
    if filter_vars[filter_name].get():  # checked
        filter_dropdowns[filter_name].grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    else:
        filter_dropdowns[filter_name].grid_forget()

def on_filter_selected(filter_vars, filter_dropdowns, search_threads_var, search_algo_var, time_label, results_table):
    totalTime = 0

    checked_filters = {}
    for col, var in filter_vars.items():
        if var.get():  # checkbox is checked
            value = filter_dropdowns[col].get()
            if value:
                checked_filters[col] = value

    filtered_df = data
    num_threads = int(search_threads_var.get())
    algorithm = search_algo_var.get()

    for col, val in checked_filters.items():
        if col in ["age", "bmi", "charges"]:
            val = float(val)  # dropdown value as float
            # Filter the DataFrame first to only include rows in the bucket
            filtered_df = filtered_df[(filtered_df[col] >= val) & (filtered_df[col] < val + 1)]

        start = time.perf_counter_ns()
        if algorithm == "Linear":
            filtered_df = thread.multitLinearSearch(filtered_df, num_threads, col, val)
        else:  # Binary search
            filtered_df = thread.multitBinarySearch(filtered_df, num_threads, col, val)
        stop = time.perf_counter_ns()
        totalTime += (stop - start)

    update_table(filtered_df, results_table)
    time_label.config(text=f"Execution Time: {totalTime:,} ns", font=("Arial", 16))

def update_table(df, results_table):
    for row in results_table.get_children():
        results_table.delete(row)
    for i, row in df.iterrows():
        results_table.insert(
            "", "end",
            values=(
                i,
                row["age"],
                row["sex"],
                row["bmi"],
                row["children"],
                row["smoker"],
                row["region"],
                row["charges"]
            )
        )

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
    #print("Has duplicates in charges?: ", data.duplicated(keep=False))
    #print(data.head())
    #print("Min", min(data['charges']))
    #print("Max", max(data['charges']))


    if graphDisplay == 'Pie Chart':
        call = thread.callVisualFunction(data, threadCount, 'Pie Chart')

        displayGraph(interface, pieGraphFigures, displayRow, displayCol, displayCount)
        execTime = tk.Label(interface, text=f"Visualization Execution Time: {call}", bg='lightblue', fg='black', font=('arial', 16))
        execTime.grid(row=1, column=2, padx=10, pady=10)
    elif graphDisplay == 'Line Chart':
        call = thread.callVisualFunction(data, threadCount, 'Line Chart')
        displayGraph(interface, lineGraphFigures, displayRow, displayCol, displayCount)
        execTime = tk.Label(interface, text=f"Visualization Execution Time: {call}", bg='lightblue', fg='black', font=('arial', 16))
        execTime.grid(row=1, column=2, padx=10, pady=10)
    elif graphDisplay == 'Bar Chart':
        call = thread.callVisualFunction(data, threadCount, 'Bar Chart')
        displayGraph(interface, barGraphFigures, displayRow, displayCol, displayCount)
        execTime = tk.Label(interface, text=f"Visualization Execution Time: {call}", bg='lightblue', fg='black', font=('arial', 16))
        execTime.grid(row=1, column=2, padx=10, pady=10)

    if sortMethod == 'Selection Sort':
        call = thread.callSortFunction(data, threadCount, 'Selection Sort')
        execTime = tk.Label(interface, text=f"Sorting Execution Time: {call}", bg='lightblue', fg='black', font=('arial', 16))
        execTime.grid(row=2, column=2, padx=10, pady=10)
    elif sortMethod == 'Insertion Sort':
        call = thread.callSortFunction(data, threadCount, 'Insertion Sort')
        execTime = tk.Label(interface, text=f"Sorting Execution Time: {call}", bg='lightblue', fg='black', font=('arial', 16))
        execTime.grid(row=2, column=2, padx=10, pady=10)
    #elif sortMethod == 'Merge Sort':
        #thread.callSortFunction(data, threadCount, 'Merge Sort')

def main():
    interface = tk.Tk()
    interface.title("Medical Insurance Database")
    interface.configure(bg='lightblue')
    interface.geometry("1600x1400")
    interface.attributes('-topmost', True)

    # Ref: Google & Stack Overflow, how to allow notebook to resize with window size
    interface.columnconfigure(0, weight=1)
    interface.rowconfigure(0, weight=1)

    notebook = ttk.Notebook(interface)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Sorting and visualization frame and searching frame
    sortVisual_frame = tk.Frame(interface, bg="skyblue")
    search_frame = tk.Frame(interface,  bg="skyblue")
    # Configures to use whole windows
    search_frame.columnconfigure(0, weight=1)
    search_frame.rowconfigure(0, weight=1)

    notebook.add(sortVisual_frame, text="Sorting & Visualization")
    notebook.add(search_frame, text="Searching")

####### Sorting & Visualization Frame #######
    options = ['Pie Chart', 'Line Chart', 'Bar Chart']
    start = tk.StringVar(sortVisual_frame)
    graphLabel = tk.Label(sortVisual_frame, text="Choose visualization of data: ", bg='lightblue', fg='black', font=('arial', 16))
    graphLabel.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    graph = tk.OptionMenu(sortVisual_frame, start, *options)
    graph.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    options1 = ['Selection Sort', 'Insertion Sort']
    start1 = tk.StringVar(sortVisual_frame)
    sortingLabel = tk.Label(sortVisual_frame, text="Choose sorting method for medical insurance charges: ", bg='lightblue', fg='black', font=('arial', 16))
    sortingLabel.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    sorting = tk.OptionMenu(sortVisual_frame, start1, *options1)
    sorting.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    options2 = [2, 4, 8, 16]
    start2 = tk.StringVar(sortVisual_frame)
    threadLabel = tk.Label(sortVisual_frame, text="Choose number of threads for the above operations: ", bg='lightblue', fg='black', font=('arial', 16))
    threadLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    thread = tk.OptionMenu(sortVisual_frame, start2, *options2)
    thread.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

    submit = tk.Button(sortVisual_frame, text="Submit", bg='lightblue', fg='black', command=lambda: submitAndProcess(sortVisual_frame, start, start1, start2))
    submit.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

####### Search Frame #######
    filter_vars = {}  # store the variable for each filter (checkbox)
    filter_dropdowns = {}  # store the dropdown (Combobox) widgets
    algo_frame = tk.Frame(search_frame, bg="lightblue")
    algo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    algo_frame.columnconfigure(0, weight=1)
    algo_frame.rowconfigure(0, weight=1)

    results_frame = tk.Frame(search_frame, bg="grey")
    results_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    results_frame.columnconfigure(0, weight=1)
    results_frame.rowconfigure(0, weight=1)

    tk.Label(
        results_frame,
        text="Results",
        bg="grey",
        fg="white",
        font=('Arial', 14, 'bold')
    ).grid(row=0, column=0, padx=10, pady=10)

    # Table (Treeview)
    columns = ("Index", "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges")
    results_table = ttk.Treeview(results_frame, columns=columns, show="headings")
    results_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")
    for col in columns:
        results_table.heading(col, text=col)
        results_table.column(col, anchor="center", width=100)

    tk.Label(algo_frame, text="Search Algorithm:", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    search_algo_var = tk.StringVar(value="Linear")
    search_algo_menu = tk.OptionMenu(algo_frame, search_algo_var, "Linear", "Binary")
    search_algo_menu.grid(row=1, column=0, padx=10, pady=10)

    tk.Label(algo_frame, text="Number of Threads:", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    search_threads_var = tk.StringVar(value="4")
    search_threads_menu = tk.OptionMenu(algo_frame, search_threads_var, 1, 2, 4, 8, 16)
    search_threads_menu.grid(row=3, column=0, padx=10, pady=10)
    filter_options = {
        "age": [str(i) for i in range(1, 100)],
        "sex": ["male", "female"],
        "bmi": [str(i) for i in range(15, 30)],
        "smoker": ["yes", "no"],
        "region": ["northeast", "northwest", "southeast", "southwest"],
        "children": [str(i) for i in range(0, 6)],
        "charges": [str(i) for i in range(10000, 20000)]
    }

    row = 4
    for filter_name in ["age", "sex", "bmi", "smoker", "region", "children", "charges"]:
        # Frame to hold checkbox + dropdown
        row_frame = tk.Frame(algo_frame, bg="lightblue")
        row_frame.grid(row=row, column=0, padx=10, pady=10)
        row += 1

        var = tk.BooleanVar()
        filter_vars[filter_name] = var

        # Checkbox
        cb = tk.Checkbutton(
            row_frame,
            text=filter_name,
            variable=var,
            bg="lightblue",
            command=lambda f=filter_name: on_filter_toggle(f, filter_vars, filter_dropdowns)
        )
        cb.grid(row=row, column=0, padx=10, pady=10)
        row += 1

        # Dropdown (hidden initially)
        options = filter_options.get(filter_name, [])
        dropdown = ttk.Combobox(row_frame, values=options, state="readonly", width=10)
        filter_dropdowns[filter_name] = dropdown
        dropdown.grid(row=1, column=0, padx=10, pady=10)
        dropdown.grid_forget()  # hide initially

    submit2 = tk.Button(
        algo_frame,
        text="Filter",
        bg='skyblue',
        fg='black',
        command=lambda: on_filter_selected(filter_vars, filter_dropdowns, search_threads_var, search_algo_var, time_label, results_table)
    )
    submit2.grid(row=row, column=0, padx=10, pady=10)

    # Time output label
    time_label = tk.Label(
        results_frame,
        text="Execution Time: ",
        bg="grey",
        fg="black",
        font=("Arial", 10, "bold")
    )
    time_label.grid(row=2, column=0, padx=10, pady=10)

    interface.mainloop()

if __name__ == '__main__':
    main()