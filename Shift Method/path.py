import scipy as sp
import numpy as np
import math
import Basics
import mesh


def straighten(layer,mesh):
    #Changes all the edges in layer so that if the vector from a to b is regarded as forward, the inside of mesh is always to the right.
    newEdges = []
    for edge in layer:
        right = sp.cross(edge.dir[0],sp.array([0,0,1]))
        if mesh.contains(edge.a+0.01*right+0.5*edge.length*edge.dir[0]):
            newEdges.append(edge)
        else:
            newEdges.append(Basics.edge(edge.b,edge.a))
    return newEdge


#Untested

def order(layer):
    running = True
    activeEdge = layer[0]
    activeLoop = [activeEdge]
    loops = []
    while running:
        startEdge = activeEdge          #Save active Edge for later
        for edge in layer:
            if sp.array_equal(edge.a,activeEdge.b):
                layer.remove(edge)
                activeLoop.append(edge)
                activeEdge = edge
        if startEdge==activeEdge:
            #We must not have found any.
            loops.append(activeLoop)
            activeLoop = [layer[0]]
            layer = layer[1:]
        if len(layer)==0: running = False
    for loop in loops:
        if not sp.array_equal(loop[0].a,loop[-1].b):
            return 'Loop opening found at ' + str(loop[0].a)
    return loops
            

def shell(shellCount,mesh,loopList):
    #This function takes a flat layer which has been linearized and generates the shell paths.
    loopGroups = []
    for loop in loopList:
        loopShells = []     #A list of the shells produced for this loop
        activeShell = []    #A list of the edges produced for this shell
        for edge in loop:
        