class Studente:
    #METODO COSTRUTTORE
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.voto = list()
    
    def get_nome(self):
        return self.nome
    
    def get_cognome(self):
        return self.cognome
    
    def get_voto(self):
        return self.voto
    
    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def add_voto(self, voto):
        self.voto.append(voto)

    def get_media_voti(self):
        media = 0
        for i in self.voto:
            media += i
        media = media/len(self.voto)
        return media

p = Studente()
p.set_nome("Gabriele")
p.set_cognome("Franchina")
p.add_voto(8)
p.add_voto(10)
print(p.voto)
print(p.get_media_voti())