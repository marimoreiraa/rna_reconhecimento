import tkinter as tk
from tkinter import messagebox, ttk
from rede_neural import RedeNeural

class Bolinha:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class DesenhoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconhecimento de Desenho com RNA")

        self.canvas_size = 200
        self.grid_size = 10
        self.rna_por_classe = {
            "arvore": RedeNeural(100),
            "casa": RedeNeural(100),
            "boneco": RedeNeural(100)
        }

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.desenhar)

        self.bolinhas = []

        frame = tk.Frame(root)
        frame.pack()
        
        self.acertos = {classe: 0 for classe in self.rna_por_classe}
        self.erros = {classe: 0 for classe in self.rna_por_classe}
        self.contador_label = tk.Label(root, text="")
        self.contador_label.pack()
        self.atualizar_contador()

        tk.Label(frame, text="Padrão:").pack(side=tk.LEFT)
        self.padrao_var = tk.StringVar()
        self.padrao_var.set("arvore")
        self.combo = ttk.Combobox(frame, textvariable=self.padrao_var, values=list(self.rna_por_classe.keys()))
        self.combo.pack(side=tk.LEFT)

        tk.Button(frame, text="Classificar", command=self.classificar).pack(side=tk.LEFT)
        tk.Button(frame, text="Limpar", command=self.limpar_canvas).pack(side=tk.LEFT)

        self.status = tk.Label(root, text="")
        self.status.pack()

    def desenhar(self, event):
        r = 6
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="black", outline="")
        self.bolinhas.append(Bolinha(event.x, event.y))

    def get_entrada_grade(self):
        entrada = [0] * (self.grid_size * self.grid_size)
        cell_w = self.canvas_size // self.grid_size
        cell_h = self.canvas_size // self.grid_size
        for b in self.bolinhas:
            col = min(b.x // cell_w, self.grid_size - 1)
            row = min(b.y // cell_h, self.grid_size - 1)
            idx = int(row * self.grid_size + col)
            entrada[idx] = 1
        return entrada

    def classificar(self):
        entrada = self.get_entrada_grade()
        classe = self.padrao_var.get()
        rna = self.rna_por_classe[classe]
        resultado = rna.aplicar(entrada)

        if resultado == 1:
            resposta = messagebox.askyesno("Verificação", f"A RNA disse: É um(a) {classe}.\nVocê concorda?")
        else:
            resposta = messagebox.askyesno("Verificação", f"A RNA disse: NÃO é um(a) {classe}.\nVocê concorda?")

        print(f"Entrada: {entrada}")
        print(f"Classe selecionada: {classe}")
        print(f"Saída da RNA: {resultado}")

        if resposta:
            self.acertos[classe] += 1
            self.status.config(text="Acertou!")
        else:
            self.erros[classe] += 1
            confirm = messagebox.askyesno("Confirmação", f"Esse desenho era um(a) {classe}?")
            desejado = 1 if confirm else 0
            rna.treinar([entrada], [desejado], epocas=10)
            self.status.config(text="Treinado com resposta correta!")

        self.atualizar_contador()


    def limpar_canvas(self):
        self.canvas.delete("all")
        self.bolinhas.clear()
        self.status.config(text="")

    def atualizar_contador(self):
        texto = " | ".join([f"{classe} - Acertos: {self.acertos[classe]} / Erros: {self.erros[classe]}"
                            for classe in self.rna_por_classe])
        self.contador_label.config(text=texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = DesenhoApp(root)
    root.mainloop()
