#outils de file
def nouvelle_file():
    return list()

def enfiler(f,e):
    f.append(e)

def defiler(f):
    return f.pop(0)

def file_vide(f): 
    return len(f) == 0

#outils de pile
def nouvelle_pile():
    return list()

def empiler(p, e):
    p.append(e)

def depiler(p):
    return p.pop()

def pile_vide(p):
    return len(p) == 0