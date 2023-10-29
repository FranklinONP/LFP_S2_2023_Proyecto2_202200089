import graphviz
import os
import time

class arbolitoo:
    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot=graphviz.Digraph(comment=f"Graph{timestr}")
        self.contador=0
        self.dot.attr(
            "node",
            style='filled',
            fillcolor='white',
            fontcolor='red',
            shape='box'
        )
    
    def addNodo(self,valor):
        name=f"nodo{self.contador}"
        self.dot.node(name,valor)
        self.contador+=1
        return name
    
    def addArista(self,nodo1:str,nodo2:str):
        self.dot.edge(nodo1,nodo2)
        
    def graficarArbol(self):
        self.dot.render("Arbol de derivacion de Franklin Noj.dot")
        self.dot.save("Arbol de derivacion de Franklin Noj.dot")
        
    def lastNode(self):
        return f"nodo{self.contador-1}"
    
arbolito=arbolitoo()