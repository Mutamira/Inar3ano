#Trabalho de INAR - 3 ano Informatica
#Rosario Mutamira, Lineida Simoes e Elisio Simao


from queue import Queue


RAIZ = "raiz"
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self, dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None

    # Percurso em ordem simétrica 
    def inorder_traversal(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            # parênteses são específicos para o nosso exemplo,
            # um percurso em ordem simétrica não precisa deles
            print('(', end='') 
            self.inorder_traversal_traversal(no.esquerda)
        print(no, end='')
        if no.direita:
            self.inorder_traversal_traversal(no.direita)
            print(')', end='')
    
    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA: https://youtu.be/QC8oiQnlYos
    def postorder_traversal(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.postorder_traversal(no.esquerda)
        if no.direita:
            self.postorder_traversal(no.direita)
        print(no)
    
    def height(self, no=None):
        if no is None:
            no = self.raiz
        hesquerda = 0
        hdireita = 0
        if no.esquerda:
            hesquerda = self.height(no.esquerda)
        if no.direita:
            hdireita = self.height(no.direita)
        if hdireita > hesquerda:
            return hdireita + 1
        return hesquerda + 1

    def inorder_traversal(self, no=None):
        if no is None:
            no = self.raiz
        if no.left:
            self.inorder_traversal(no.esquerda)
        print(no, end=' ')
        if no.direita:
            self.inorder_traversal(no.direita)


    def levelorder_traversal(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz

        queue = Queue()
        queue.push(no)
        while len(queue):
            no = queue.pop()
            if no.left:
                queue.push(no.esquerda)
            if no.direita:
                queue.push(no.direita)
            print(no, end=" ")


class ArvoreBinariadeBusca(ArvoreBinaria):
    
    def insert(self, valor):
        parente = None
        x = self.raiz
        while(x):
            parente = x
            if valor < x.dado:
                x = x.esquerda
            else:
                x = x.direita
        if parente is None:
            self.raiz = No(valor)
        elif valor < parente.dado:
            parente.esquerda = No(valor)
        else:
            parente.direita = No(valor)

    def search(self, valor):
        return self._search(valor, self.raiz)

    def _search(self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreBinariadeBusca(no)
        if valor < no.data:
            return self._search(valor, no.esquerda)
        return self._search(valor, no.direita)

   
    def min(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado

    def max(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.dado


    def remove(self, valor, no=RAIZ):
        # Se for o valor padrão, executa a partir da raiz
        if no == RAIZ:
            no = self.raiz
        # Se desceu até um ramo nulo, não há nada a fazer
        if no is None:
            return no
        # Se o valor for menor, desce à esquerda
        if valor < no.dado:
            no.esuqerda = self.remove(valor, no.esquerda)
        # Se o valor for maior, desce à direita
        elif valor > no.dado:
            no.direita = self.remove(valor, no.direita)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(no.direita)
                # Ao invés de trocar a posição dos nós, troca o valor
                no.dado = substitute
                # Depois, remove o substituto da subárvore à direita
                no.direita = self.remove(substitute, no.direita)

        return no
        
    
    # def search(self, value, no=RAIZ):
    #     if no == RAIZ:
    #         no = self.raiz
    #     if no is None or no.data == valor:
    #         return BinarySearchTree(no)
    #     if value < node.data:
    #         return self.search(valor, no.esquerda)
    #     return self.search(valor, no.direita)
        
        

if __name__ == "__main__":
    arvore = ArvoreBinaria(10)
    arvore.raiz.esquerda = No(5)
    arvore.raiz.direita = No(20)

    print(arvore.raiz)
    print(arvore.raiz.direita)
    print(arvore.raiz.esquerda)

