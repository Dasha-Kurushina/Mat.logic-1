#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:30:20 2018

@author: dasha
"""

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

if __name__ == "__main__":
    print (parseInputString())