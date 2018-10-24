#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:30:20 2018

@author: dasha
"""
from truths import Truths

def parseInputString(inputString = "avb&(c⊕d)"):
    rez = {
            "Var":['a','b','c','d'],
            "Ops":[]}
    rez = {
    "Var":[],
    "Ops":[]}
    
    for s in inputString:
        if s in ['a','b','c','d']:
            rez["Var"].append(s)
        else:
            rez["Ops"].append(s)
  
    
    return rez

def make_SKNF(parsed_var):
    t = str(Truths(parsed_var['Var']))
    F = "F = "  
    for e in t.split("\n")[3:-1]:
        n = 0
        F += "("
        A = ""
        for m in e.split("|")[1:-1]:
            if m == " 1 ":
                A += "v¬"+parsed_var['Var'][n]
            else:
                A += "v"+parsed_var['Var'][n]     
            n += 1
        F += A[1:] + ")^"
        
    return F[:-1]

def make_SDNF(parsed_var):
    t = str(Truths(parsed_var['Var']))
    F = "F = "
    for e in t.split("\n")[3:-1]:
        n = 0
        A = ""
        for m in e.split("|")[1:-1]:
            if m == " 1 ":
                A += "⌐"+parsed_var['Var'][n]
            else:
                A += ""+parsed_var['Var'][n]     
            n += 1
        F += A + " v "
        
    return F[:-2]

if __name__ == "__main__":
    print (parseInputString())
    v = parseInputString("a + b+c+d")
    print (make_SKNF(v))
    print (make_SDNF(v))
    
