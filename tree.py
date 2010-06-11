##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
## Date: 28-05-2010
##
## tree.py
##
## LICENSED UNDER: GNU General Public License v2
##

import random as r

class Tree(object):
    def __init__ (self, children = None, content = None):
        """Initialise the Tree object"""
        if not children:
            self.children = []
        else:
            self.children = children
        if not content:
            self.content = ''
        else:
            self.content = content
   
    def clear(self):
        """Clear the Tree"""
        self.setChildren([])
        self.setContent('')
        
    def getContent(self):
        """Return content"""
        return self.content
    
    def setContent(self, content):
        """Set content"""
        self.content = content
        
    def getChildren(self):
        """Return all children"""
        return self.children
        
    def setChildren(self, children):
        """Set new children to Tree"""
        self.children = children
        
    def addChild(self, child, index=None):
        """Add new child to Tree"""
        if(self.children.__len__() > index and index > -1):
            
            self.setChildren(self.getChildren()[:index] + [child] + self.getChildren()[index:])
        else:
            self.children.append(child)
        
    def removeChild(self, index):
        """Remove a child specified by the index"""
        if(self.children.__len__() > index and index > -1):
            del self.children[index]
            
    def generateRandomTree(self, numberofvertices = 10):
        """Generates a random Tree"""
                    
        def maybeAddNode(t):
            """Recursively (and randomly) goes through the Tree and add a Node"""
            index = r.randint(0,len(t.getChildren()))
            if(index == len(t.getChildren())):
                index = r.randint(0,len(t.getChildren()))
                first = t.getChildren()[:index]
                last = t.getChildren()[index:]
                t.setChildren(first + [Tree(children = None, content = 'T')] + last)
            else:
                maybeAddNode(t.getChildren()[index])
        
        # Clear the Tree
        self.clear()
        # Add children to the tree        
        for i in range(numberofvertices-1):
            maybeAddNode(self)
