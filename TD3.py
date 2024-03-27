import unittest

class Tree:
    def __init__(self, symbol, *children):
        '''
        This function define 
        '''
        self.__symbol = symbol
        self.__children = children

    def label(self):
            return f"{self.__symbol}"
 
    def children(self):
        return self.__children
    
    def nb_children(self):
        cpt=0
        
        return len(self.__children)

    def child(self, i):
        return(self.__children[i])
    def is_leaf(self):
        return self.nb_children() == 0
    
    def depth(self):
         
         

if __name__=='__main__':
    
    tree1=Tree('a')
    tree2=Tree('a',Tree('b'))

    print(tuple(list(tree1)))
    print(tree1.label())
    print(tree2.children())
    #print(tree2.nb_children())
    #print(tree2.child(1))
    #print(tree1.is_leaf())