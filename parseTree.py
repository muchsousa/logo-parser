
class ParserTree:
    def __init__(self, tree):
        self.result = []

        return self.parse(tree)

    def parse(self, tree):
        name = tree.name

        if name == "program":
            self.result.append("")
        
        return 


    def  parseWrite(self, tree):
        return ""