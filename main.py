# Owner of this script Alphabetical Order 
# Christian Di Maio & Giacomo Nunziati
import lark
import pydot
from Class.Loader import Loader

if __name__ == "__main__":
    loader : Loader = Loader("./Test/test1.json")
    source : str = loader.load()
    print(">> Input string: ",source)

    json_parser = lark.Lark.open("json.lark",rel_to=__file__,start="value")
    result = json_parser.parse(source)
    print("\n*** Parse tree ***\n",result)
    print("\n*** Parse tree pretty print\n", result.pretty())

  