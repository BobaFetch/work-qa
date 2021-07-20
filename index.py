import tkinter as tk
from tkinter import ttk
import csv
import datetime

root = tk.Tk()
# set window title
root.title('Imaginetics')
# set window size/loc
root.geometry('300x200+50+50')
message = tk.Label(
    root,
    text='Wet Test',
    bg='slategrey',
    fg='white')
message.pack(ipadx=10, ipady=10, fill='both', expand=True)
# part number input
part_number = tk.StringVar()
run_number = tk.IntVar()


def add_part():
    date = datetime.datetime.today().strftime('%m/%d/%Y')
    data = [part_number.get(), run_number.get(), date]
    with open('data.csv', 'a+', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# TODO write function to store data in file


part_info = ttk.Frame(root)
part_info.pack(padx=10, pady=10, fill='x', expand=True)

# part number
part_label = ttk.Label(part_info, text='Part Number:')
part_label.pack(fill='x', expand=True)

part_entry = ttk.Entry(part_info, textvariable=part_number)
part_entry.pack(fill='x', expand=True)
part_entry.focus()

# run number
run_label = ttk.Label(part_info, text='Run:')
run_label.pack(fill='x', expand=True)

run_entry = ttk.Entry(part_info, textvariable=run_number)
run_entry.pack(fill='x', expand=True)


# input button
submit_button = ttk.Button(part_info, text='Add Part', command=add_part)
submit_button.pack(fill='x', expand=True)


# styling
s = ttk.Style()
s.configure('new.TFrame', background='slategrey')

root.mainloop()
