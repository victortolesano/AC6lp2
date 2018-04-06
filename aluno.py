class Aluno:
        
    def __init__(self, nome='', email='', ra='', celular='', desconto=0.0, disciplinas=[]):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = disciplinas

    def getNome(self):
        return self.__nome        

    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getRA(self):
        return self.__ra

    def getCelular(self):
        return self.__celular

    def setCelular(self, celular):
        self.__celular = celular

    def getDesconto(self):
        return self.__celular

    def setDesconto(self, celular):
        self.__celular = celular

    def getDisciplinas(self):
        return self.__disciplinas

