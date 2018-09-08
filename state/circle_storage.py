circleDictionary = {}

def put(identifier, tuple):
    circleDictionary[identifier] = tuple

def get(identifier):
    return circleDictionary.get(identifier)

def empty():
    circleDictionary = {}