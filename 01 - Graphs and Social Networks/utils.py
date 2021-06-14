import matplotlib.pyplot as plt
import IPython
from IPython.display import SVG
from IPython.display import HTML
from IPython.display import display
import networkx as nx
import StringIO
from networkx.drawing.nx_pydot import read_dot
from networkx.drawing.nx_pydot import from_pydot
from networkx.drawing.nx_agraph import to_agraph
import pydot

'''
Utility Functions 
'''
def toGraph(g):
    G = nx.Graph()
    for n in g:
        for n2 in g[n]:
            G.add_edge(n,n2)
    return G

def nM(d):
    '''Generate node labeler from dictionary''' 
    def m(n, N):
        if n in d:
            N.attr['label'] = n + ' ' + str(d[n])
    return m
def eM(d):
    '''Generate edge labeler from dictionary''' 
    def m(e, E):
        if e in d:
            E.attr['label'] = str(d[e])
    return m

def pathColorer(path, color='red'):
    '''Generate edge colorer from path''' 
    pairs = set()
    for i in range(len(path)-1):
        l = sorted([path[i], path[i+1]])
        pairs.add((l[0],l[1]))
    def colorer(e,E):
        e = tuple(sorted(e))
        if e in pairs:            
            E.attr['color'] = color
    return colorer

def pathNumberer(path):
    '''Generate edge numberer from path''' 
    pairs = dict()
    for i in range(len(path)-1):
        l = tuple(sorted([path[i], path[i+1]]))
        pairs[l]=i+1
    def colorer(e,E):
        e = tuple(sorted(e))
        if e in pairs:            
            E.attr['label'] = str(pairs[e])
    return colorer

def strongWeakEdges():
    '''Label edges with strength''' 
    def labeler(e,E):
        if float(E.attr['weight']) <=0.6:            
            E.attr['label'] = "w"
        else:
            E.attr['label'] = "s"
    return labeler

def draw(G, mapping=None, emapping=None):
    '''draw graph with node mapping and emapping''' 
    A=to_agraph(G)
    A.graph_attr['overlap']='False'
    if mapping:
        if isinstance(mapping, dict):
            mapping = nM(mapping)
        for n in A.nodes():
            mapping(n, A.get_node(n))
    if emapping:
        if isinstance(emapping, dict):
            emapping = eM(emapping)
        for e in A.edges():
            emapping(e, A.get_edge(e[0],e[1]))
    A.layout()
    output = StringIO.StringIO()
    A.draw(output, format='svg')
    return SVG(data=output.getvalue())
    
def fromDot(s):
  P_list = pydot.graph_from_dot_data(s)
  return from_pydot(P_list[0])

def bfs(graph, start):
    ''' 
    In breadth first search discovered nodes are attached to the end of the queue. Thus,
    the algorithm first searches through all nodes in the same distance from the start node.
    The dictionary visited maps each node to a visiting time and thus keeps track of
    which node was already visited.
    '''
    visited, queue = dict(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited[vertex] = len(visited)
            queue.extend(set(graph[vertex]) - set(visited))
    return visited

def dfs(graph, start):
    ''' 
    Depth-first-search in graph starting from the node 'start'.  
    The algorithm starts at start and explores as far as possible along each branch before backtracking.
    '''
    visited, stack = dict(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited[vertex] = len(visited)
            stack.extend(set(graph[vertex]) - set(visited.keys()))
    return visited

def isStrong(e):
    return float(e['weight']) > 0.5

def neighborPairs(G, a):
    return [ (n1,n2) for n1 in G['A'] for n2 in G['A'] if n1<n2 ]

def answer(b):
    if b:
        return HTML("<h2 style='color: green;'>Correct</h2>")
    else:
        return HTML("<h2 style='color: red;'>Incorrect</h2>")
