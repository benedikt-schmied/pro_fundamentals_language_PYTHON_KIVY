'''
Created on 16.10.2018

@author: schmied
'''

from auxiliary1 import printer

class c_plotter():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.printer = printer.c_printer()
    
    def run(self):
        print(">>>  plotter <<<")
        self.printer.run()
        