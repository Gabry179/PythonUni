class Person:
    #METODO COSTRUTTORE
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    #METODI DELLA CLASSE
    def prova(self):
        print("Questo e' un metodo della classe Person")

    #METODI SET
    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_eta(self, eta):
        self.eta = eta

    #METODI GET
    def get_nome(self):
        return self.nome
    
    def get_cognome(self):
        return self.cognome
    
    def get_eta(self):
        return self.eta

class sottoclasse(Person):
    def __init__(self, nome, cognome, eta, robasottoclasse):
        super().__init__(nome, cognome, eta)
        self.robasottoclasse = robasottoclasse
    
    #METODI
    def provasottoclasse(self):
        print("Sottoclasse")

    #GETTER E SETTER
    def get_robasottoclasse(self):
        return self.robasottoclasse

    def set_robasottoclasse(self, robasottoclasse):
        self.robasottoclasse = robasottoclasse

p = Person("Gabry", "F", "19")
p.set_nome("Ciao")
print(p.get_nome())
p2 = sottoclasse("Nome", "Cognome", "Eta", "Robe")
p2.prova()
#print(p.nome,p.cognome,p.eta)