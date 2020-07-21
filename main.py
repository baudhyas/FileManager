import os
from tkinter import Tk, Frame, ttk, BOTH, StringVar, filedialog
from tkinter.ttk import *
from PIL import Image, ImageTk
from pathlib import Path


GEOMETRY = (1200, 800)


class FileManager(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.parent = master
        self.parent.geometry('x'.join(map(str, GEOMETRY)))
        self.style = Style()
        self._folder_path = StringVar()
        self._selected_folder = StringVar()
        self._folder_path.set(os.path.abspath('.'))
        self.gui()

    def gui(self):
        self.config()
        self.top_bar()
        self.body()

    def top_bar(self):
        # Adding Top bar
        self.top_frame = ttk.Frame(
            self.parent, borderwidth=2, width=1200, height=55, style='W.TFrame')
        self.top_frame.pack(fill=BOTH)
        images = self.load_top_bar_images()
        self.top_bar_buttons = []

        self.open_folder_button = ttk.Button(
            self.top_frame, image=images[0], command=self.select_folder)
        self.open_folder_button.grid(column=0, row=1)
        self.open_folder_button.image = images[0]

    def body(self):
        self.body = ttk.Frame(
            self.parent, borderwidth=2, width=1200, height=700, style='B.TFrame')
        self.body.pack(fill=BOTH)

    def config(self):
        self.style.configure('W.TFrame', foreground='#aecccf',
                             background='#aecccf')
        self.style.configure('B.TFrame', foreground='#ffcccf',
                             background='#ffcccf')

    def load_top_bar_images(self):
        images = []
        for i in os.listdir('icons/'):
            print(i)
            path = ImageTk.PhotoImage(Image.open(
                FileManager.resource_path('icons/'+i)))
            images.append(path)
        return images

    def select_folder(self):
        path = filedialog.askdirectory()
        self._folder_path.set(path)

    @ staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS  # pylint: disable=no-member
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


def main():
    root = Tk()
    root.title('File Manager')
    app = FileManager(root)
    app.mainloop()


if __name__ == '__main__':
    main()
