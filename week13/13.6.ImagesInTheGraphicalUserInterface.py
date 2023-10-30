"""
COMP.CS.100 Programming 1.
13.1.Basics.py
Creator: Thinh Kieu
Student id number: 152167613

This program is to note down more advanced implementations of a graphic user interface (GUI).
About Images - PhotoImage(), image=.
"""

from tkinter import *


class BombAnimation:
    def __init__(self):
        self.__update_counter = 0

        self.__main_window = Tk()

        self.__bomb_images = []
        for image_file in ["cherrybomb-1.gif", "cherrybomb-2.gif"]:
            self.__bomb_images.append(PhotoImage(file=image_file))

        self.__bomb_button = Button(self.__main_window, command=self.quit)
        self.__bomb_button.pack()

        self.update_image()

        self.__main_window.mainloop()

    def quit(self):
        self.__main_window.destroy()

    def update_image(self):
        self.__bomb_button.configure(image=self.__bomb_images[self.__update_counter % 2])
        self.__update_counter += 1
        self.__main_window.after(200, self.update_image)


def main():
    gui = BombAnimation()


if __name__ == "__main__":
    main()
