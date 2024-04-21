import tkinter as tk
from tkinter import messagebox
from nltk.chat.util import Chat, reflections

pares_palmeiras = [
    [
        r"oi|olá|hey|hello",
        ["Olá!", "Oi!", "Opa! Avanti Palestra!"]
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é VerdãoBot! 🐷", "Eu sou o ColossalmeirasBot!"]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado! E você? Ansioso para falar sobre os títulos do Verdão?",
         "Estou ótimo e adoraria falar sobre os títulos principais do Palmeiras!"]
    ],
    [
        r"adeus|tchau",
        ["Tchau!", "Até mais!", "Até a próxima!"]
    ],
    [
        r"quais são os títulos do Palmeiras?",
        ["O Palmeiras é um dos clubes mais vitoriosos do Brasil. Aqui estão alguns dos seus principais títulos:",
         "- Copa Rio (Torneio Internacional de Clubes Campeões): 1951",
         "- Conmebol Libertadores: 1999, 2020 e 2021",
         "- Campeonato Brasileiro: 12 títulos na primeira divisão, incluindo 2016, 2018, 2022 e 2023",
         "- Copa do Brasil: 1998, 2012, 2015 e 2020",
         "- Campeonato Paulista: 25 títulos estaduais, com conquistas em diversos anos",
         "- Torneios Rio-São Paulo: 1933, 1951, 1965, 1993 e 2000"]
    ],
    [
        r"O palmeiras não tem mundial|O palmeiras tem mundial?",
        ["A Fifa entende que a Copa Rio de 1951 foi o primeiro torneio de clubes de nível mundial, independentemente do nome que a competição tinha. Então, sim, o Palmeiras tem mundial!!"]
    ],
            [
        r"quantos titulos o palmeiras tem?",
        ["Até o momento, o Verdão conquistou 54 títulos em sua história, contando os principais campeonatos que o clube já disputou."]
    ],
        [
        r".*",
        ["Desculpe, não entendi. Pode reformular a pergunta?",
         "Não tenho informações sobre isso. Pode tentar outra pergunta?"]
    ]
]

def responder():
    pergunta = entrada.get()
    resposta = chatbot_responder(pergunta)
    area_resposta.config(state=tk.NORMAL)
    area_resposta.delete(1.0, tk.END)
    area_resposta.insert(tk.END, resposta)
    area_resposta.config(state=tk.DISABLED)

def enviar_quando_enter(event):
    responder()

def chatbot_responder(pergunta):
    chat = Chat(pares_palmeiras, reflections)
    resposta = chat.respond(pergunta)
    return resposta

janela = tk.Tk()
janela.title("VerdãoBot")
janela.geometry("400x400")

imagem_bandeira = tk.PhotoImage(file="img/bandeira-italia.png")

label_bg = tk.Label(janela, image=imagem_bandeira)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

titulo = tk.Label(janela, text="VerdãoBot", font=("Arial", 20, "bold"), bg="white", fg="green")
titulo.pack(pady=10)

entrada = tk.Entry(janela, width=30, relief=tk.SUNKEN)
entrada.pack(pady=10)
entrada.bind("<Return>", enviar_quando_enter)

botao_enviar = tk.Button(janela, text="Enviar", command=responder, bg="white", fg="green")
botao_enviar.pack(pady=5)

area_resposta = tk.Text(janela, width=50, height=15, state=tk.DISABLED, bg="white")
area_resposta.pack(pady=10)

janela.mainloop()