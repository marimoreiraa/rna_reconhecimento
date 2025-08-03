# Reconhecimento de Desenhos com Rede Neural Artificial (RNA)

Este projeto implementa uma Rede Neural Artificial (RNA) simples, sem o uso de bibliotecas externas de aprendizado de máquina, para reconhecer padrões desenhados pelo usuário, como árvore, casa e boneco palito.

## Objetivo

Treinar manualmente uma RNA com algoritmo de retropropagação para reconhecer desenhos feitos em um canvas, com entrada convertida para uma grade (grid) de 10x10 ou 20x20.

## Tecnologias Utilizadas
- Python 3
- Tkinter (interface gráfica)
- Rede Neural implementada manualmente (sem bibliotecas como sklearn, keras, etc.)

## Estrutura de Arquivos
- main.py — Interface gráfica e fluxo da aplicação.
- rede_neural.py — Implementação da RNA com retropropagação.
- requirements.txt — Dependências mínimas.

## Como Executar
Pré-requisitos:
- Python 3.8 ou superior
- Tkinter instalado (no Linux: sudo apt-get install python3-tk)

### Instalação:
```bash  
pip install -r requirements.txt
```

### Execução:
```bash
python app.py
```

## Como Funciona
1. O usuário escolhe um padrão para desenhar (ex: árvore, casa, boneco).
2. Desenha no canvas clicando com o mouse.
3. Clica no botão "Classificar".
4. O sistema classifica se é ou não o padrão selecionado.
5. Se estiver errado, o usuário informa o correto e o sistema realiza o treinamento com retropropagação.
