# Nó para alocação de uma Fila
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# Classe que define uma Fila
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._tamanho = 0

    # inserir na fila
    def push(self, elem):
        """Insere um elemento na fila"""
        no = No(elem)
        if self.ultimo is None:
            self.ultimo = no
            self.ultimo.proximo = no
            self.ultimo = no

        if self.primeiro is None:
            self.primeiro = no

        self._tamanho = self._tamanho + 1

    # remover da fila
    def pop(self):
        """Remove o elemento do topo da pilha""" 
        if self._tamanho > 0:
            elem = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
            # faltou tratar este caso no vídeo #
            if self.primeiro is None:
                self.ultimo = None
            ####################################
            self._tamanho = self._tamanho - 1
            return elem
        raise IndexError("A fila esta vazia")

    # observar o primeiro da fila
    def peek(self):
        """Retorna o topo sem remover"""
        if self._tamanho > 0:
            elem = self.primeiro.dado
            return elem
        raise IndexError("A fila esta vazia")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._tamanho


    def __repr__(self):
        if self._tamanho> 0:
            r = ""
            ponteiro = self.primeiro
            while(ponteiro):
                r = r + str(ponteiro.dado) + " "
                ponteiro = ponteiro.proximo
            return r
        return "Empty Fila"

    def __str__(self):
        return self.__repr__()