'''
Created on 16.10.2018

@author: schmied
'''
from auxiliary.subaux import miniprinter


class c_printer():
    
    def __init__(self):
        self.miniprinter = miniprinter.c_miniprinter()
    
    
    def run(self):
        print("... running the submodule... ")
        self.miniprinter.run()