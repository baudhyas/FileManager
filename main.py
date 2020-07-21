import os
from tkinter import Tk, Frame, ttk, BOTH, StringVar, filedialog, Toplevel
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

        # First Button
        self.open_folder_button = ttk.Button(
            self.top_frame, image=images[0], command=self.select_folder)
        self.open_folder_button.grid(column=1, row=1)
        self.open_folder_button.image = images[0]

        # Second Button
        self.rename_current_folder = ttk.Button(
            self.top_frame, image=images[1], command=self.rename_current_dir)
        self.rename_current_folder.grid(column=2, row=1)
        self.rename_current_folder.image = images[1]

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

# In completeMethod
    def rename_current_dir(self):
        # In completeMethod
        def submit():
            data = entry1.get()
            print(data)

        print('Hello')
        newWindow = Toplevel(self.parent)
        newWindow.title("New Window")
        newWindow.geometry("200x100")
        input_text = StringVar()
        Label(newWindow, text='Enter New Name').grid(
            column=1, row=1, sticky='nesw', padx=43)
        entry1 = Entry(newWindow, textvariable=input_text)
        entry1.focus_force()
        entry1.grid(column=1, row=2, sticky='nesw', padx=20, pady=13)
        Button(newWindow, text='Submt', command=submit).grid(
            column=1, row=3, sticky='nesw', padx=43)

    @staticmethod
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
