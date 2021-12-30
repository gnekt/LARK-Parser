# Owners of this script in Alphabetical Order 
# Christian Di Maio & Giacomo Nunziati

import lark
from lark import Lark, Tree, Token
import pydot
from Utils.Loader import Loader

def clean_tree(tree: Tree):
    """Remove all rule leaves from the tree

    Args:
        tree (Tree): The input tree 

    Returns:
        // operation are inplace
    """
    if isinstance(tree, Token): return False
    if len(tree.children) == 0 and tree.data.type == "RULE":
        return True
    for idx,children in enumerate(tree.children):
        if clean_tree(children):
            del tree.children[idx]
        
    
if __name__ == "__main__":
    loader : Loader = Loader("./Test/test1.c")
    source : str = loader.load()
    print(">> Input string: ",source)

    grammar_parser : Lark = lark.Lark.open("grammar.lark", start="statement")
    result : Tree = grammar_parser.parse(source)
    print("\t *** Parse tree pretty print\n", result.pretty())

    clean_tree(result)
    print("\t saving PDF version of tree")
    graph = lark.tree.pydot__tree_to_graph(result, "TB")
    graph.write_pdf("grammar.pdf")