import nltk
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

def chatbot_palmeiras():
    print("Olá! Sou o Chatbot temático sobre o Palmeiras. Como posso ajudá-lo hoje?")
    chat = Chat(pares_palmeiras, reflections)
    while True:
        try:
            entrada = input()
            resposta = chat.respond(entrada)
            print(resposta)
        except KeyboardInterrupt:
            break

chatbot_palmeiras()