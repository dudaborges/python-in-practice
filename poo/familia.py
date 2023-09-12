class Mae:
    nomeMae = "Shirlene"

class Pai:
    nomePai = "Wlamir"

class Filho(Mae,Pai):
    def informarPais(self):
        print(self.nomeMae, self.nomePai)

filho1 = Filho()
filho1.informarPais()