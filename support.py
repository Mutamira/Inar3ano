from arvore import ArvoreBinaria
from arvore import Arvore, No


def postorder_examplo_arvore():
    arvore = ArvoreBinaria()
    arvore = Arvore()
    n1 = No ("10")
    n2 = No ("5")
    n3 = No ("20")
    n4= No ("6")
    n5= No ("1")
    n6= No ("7")
    n6 = No ("2")
    n7 = No ("8")
    n8 = No ("3")
    n9 = No ("4")
    n10 = No ("9")
    n11 = No ("13")
    n12 = No ("19")
    n13 = No ("11")
    n14 = No ("15")
    n16 = No ("16")
    n17 = No ("17")
    n18 = No ("12")
    n19 = No ("14")
    n20 = No ("18")

    return arvore

if __name__ == "__main__":
    arvore = postorder_examplo_arvore()
    print("Percurso em pós ordem:")
    arvore.postorder_traversal()
    print("Altura: ", arvore.height())
