import backend

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

gui = Tk()
gui.geometry("765x610")
gui.title("CS 350 Project")


def choose_file():
    selected = filedialog.askdirectory()
    folderPath.set(selected)


def find_path():
    folder_path = folderPath.get()
    number_files, number_dirs = backend.find_number(folder_path)
    file_list = backend.find_name(folder_path)
    type_list = backend.find_type(folder_path)
    a, size_list = backend.find_size(folder_path)
    file_list_type.delete(0, 'end')
    file_list_name.delete(0, 'end')
    file_list_size.delete(0, 'end')
    a = str(a / 1000)
    total_size['text'] = 'Total size: ' + a + 'KB'
    total_files['text'] = 'Total number of files: ' + str(number_files)
    for i in range(number_files):
        file_list_name.insert(i, file_list[i])
        file_list_type.insert(i, type_list[i])
        file_list_size.insert(i, str(size_list[i] / 1000) + ' KB')


folderPath = StringVar()

selection = Label(gui, text="Select your file", font="13", bg='hot pink')
selection.grid(row=0, column=0, ipadx=40)

enter_file = Entry(gui, textvariable=folderPath, state='disabled', width=30, font=11)
enter_file.grid(row=0, column=1)

browse_folder = ttk.Button(gui, text="Browse Folder", command=choose_file)
browse_folder.grid(row=0, column=2)

analyze_button = ttk.Button(gui, text="Analyze", command=find_path)
analyze_button.grid(row=2, column=1)

total_size = Label(gui, text='Total size: ')
total_size.grid(row=3, column=2)
total_files = Label(gui, text='Total number of files: ')
total_files.grid(row=2, column=2)

file_name = Label(gui, text='File Name', bg='lime green')
file_name.grid(row=4, column=0, ipadx=91)

file_type = Label(gui, text='File Type', bg='coral')
file_type.grid(row=4, column=1, ipadx=94)

file_type = Label(gui, text='File Size', bg='SlateBlue1')
file_type.grid(row=4, column=2, ipadx=97)

file_list_name = Listbox(gui, height=30, width=40)
file_list_name.grid(row=5, column=0)

file_list_type = Listbox(gui, height=30, width=40)
file_list_type.grid(row=5, column=1)

file_list_size = Listbox(gui, height=30, width=40)
file_list_size.grid(row=5, column=2)

author_name = Label(gui, text="Fatih Memis & Tolga Gümüşçü", font='13', bg='Indianred1')
author_name.grid(row=6, column=1)

gui.mainloop()
