import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv
import datetime

# create the main window
root = tk.Tk()
root.title('Imaginetics')
root.geometry('1000x300')


def add_part():
    # grab the current date/time
    current = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    later = (datetime.datetime.now(
    ) + datetime.timedelta(hours=test_duration.get())).strftime('%m/%d/%Y %H:%M:%S')

    data = [part_number.get(), run_number.get(), bin.get(), current, later]

    with open('wet_test.csv', 'a+', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    part_entry.delete(0, 'end')
    run_entry.delete(0, 'end')
    bin.set('A1')
    part_entry.focus()

    write_table()


def create_scan_window():
    global part_number
    global part_entry
    global run_number
    global run_entry
    global bin
    global test_duration

    scan_window = tk.Toplevel(root, background='white')
    scan_window.geometry('270x200+50+50')

    part_number = tk.StringVar()
    run_number = tk.IntVar()
    bin = tk.StringVar()
    test_duration = tk.IntVar()

    bins = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
    bin.set('A1')
    test_time_options = [24, 12, 8, 6, 2]
    test_duration.set(24)

    header = ttk.Label(
        scan_window,
        text='Wet Test',
        background='white',
        foreground='black',
        font=('Roboto', 20)
    )
    header.grid(row=0, rowspan=2, column=1, columnspan=6)

    # pack in all the entry boxes

    # part info
    part_label = ttk.Label(scan_window, padding=4, width=10,
                           text='Part Number: ', background='white')
    part_label.grid(row=2, column=1, columnspan=2)
    part_entry = ttk.Entry(
        scan_window, textvariable=part_number)
    part_entry.grid(row=2, column=3, columnspan=4, pady=4)
    part_entry.focus()

    # run info
    run_label = ttk.Label(scan_window, padding=4, width=10,
                          text='Run: ', background='white')
    run_label.grid(row=3, column=1, columnspan=2)
    run_entry = ttk.Entry(scan_window, textvariable=run_number)
    run_entry.grid(row=3, column=3, columnspan=4, pady=4)

    # location info
    bin_label = ttk.Label(scan_window, padding=4,
                          width=10, text='Bin Location: ', background='white')
    bin_label.grid(row=4, column=1, columnspan=2)
    bin_menu = ttk.OptionMenu(scan_window, bin, *bins)
    bin_menu_style = ttk.Style()
    # bin_menu_style.configure('TMenubutton', background='lightgrey')
    bin_menu.grid(row=4, column=3, pady=4)

    # test duration info
    test_duration_label = ttk.Label(
        scan_window, padding=4, width=10, text='Test Duration: ', background='white')
    test_duration_label.grid(row=5, column=1, columnspan=2)
    test_menu = ttk.OptionMenu(scan_window, test_duration, *test_time_options)
    bin_menu_style.configure('TMenubutton', background='lightgrey')
    test_menu.grid(row=5, column=3, pady=4)

    # add the button
    submit_btn = ttk.Button(scan_window, text='Submit', command=add_part)
    submit_btn.grid(row=6, column=2, columnspan=4, pady=4)


# init top div of main window
top_frame = ttk.Frame(root, width=300).grid(row=1, column=0)


def write_table():
    tree = ttk.Treeview(top_frame)
    tree.delete(*tree.get_children())
    root.update_idletasks()

    df = pd.read_csv('wet_test.csv')

    cols = list(df.columns)

    tree['columns'] = cols
    for i in cols:
        tree.column(i, anchor='center', stretch='yes')
        tree.heading(i, text=i, anchor='center')

    for index, row in df.iterrows():
        tree.insert('', 0, values=list(row))

    tree.column('#0', width=0, stretch='no')

    table_style = ttk.Style()
    table_style.theme_use('default')
    table_style.map('Treeview')
    tree.grid(row=2, column=0, columnspan=5)


# init bottom div of main window
bottom_frame = ttk.Frame(root).grid(row=2, column=0)
button = ttk.Button(root, text='Add Part', command=create_scan_window)
button.grid(row=3, column=1)

write_table()


root.mainloop()
