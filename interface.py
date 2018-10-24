#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:17:35 2018

@author: dasha
"""
from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Text, END, W, N

from logic import parseInputString
from truths import Truths
from logic import make_SKNF, make_SDNF
from buttonNames import NAMESa
from buttonNames import NAMESb
from buttonNames import NAMESc

class MainWindow:
    def __init__(self):
        print ('hello')
        self.root = Tk()
        
        self.root.config(bg = "light green")
        
        self.calcFrame = Frame(self.root, bg = "light green")
        self.answFrame = Frame(self.root, bg = "green")
        self.inptFrame = Frame(self.calcFrame, bg = "light blue")
        self.buttFrame = Frame(self.calcFrame, bg = "light green")
        self.helpFrame = Frame(self.calcFrame, bg = "blue")
        
        self.stmtVar = StringVar()
        
        self.stmtEntry = Entry(self.inptFrame, textvariable = self.stmtVar)
        
        self.sknfBtn = Button(self.inptFrame, text = u"В СКНФ", command = self.toSKNF,  bg = "#a3d4ed")
        self.sdnfBtn = Button(self.inptFrame, text = u"В СДНФ", command = self.toSDNF,  bg = "#a3d4ed")
        self.deltBtn = Button(self.inptFrame, text = u"Сбросить", command = self.clearStmtEntry,  bg = "#9ac0d3")
        
        Label(self.helpFrame, text = u'1. Используя кнопки введите выражение. \n        2. Закончив данный процесс, можете выбрать, \nв какую форму Вы хотите его преобразовать, в СКНФ или в СДНФ.\n                3. Получив желанный результат - радуйтесь жизни.', bg = "#9bff87").pack()
         
        self.calcFrame.grid(row=0, column=0, sticky = N)
        self.answFrame.grid(row=0, column=1)
        self.inptFrame.grid(row=0, column=0)
        self.buttFrame.grid(row=1, column=0)
        self.helpFrame.grid(row=2, column=0)
        
        self.stmtEntry.grid(row=0, column=0)
        
        self.sknfBtn.grid(row=0, column=1)
        self.sdnfBtn.grid(row=0, column=2)
        self.deltBtn.grid(row=0, column=3)
        
        i, j = 0, 0
        
        
        for NAMES, BG in zip([NAMESa, NAMESb, NAMESc], ["#adff9b", "#adff7b", "#adff5b"]):
        
            for key in NAMES:
                symbol, text = key, NAMES[key]
                b = Button(self.buttFrame,
                       text = u"%s - %s" % (symbol, text),
                       bg = BG,
                       width = "38",
                       anchor = W)
    
                b.bind('<Button-1>', self.updateStmtEntry)
                b.grid(row=i, column=j)      
                i += 1
            j += 1
            if j > 1: 
                j = 1
            else:
                i =0
                
                
        self.outTable = Text(self.answFrame,height=40,width=50,font='Monospace 10')
        self.outTable.pack()
                
        print ("uyy")
        
    def clearStmtEntry(self):
        self.stmtVar.set("")
        
    def toSKNF(self):
        self.outTable.delete('1.0', END) 
        e = self.stmtVar.get()
        v = parseInputString(e)
        t = Truths(v['Var'])
        self.outTable.insert(1.0, t)
        F = make_SKNF(v)
        self.outTable.insert(END, "\n\n"+F)
            
    def toSDNF(self):
        self.outTable.delete('1.0', END) 
        e = self.stmtVar.get()
        v = parseInputString(e)
        t = Truths(v['Var'])
        self.outTable.insert(1.0, t)
        F = make_SDNF(v)
        self.outTable.insert(END, "\n\n"+F)

                
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