# Owner of this script Alphabetical Order 
# Christian Di Maio & Giacomo Nunziati
import lark
import pydot

source = '{"a":1, "b":[1,2,3], "c": {"d": true}, "e":[[1,2,3],[4,5,6]], "f": "hello" }'
print(">> Input string: ",source)

json_parser = lark.Lark.open("json.lark",rel_to=__file__,start="value")
result = json_parser.parse(source)
print("\n*** Parse tree ***\n",result)
print("\n*** Parse tree pretty print\n", result.pretty())

print("\n saving PDF version of tree")
graph = lark.tree.pydot__tree_to_graph(result, "TB")
graph.write_pdf("json_parse_tree.pdf")

if __name__ == "__main__":
    print("Ciao")