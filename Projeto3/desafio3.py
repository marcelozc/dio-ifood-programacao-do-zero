class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):

        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"

        print(f"O {self.tipo} atacou usando {ataque}!")

guerreiro = Heroi("Marcelo", 31, "guerreiro")
mago = Heroi("Rafael", 31, "mago")
monge = Heroi("Ko", 31, "monge")
ninja = Heroi("Marcelo", 31, "ninja")

guerreiro.atacar()
mago.atacar()
monge.atacar()
ninja.atacar()
