#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:17:35 2018

@author: dasha
"""
from tkinter import Tk, Frame, Label, Entry, Button, StringVar

from buttonNames import NAMES

class MainWindow:
    def __init__(self):
        print ('hello')
        self.root = Tk()
        
        self.calcFrame = Frame(self.root, bg = "yellow")
        self.answFrame = Frame(self.root, bg = "green")
        self.inptFrame = Frame(self.calcFrame, bg = "blue")
        self.buttFrame = Frame(self.calcFrame, bg = "pink")
        self.helpFrame = Frame(self.calcFrame, bg = "grey")
        
        self.stmtVar = StringVar()
        
        self.stmtEntry = Entry(self.inptFrame, textvariable = self.stmtVar)
        
        self.sknfBtn = Button(self.inptFrame, text = u"В СКНФ")
        self.sdnfBtn = Button(self.inptFrame, text = u"В СДНФ")
        self.deltBtn = Button(self.inptFrame, text = u"Сбросить", command = self.clearStmtEntry)
        
        Label(self.helpFrame, text = u'Я справка!').pack()
         
        self.calcFrame.grid(row=0, column=0)
        self.answFrame.grid(row=0, column=1)
        self.inptFrame.grid(row=0, column=0)
        self.buttFrame.grid(row=1, column=0)
        self.helpFrame.grid(row=2, column=0)
        
        self.stmtEntry.grid(row=0, column=0)
        
        self.sknfBtn.grid(row=0, column=1)
        self.sdnfBtn.grid(row=0, column=2)
        self.deltBtn.grid(row=0, column=3)
        
        i, j = 0, 0
        for key in NAMES:
            symbol, text = key, NAMES[key]
            b = Button(self.buttFrame,  
                   text = u"%s - %s" % (symbol, text))
            b.bind('<Button-1>', self.updateStmtEntry)
            b.grid(row=i, column=j)
        
            i += 1
            if i > len(NAMES)/2:
                i = 0
                j += 1
        print ("uyy")
        
    def clearStmtEntry(self):
        self.stmtVar.set("")
        
    def updateStmtEntry(self, event):
        d = event.widget.cget("text").split(' - ')[0]
        e = self.stmtVar.get()
        if len(e) > 20:
            pass
        else:
            self.stmtVar.set(e + d)
        
    def run(self):
        self.root.mainloop()
    
if __name__ == "__main__":
    mw = MainWindow()
    mw.run()