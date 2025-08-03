import random

class RedeNeural:
    def __init__(self, num_entradas, taxa_aprendizado=0.1, limiar=0.8):
        self.n = taxa_aprendizado
        self.limiar = limiar
        self.num_entradas = num_entradas
        self.v1k = [random.uniform(-0.5, 0.5) for _ in range(num_entradas)]
        self.v2k = [random.uniform(-0.5, 0.5) for _ in range(num_entradas)]
        self.w11 = random.uniform(-0.5, 0.5)
        self.w12 = random.uniform(-0.5, 0.5)

    def funcao_ativacao(self, y):
        return 1 if y > self.limiar else 0

    def aplicar(self, entrada):
        h1 = sum(self.v1k[i] * entrada[i] for i in range(self.num_entradas))
        h2 = sum(self.v2k[i] * entrada[i] for i in range(self.num_entradas))
        y = h1 * self.w11 + h2 * self.w12
        return self.funcao_ativacao(y)

    def treinar(self, entradas, desejados, epocas=1000):
        for epoca in range(epocas):
            erros = 0
            for entrada, desejado in zip(entradas, desejados):
                h1 = sum(self.v1k[i] * entrada[i] for i in range(self.num_entradas))
                h2 = sum(self.v2k[i] * entrada[i] for i in range(self.num_entradas))
                y = h1 * self.w11 + h2 * self.w12
                saida = self.funcao_ativacao(y)
                erro = desejado - saida
                if erro != 0:
                    erros += 1
                    for i in range(self.num_entradas):
                        self.v1k[i] += self.n * erro * entrada[i]
                        self.v2k[i] += self.n * erro * entrada[i]
                    self.w11 += self.n * erro * h1
                    self.w12 += self.n * erro * h2
            if erros == 0:
                break

    def print_modelo(self):
        print("Modelo atual:")
        print(f"w11 = {self.w11}")
        print(f"w12 = {self.w12}")
        for i in range(self.num_entradas):
            print(f"v1k[{i}] = {self.v1k[i]}")
            print(f"v2k[{i}] = {self.v2k[i]}")
