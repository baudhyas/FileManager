import os
from tkinter import *
from tkinter.ttk import *
from pathlib import Path


class FileManager(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.parent = master
        self.parent.geometry('900x600')


def main():
    root = Tk()
    root.title('File Manager')
    app = FileManager(root)
    app.mainloop()


if __name__ == '__main__':
    main()
