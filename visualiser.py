##
## Authors: Kim Lundsteen Juncher and Brian Soborg Mathiasen
## Insitute of Computer Science, Copenhagen University, Denmark
##
## Date: 28-05-2010
##
## visualiser.py
##
## LICENSED UNDER: GNU General Public License v2
##

import matplotlib.pyplot as plt
import networkx as nx

##
## This part contains functions for visualising graphs!
##
class Visualiser:

    def __init__(self, obj, objtype):
        """ Contains all initialisations needed for the visualiser, this method
        is invoked implicitly."""
        plt.ion()
        self.obj = obj
        self.objtype = objtype
        self._g = nx.Graph()
        self._oldgvertices = []
        self._oldgedges = []
        self._pos = {}

    def visualise(self, **args):
        def trying(arg, default):
            if arg in args:
                return args[arg]
            return default
        def graphVis():
            figNum = trying('figNum', 0)
            markEdges = trying('markEdges', [])
            markVertices = trying('markVertices', [])
            savefig = trying('savefig', None)
            savefig_format = trying('savefig_format', 'png')
            vertexLabels = trying('vertexLabels', None)
            
            """ Method to invoke the visualisation of the content of the
            structure."""
            #check API of input obj, certain methods must be available
            objmethods = dir(self.obj)
            if not '__subconstruct__' and 'getEdges' and 'getVertices' \
            and 'clear' in objmethods:
                raise AttributeError

