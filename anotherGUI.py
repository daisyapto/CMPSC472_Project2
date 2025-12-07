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
    '''tk.Label(
        tools_frame,
        text="Choose an option",
        bg="skyblue",
    ).pack(padx=5, pady=5)'''
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

    def on_tool_selected():
        selected = tools_var.get()
        sorted_df =  thread.multitLinearSearch(data, 4,  selected,"male")
        update_table(sorted_df)

    for tool in ["age", "sex", "bmi", "smoker", "region", "children","charges"]: # has to lower case so string matches when traversing thorouhg csv
        tk.Radiobutton(
            tools_tab,
            text=tool,
            variable=tools_var,
            value=tool,
            bg="lightblue",
            command = on_tool_selected
        ).pack(anchor="w", padx=20, pady=5)

    filters_tab = tk.Frame(notebook, bg="lightblue")
    filters_var = tk.StringVar(value="None")
    def on_filter_selected():
        selected = tools_var.get()
        sorted_df =  thread.multitLinearSearch(data, 4,  "sex","male")
        update_table(sorted_df)
    for filter in ["Age", "Sex", "BMI", "Smoker", "region", "children","charges"]:
        tk.Radiobutton(
            filters_tab,
            text=filter,
            variable=filters_var,
            value=filter,
            bg="lightblue",
            command=on_filter_selected
        ).pack(anchor="w", padx=20, pady=5)

    filter_vars = {}  # store the variable for each filter (checkbox)
    filter_dropdowns = {}  # store the dropdown (Combobox) widgets

    def on_filter_toggle(filter_name):
        """Show/hide dropdown when checkbox is toggled."""
        if filter_vars[filter_name].get():  # checked
            filter_dropdowns[filter_name].pack(anchor="w", padx=40, pady=2)
        else:
            filter_dropdowns[filter_name].pack_forget()  # hide dropdown

    filters_tab = tk.Frame(notebook, bg="lightblue")
    filters_tab.pack(fill="both", expand=True)
    filter_options = {
    "Age": [str(i) for i in range(1, 100)],
    "Sex": ["male", "female"],
    "BMI": [str(i) for i in range(10, 50)],
    "Smoker": ["yes", "no"],
    "Region": ["northeast", "northwest", "southeast", "southwest"],
    "Children": [str(i) for i in range(0, 6)],
    "Charges": [str(i) for i in range(10000, 20000)]
    }

    def on_filter_selected():
        selected = tools_var.get()
        sorted_df = thread.multitLinearSearch(data, 4, "sex", "male")
        update_table(sorted_df)

    for filter_name in ["Age", "Sex", "BMI", "Smoker", "region", "children", "charges"]:
        var = tk.BooleanVar()
        filter_vars[filter_name] = var
        cb = tk.Checkbutton(
            filters_tab,
            text=filter_name,
            variable=var,
            bg="lightblue",
            command=lambda f=filter_name: on_filter_toggle(f)
        ).pack(anchor="w", padx=20, pady=5)

        options = filter_options.get(filter_name, [])
        dropdown = ttk.Combobox(filters_tab, values=options, state="readonly")
        filter_dropdowns[filter_name] = dropdown
        #filterB = submit = tk.Button(interface, text="Submit", bg='lightblue', fg='black', comman start1, start2, start3, start4))
        #filterB.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

    notebook.add(tools_tab, text="Sort")
    notebook.add(filters_tab, text="Search")


    interface.mainloop()

if __name__ == '__main__':
    main()
