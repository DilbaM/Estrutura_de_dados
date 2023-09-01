class aluno:
    def __init__(self, nome, nt1, nt2):
        self.nome = nome
        self.nt1 = nt1
        self.nt2 = nt2
        self.media = 0,0

    def calcular_media(self):
        self.media = float(self.nt1+self.nt2)/2
        return self.media

    def resultado(self):
            if self.media>=7:
                print("Aprovado")
            else:
                print("Reprovado")

    def mostrar_resultado(self):
        print(f"nome:{self.nome}")
        print(f"nota1:{self.nt1}")
        print(f"nota2:{self.nt2}")
        print(f"média:{self.media}")

aluno1 = aluno("Carol", 9.0, 8.0)
aluno2 = aluno("Dilba", 9.0, 8.0)
aluno3 = aluno("gostosa", 9.0, 8.0)

aluno2.calcular_media()
aluno2.mostrar_resultado()