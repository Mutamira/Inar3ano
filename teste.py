import random
from arvore import ArvoreBinariadeBusca

random.seed(10)

def random_arvore(tamanho=20):
    valores = random.sample(range(1, 1000), 20)
    arvore = ArvoreBinariadeBusca()
    for v in valores:
        arvore.inserir(v)
    return arvore

def exemplo_arvore():
    valores= [10, 5, 6, 7, 2, 4, 1, 8, 3, 9]
    arvore= ArvoreBinariadeBusca()
    for v in valores:
        arvore.inserir(v)
    return arvore

def extended_arvore():
    valores = [20, 13, 11, 16, 17, 18, 19, 15, 12, 14]
    arvore = ArvoreBinariadeBusca()
    for v in valores:
        arvore.inserir(v)
    return arvore

bst = extended_arvore()
bst.inorder_traversal()