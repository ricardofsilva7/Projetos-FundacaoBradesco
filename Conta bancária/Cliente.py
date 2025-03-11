class Cliente:
    def __init__(self, n, fone):                             # Método Construtor / 'self' é uma referência à própria instância do objeto. 
        
        self._nome = n                                       # "_" representa metodos e atributos PROTEGIDOS.
        self._telefone = fone

    #metodo get
    def get_nome(self):
        return self._nome
                                                           #Conceito de encapsulamento
    #meteodo set
    def set_nome(self, nome):
        self._nome = nome
