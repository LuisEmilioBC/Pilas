from Nodo import Nodo

class Pila:
    def __init__(self) -> None:
        self.cima = None
        
    def esta_vacia(self):
        return self.cima is None
    
    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cima = nuevo_nodo
        else: 
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
            
    def desapilar(self):
        if self.esta_vacia():
            print('La pila está vacía')
        else:
            valor = self.cima.valor
            self.cima = self.cima.siguiente
            return valor
        
    def ver_cima(self):
        if self.esta_vacia():
            print('La pila está vacía')
        else:
            return self.cima.valor
        
    def mostrar(self):
        if self.esta_vacia():
            print('La lista está vacía')
        actual = self.cima
        string = ''
        while actual:
            string += str(actual.valor)+'\n'
            actual = actual.siguiente
        return string
    
    def vaciar(self):
        while self.cima:
            self.cima =self.cima.siguiente
    
    def buscar(self, valor):
        actual = self.cima
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return
    
    def copiar(self):
        actual = self.cima
        pila_inversa=Pila()
        while actual:
            pila_inversa.apilar(actual.valor)
            actual = actual.siguiente
            
        actual=pila_inversa.cima
        pila = Pila()
        while actual:
            pila.apilar(actual.valor)
            actual = actual.siguiente
        return pila
    
    def ordenar_ascendente(self):
        i = self.cima
        while i is not None:
            j = self.cima
            while j.siguiente is not None:
                valor1 = j.valor
                valor2 = j.siguiente.valor
                if valor1 > valor2:
                    j.valor = valor2
                    j.siguiente.valor = valor1
                j = j.siguiente       
            i = i.siguiente
                    
                    
            
    def cantidad_elementos(self):
        contador = 0
        actual = self.cima
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador