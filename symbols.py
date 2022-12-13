
class Symbols:
    def __init__(self):
        self.symbols = {}

    def addSymbol(self, symId, symType, line, value):
        self.symbols[symId] = {
            'name': symId,
            'type': symType,
            'line': line,
            'value': value
        }

    def getSymbol(self, symId):
        try:
            return self.symbols[symId]
        except KeyError:
            return None