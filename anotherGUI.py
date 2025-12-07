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



def main():
    data = pd.read_csv("Train_Data.csv")
    interface = tk.Tk()
    interface.title("Medical Insurance Database")

    # Tools frame
    tools_frame = tk.Frame(interface, width=200, height=400, bg="skyblue")
    tools_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)

    # Tools and Filters tabs
    notebook = ttk.Notebook(tools_frame)
    notebook.pack(expand=True, fill="both")

    tools_tab = tk.Frame(notebook, bg="lightblue")
    tools_var = tk.StringVar(value="None")
    results_frame = tk.Frame(interface, width=600, height=400, bg="grey")
    results_frame.pack(padx=5, pady=5, side=tk.RIGHT, fill="both", expand=True)

    tk.Label(
        results_frame,
        text="Results",
        bg="grey",
        fg="white",
        font=('Arial', 14, 'bold')
    ).pack(padx=5, pady=5)

    # Table (Treeview)
    columns = ("Index", "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges")
    results_table = ttk.Treeview(results_frame, columns=columns, show="headings")
    results_table.pack(fill="both", expand=True, padx=10, pady=10)
    for col in columns:
        results_table.heading(col, text=col)
        results_table.column(col, width=100, anchor="center")

    def update_table(df):
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

    # Time output label
    time_label = tk.Label(
        results_frame,
        text="Execution Time: ",
        bg="grey",
        fg="black",
        font=("Arial", 10, "bold")
    )
    time_label.pack(pady=5)

    center_frame = tk.Frame(tools_tab, bg='lightblue')
    center_frame.pack(expand=True)
    def on_sort_selected():
        sort_method = start1.get()
        thread_count = int(start2.get())
        start = time.perf_counter_ns()
        sorted_df = thread.callSortFunction(data, thread_count, sort_method)
        stop = time.perf_counter_ns()
        update_table(sorted_df)
        time_ns = stop - start
        time_label.config(text=f"Execution Time (Sort): {time_ns:,} ns")

    options1 = ['Selection Sort', 'Insertion Sort', 'Merge Sort']
    options2 = [2,4,8,16]
    start1 = tk.StringVar(value="Selection Sort") # the default will be selection
    start2 = tk.StringVar(value="2")
    sort_frame = tk.Frame(center_frame, bg='lightblue')
    sort_frame.pack(pady=5, fill='x')
    sortingLabel = tk.Label(
        sort_frame,
        text="Choose sorting method:",
        bg='lightblue',
        fg='black',
        font=('Arial', 12)
    )
    sortingLabel.pack(side='left', pady=5)
    sorting = tk.OptionMenu(sort_frame, start1, *options1)
    sorting.pack(side='left', padx=5 )
    thread_frame = tk.Frame(center_frame, bg='lightblue')
    thread_frame.pack(pady=5, fill='x')
    sortingLabel2 = tk.Label(
        thread_frame,
        text="Choose amount of threads:",
        bg='lightblue',
        fg='black',
        font=('Arial', 12)
    )
    sortingLabel2.pack(side='left', pady=5)
    sorting2 = tk.OptionMenu(thread_frame, start2, *options2)
    sorting2.pack(side='left', padx=5)

    submit = tk.Button(
        tools_tab,
        text="Apply Sort",
        bg='skyblue',
        fg='black',
        command=lambda:on_sort_selected()
    )
    submit.pack(padx=10, pady=10, anchor="center")








    filter_vars = {}  # store the variable for each filter (checkbox)
    filter_dropdowns = {}  # store the dropdown (Combobox) widgets

    def on_filter_toggle(filter_name):
        if filter_vars[filter_name].get():  # checked
            filter_dropdowns[filter_name].pack(side="left", padx=10)
        else:
            filter_dropdowns[filter_name].pack_forget()

    filters_tab = tk.Frame(notebook, bg="lightblue")
    filters_tab.pack(fill="both", expand=True)
    algo_frame = tk.Frame(filters_tab, bg="lightblue")
    algo_frame.pack(anchor="w", padx=20, pady=5, fill="x")

    tk.Label(algo_frame, text="Search Algorithm:", bg="lightblue", font=("Arial", 12)).pack(side="left")
    search_algo_var = tk.StringVar(value="Linear")
    search_algo_menu = tk.OptionMenu(algo_frame, search_algo_var, "Linear", "Binary")
    search_algo_menu.pack(side="left", padx=10)

    tk.Label(algo_frame, text="Number of Threads:", bg="lightblue", font=("Arial", 12)).pack(side="left", padx=(20, 0))
    search_threads_var = tk.StringVar(value="4")
    search_threads_menu = tk.OptionMenu(algo_frame, search_threads_var, 1, 2, 4, 8, 16)
    search_threads_menu.pack(side="left", padx=10)
    filter_options = {
    "age": [str(i) for i in range(1, 100)],
    "sex": ["male", "female"],
    "bmi": [str(i) for i in range(15, 30)],
    "smoker": ["yes", "no"],
    "region": ["northeast", "northwest", "southeast", "southwest"],
    "children": [str(i) for i in range(0, 6)],
    "charges": [str(i) for i in range(10000, 20000)]
    }

    def on_filter_selected():
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

        update_table(filtered_df)
        time_label.config(text=f"Execution Time: {totalTime:,} ns")

    for filter_name in ["age", "sex", "bmi", "smoker", "region", "children", "charges"]:
        # Frame to hold checkbox + dropdown
        row_frame = tk.Frame(filters_tab, bg="lightblue")
        row_frame.pack(anchor="w", padx=20, pady=5, fill="x")

        var = tk.BooleanVar()
        filter_vars[filter_name] = var

        # Checkbox
        cb = tk.Checkbutton(
            row_frame,
            text=filter_name,
            variable=var,
            bg="lightblue",
            command=lambda f=filter_name: on_filter_toggle(f)
        )
        cb.pack(side="left")

        # Dropdown (hidden initially)
        options = filter_options.get(filter_name, [])
        dropdown = ttk.Combobox(row_frame, values=options, state="readonly", width=10)
        filter_dropdowns[filter_name] = dropdown
        dropdown.pack(side="left", padx=10)
        dropdown.pack_forget()  # hide initially

    submit2 = tk.Button(
        filters_tab,
        text="Filter",
        bg='skyblue',
        fg='black',
        command=lambda: on_filter_selected()
    )
    submit2.pack(padx=10, pady=10, anchor="center")







    notebook.add(tools_tab, text="Sort")
    notebook.add(filters_tab, text="Search")



    interface.mainloop()



if __name__ == '__main__':
    main()