#            if not '_g' in objmethods:
#                self.__subconstruct__()
                
            plt.figure(figNum, facecolor='white')
            plt.clf()
            plt.axis('off')
            self._g.clear()
            for vertex in self.obj.getVertices():
                self._g.add_node(vertex.getId())

            for edge in self.obj.getEdges():
                self._g.add_edge(edge.start_vertex,edge.end_vertex)
                
            if (not self._oldgvertices and not self._oldgedges) or \
                (not self._oldgvertices == self._g.nodes() or \
                 not self._oldgedges == self._g.edges()):
                self._pos = nx.spring_layout(self._g)

            self._oldgvertices = self._g.nodes()
            self._oldgedges = self._g.edges()

            if not markVertices and not markEdges:
                nx.draw_networkx_nodes(self._g, self._pos, node_color='#557A66')#, edge_color='#272E2E')
                nx.draw_networkx_edges(self._g, self._pos)#, edge_color='#272E2E')
                nx.draw_networkx_labels(self._g, self._pos, labels=vertexLabels)
    #            nx.draw_networkx_edge_labels(self.G, self._pos, edge_labels=vertexLabels)
    # drawing edge labels are only available from networkX 1.1 and beyond
            else:
                unmarkedVertices = list(set(self._g.nodes()).difference(markVertices))
                unmarkedEdges = list(set(self._g.edges()).difference(markEdges))

                nx.draw_networkx_nodes(self._g, self._pos, nodelist=unmarkedVertices, node_color='#557A66')#, vertex_size=700)
                nx.draw_networkx_nodes(self._g, self._pos, nodelist=markVertices, node_size=700, node_color='#9ed95e')
                # E82B1E <- roed sort trae
                nx.draw_networkx_edges(self._g, self._pos, edgelist=unmarkedEdges)#, edge_color='#272E2E')#, width=6)
                nx.draw_networkx_edges(self._g, self._pos, edgelist=markEdges,width=6)#, edge_color='#272E2E')

                nx.draw_networkx_labels(self._g, self._pos, labels=vertexLabels)

            if savefig:
                plt.savefig(savefig, format=savefig_format)

        def treeVis():
            '''Visualize the tree'''
            # extract function arguments from parent arg '**args'
            figNum = trying('figNum', 0)
            markVertices = trying('markVertices', None)
            withLabels = trying('withLabels', False)
            vertexLabels = trying('vertexLabels', None)
            structured = trying('structured', False)
            colorMap = trying('colorMap', None)
                        
            def getEdges(t,p=-1,num=0):
                '''Return list of edges for drawing the tree'''
                if(p != -1):
                    edges = [(p,num)]
                else:
                    edges = []
                this = num
                for child in t.getChildren():
                    if(child != None):
                        edges += getEdges(child,this,num+1)
                        p,num = edges[-1]
                return edges
            
            ### START - Functions used for calculating a more intelligent positioning of the tree's nodes        
            def fam(tree):   
                '''Returns a list with the number of familymembers on each level below the given root.'''        
                res = []
                if(tree.getChildren() == []):
                    return res
                else:
                    for child in tree.getChildren():
                            res.append(fam(child))                  
                    addedRes = addList(res)
                    return [len(tree.getChildren())] + addedRes

                    
            def getPercentage(tree):
                '''Calculates how much space a given child should recieve, to draw a nice tree'''
                #Get the family of all children
                lst = []
                for t in tree.getChildren():
                    lst.append(fam(t))
                tmp = []
                totals = addList(lst)
                for i in range(0,len(lst)):
                    tmp.append(1.0/float(len(lst)))
                    for j in range(0,len(lst[i])):
                        tmp[i] += float(lst[i][j])/(float(totals[j]))
                totL = len(totals);
                if(totL <= 0):
                    for i in range(0,len(lst)):
                        tmp[i] = 1.0/float(len(lst))
                    return tmp            
                else:
                    for i in range(0,len(lst)):
                        tmp[i] = tmp[i]/float(totL+1)
                    return tmp 
                    
            def addList(lst):
                """Returns a list with the sum of the values 
                for every index in the Lists 
                given a List of Lists with integers"""
                tmp = []
                for l in lst:
                    for i in range(0,len(l)):
                        if(len(tmp)>i):
                            tmp[i] += l[i]
                        else:
                            tmp.append(l[i])
                return tmp

            def getPosAndObjectLists(tree,num=0, ph=0, pw=0, space=1):
                """Returns a position dictionary, 
                a list with the node Ids,
                a dictionary with labels
                and the id of the last added node.
                The positions are calculated trying to draw a nice looking tree"""   
                d = {num:(pw,ph)}
                labels = {num:tree.getContent()}
                nodeList = [num]
                edge = pw-(space/2.0)
                
                #Calculate the percentage(width) each child should recieve in the tree
                perc = getPercentage(tree)
                c = 0
                #Calculate positions for all getChildren(), and family recursively
                for t in tree.getChildren():
                    l = float(space)*perc[c]
                    if(t != None):
                        num += 1
                        nList, res, resLabels, num = getPosAndObjectLists(t,num, ph-1, edge+(l/2.0), l)
                        nodeList += nList
                        c += 1
                        d.update(res)
                        labels.update(resLabels)                
                    edge += l
                return nodeList, d, labels, num

            ### END - Functions used for calculating a more intelligent positioning of the tree's nodes
            
            def getPosAndObjectListsStructured(tree,num=0, ph=0, pw=0, space=1):
                """Returns a position dictionary, 
                a list with the node Ids,
                a dictionary with labels
                and the id of the last added node.
                The positions are calculated trying to draw a more structured tree""" 
                d = {num:(pw,ph)}
                labels = {num:tree.getContent()}
                nodeList = [num]         
                spaceBuf = float(space)*0.05
                l = pw-(float(space)/2.0) + spaceBuf
                if(len(tree.getChildren()) > 0):
                    nodeSpace = (float(space)*0.9)/float(len(tree.getChildren()))
                else:
                    nodeSpace = (float(space)*0.9)
                for t in tree.getChildren():
                    l += nodeSpace/2
                    if(t != None):
                        num += 1
                        nList, res, resLabels, num = getPosAndObjectListsStructured(t,num, ph-1, l, nodeSpace)
                        nodeList += nList
                        d.update(res)
                        labels.update(resLabels)
                    l += nodeSpace/2
                return nodeList, d, labels, num

                                    
            # Start visualisation
            plt.figure(figNum)
            plt.clf()
            plt.axis('off')
            self._g.clear()
            # Calc position of nodes and edges
            '''Visualize the tree'''

            if(structured):
                lstOfNodes,totalPos, labels, lastAddedObject =\
                 getPosAndObjectListsStructured(self.obj)        
            else:
                lstOfNodes,totalPos, labels, lastAddedObject =\
                 getPosAndObjectLists(self.obj)
            e = getEdges(self.obj)
            # Add edges and nodes to nx.graph
            for i in lstOfNodes:
                self._g.add_node(i)
            for x,y in e:
                self._g.add_edge(x,y)
            # Draw the nodes
            if(colorMap):
                unspecifiedColors = [index for index in totalPos if index not in colorMap]
                if(markVertices == None):
                    # Don't mark any vertices
                    if(withLabels):                        
                        for colorIndex in colorMap:
                            nx.draw_networkx(self._g, totalPos, nodelist=[colorIndex],labels=labels,node_color=colorMap[colorIndex],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=unspecifiedColors,labels=labels,node_color='#272E2E',font_color='#FFFFFF')
                    else:
                        for colorIndex in colorMap:
                            nx.draw_networkx(self._g, totalPos, nodelist=[colorIndex],node_color=colorMap[colorIndex],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=unspecifiedColors,node_color='#272E2E',font_color='#FFFFFF')
                else:
                    # Mark specific vertices
                    unmarkedNodes = list(set(lstOfNodes) - set(markVertices))
                    unmarkedColored = list(set(unmarkedNodes) - set(unspecifiedColors))
                    unmarkedUnColored = list(set(unmarkedNodes) - set(unmarkedColored))
                    markedNodes = list(set(lstOfNodes) - set(unmarkedNodes))
                    markedNodesColored = list(set(markedNodes) - set(unspecifiedColors))
                    markedNodesUnColored = list(set(markedNodes) - set(markedNodesColored))
                    if(withLabels):
                        for index in unmarkedColored:
                            nx.draw_networkx(self._g, totalPos, nodelist=[index],labels=labels,node_color=colorMap[index],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=unmarkedUnColored,labels=labels,node_color='#272E2E',font_color='#FFFFFF')
                        for index in markedNodesColored:
                            nx.draw_networkx(self._g, totalPos, nodelist=[index],labels=labels,node_size=700,node_color=colorMap[index],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=markedNodesUnColored,labels=labels,node_size=700,node_color='#557A66',font_color='#FFFFFF')
                    else:
                        for index in unmarkedColored:
                            nx.draw_networkx(self._g, totalPos, nodelist=[index],node_color=colorMap[index],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=unmarkedUnColored,node_color='#272E2E',font_color='#FFFFFF')
                        for index in markedNodesColored:
                            nx.draw_networkx(self._g, totalPos, nodelist=[index],node_size=700,node_color=colorMap[index],font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=markedNodesUnColored,node_size=700,node_color='#557A66',font_color='#FFFFFF')
            
                
            else:
                if(markVertices == None):
                    # Don't mark any vertices
                    if(withLabels):
                        nx.draw_networkx(self._g, totalPos, nodelist=lstOfNodes,labels=labels,node_color='#272E2E',font_color='#FFFFFF')
                    else:
                        nx.draw_networkx(self._g, totalPos, nodelist=lstOfNodes,node_color='#272E2E',font_color='#FFFFFF')
                else:
                    # Mark specific vertices
                    unmarkedNodes = list(set(lstOfNodes) - set(markVertices))
                    markedNodes = list(set(lstOfNodes) - set(unmarkedNodes))
                    if(withLabels):
                        nx.draw_networkx(self._g, totalPos, nodelist=unmarkedNodes,labels=labels,node_color='#272E2E',font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=markedNodes,labels=labels,node_size=700,node_color='#557A66',font_color='#FFFFFF')
                    else:
                        nx.draw_networkx(self._g, totalPos, nodelist=unmarkedNodes,node_color='#272E2E',font_color='#FFFFFF')
                        nx.draw_networkx(self._g, totalPos, nodelist=markedNodes,node_size=700,node_color='#557A66',font_color='#FFFFFF')

        def listVis():
            """ Method to invoke the visualisation of the content of the structure."""
            figNum = trying('figNum', 0)
            def calcPos(lst):
                pos = {}
                labels = {}
                for i in range(0,len(lst)):
                    pos[i] = (i,0)
                    labels[i] = lst[i]
                return pos, labels

            plt.figure(figNum, facecolor='white')
            plt.clf()
            plt.axis('off')
            self._g.clear()
            if not positioning:
                positioning = calcPos
            for i in range(0,len(self)):
                self._g.add_node(i)
            pos, labels = positioning(self)

            nx.draw_networkx(self._g, pos, labels=labels,node_color='#557A66')

    #        nx.draw_networkx(self._G, pos, labels=labels,\
    #         node_color='#9ed95e')
            #nx.draw_networkx(self._G, pos2, nodelist=[3])
    #        nx.draw_networkx_nodes(self._G, pos, node_color='#557A66', node_shape='s')#, edge_color='#272E2E')
    #        nx.draw_networkx_labels(self._G, pos, labels=labels)

        if self.objtype.lower() == 'graph':
            graphVis()
        if self.objtype.lower() == 'tree':
            treeVis()
        if self.objtype.lower() == 'list':
            listVis()

    def clearVisualisation(self):
        """ Clears and closes the active visualisations"""
        self._pos = {}
        plt.close()


