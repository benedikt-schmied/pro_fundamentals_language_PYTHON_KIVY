'''
Created on 16.10.2018

@author: schmied
'''

from auxiliary import printer as pt
from auxiliary2 import plotter
class c_discon_fw_bootstrap():
    '''
    DisCon FW bootstrap
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.printer = pt.c_printer()
        self.plotter = plotter.c_plotter()
        
    def run(self):
        print(" ... running it ...")
        self.printer.run()
        self.plotter.run()
    
if __name__ == "__main__":
    
    l_discon_fw_bootstrap = c_discon_fw_bootstrap()
    l_discon_fw_bootstrap.run()
    