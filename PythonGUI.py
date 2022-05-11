#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:07:07 2022

@author: nicholascarter
"""

from tkinter import *
from matplotlib import pyplot as plt

# Code to get variables

list = []

def handle_keypress(event):
    list.append(rollEntry.get())
    rollEntry.delete(0, 2)
    
def handle_butonPress():
    fig, ax = plt.subplots(figsize = (10, 7))
    ax.hist(list, bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.show()

    
# Actual GUI stuff

root = Tk()
root.geometry("600x450")
frame = Frame(root)
frame.pack()


label = Label(frame, text = "Insert Roll Below")
label.pack()

rollEntry = Entry(frame, width = 10, justify = 'center')
rollEntry.bind("<Return>", handle_keypress)
rollEntry.pack()

printList = Button(frame, text = "List", command = handle_butonPress)
printList.pack()

root.title("Settlers of Catan Roll Tracker")
root.mainloop()