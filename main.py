# Owners of this script in Alphabetical Order 
# Christian Di Maio & Giacomo Nunziati

import lark
from lark import Lark, Tree
import pydot
from Utils.Loader import Loader

if __name__ == "__main__":
    loader : Loader = Loader("./Test/test1.c")
    source : str = loader.load()
    print(">> Input string: ",source)

    grammar_parser : Lark = lark.Lark.open("grammar.lark", start="statement")
    result : Tree = grammar_parser.parse(source)
    print("\t *** Parse tree pretty print\n", result.pretty())

    print("\t saving PDF version of tree")
    graph = lark.tree.pydot__tree_to_graph(result, "TB")
    graph.write_pdf("grammar.pdf")