"""
COMP.CS.100 Programming 1.
13.1.Basics.py
Creator: Thinh Kieu
Student id number: 152167613

This program is to note down more advanced implementations of a graphic user interface (GUI).
About Images - PhotoImage(), image=.
"""

from tkinter import *

class BOMB_GUI:
  def __init__(self):
    self.__main_window = Tk()

    self.__bang_image = PhotoImage(file="bang.gif")
    self.__bomb_image = PhotoImage(file="bomb.gif")
    self.__boom_image = PhotoImage(file="boom.gif")

    self.__bomb_label = Label(self.__main_window, image=self.__bomb_image)
    self.__explode_button = Button(self.__main_window, image=self.__bang_image,
                                   command=self.explode)
    self.__reload_button = Button(self.__main_window, text="Reload",
                                  command=self.reaload, state=DISABLED,
                                  background="white")
    self.__quit_button = Button(self.__main_window, text="Quit",
                                command=self.quit, background="white")

    self.__bomb_label.pack(fill=BOTH)
    self.__explode_button.pack()
    self.__reload_button.pack(fill=BOTH)
    self.__quit_button.pack(fill=BOTH)

    self.__main_window.mainloop()

  def explode(self):
    self.__bomb_label.configure(image=self.__boom_image)
    self.__explode_button.configure(state=DISABLED)
    self.__reload_button.configure(state=NORMAL)

  def reaload(self):
    self.__bomb_label.configure(image=self.__bomb_image)
    self.__explode_button.configure(state=NORMAL)
    self.__reload_button.configure(state=DISABLED)

  def quit(self):
    self.__main_window.destroy()

def main():
  gui = BOMB_GUI()

if __name__ == "__main__":
   main()