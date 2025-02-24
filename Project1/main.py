import tkinter as tk
import ttkbootstrap as ttk

#converting miles to Km function
def convert():
    miles = entry_int.get()
    km_value = round((miles * 1.61),2)
    output_string.set(f"{str(km_value)}Km")


#window

window = ttk.Window(themename='darkly')
window.title('Convert Miles to Kilometers')
window.minsize(400, 150)  # Minimum width = 400, height = 300
# window.maxsize(1200, 800)  Maximum width = 1200, height = 800


title_label = ttk.Label(master = window, text="Miles to Kilometers", font='Tahoma 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master= input_frame, text='Convert',command=convert)
entry.bind('<Return>', lambda event: convert())
entry.pack(side='left')
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,text='Output',font='Tahoma 24',textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()