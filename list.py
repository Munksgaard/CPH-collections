##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
## Date: 28-05-2010
##
## list.py
##
## LICENSED UNDER: GNU General Public License v2
##

import random as r

class List(list):
    """ inherits the built-in list container and extend with new 
    functionality, such as visualise, generateRandomList, etc."""
    def generateRandomList(self, length=0, minvalue=0, maxvalue=20):
        """ Generates and occupies the structure with random elements."""
        if length == 0:
            length = r.randint(5,20)
            
        self.clear()
        for i in range(0,length):
            self.append(r.randint(minvalue,maxvalue))
        
   
    def clear(self): 
        """ Clears and empties the structure of elements """
        self = List()            
            
