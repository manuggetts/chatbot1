from PyQt5.QtWidgets import QApplication, QMainWindow
from nltk.chat.util import Chat, reflections
from design import Ui_VerdaoBot
from PyQt5.QtGui import QIcon

pares_palmeiras = [
    [
        r"oi|olá|hey|hello",
        ["Olá!", "Oi!", "Opa! Avanti Palestra!"]
    ],
    [
        r"palmeiras",
        ["Palmeiras é o maior time do Brasil!", "Avanti Palestra!"]
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

class VerdãoBot(QMainWindow, Ui_VerdaoBot):
    def __init__(self, *args, **kwargs):
        super(VerdãoBot, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(QIcon('img/projeto5.jpg'))

        self.Resposta.setReadOnly(True)

        self.Enviar.clicked.connect(self.responder)
        self.Texto.returnPressed.connect(self.responder)

    def responder(self):
        pergunta = self.Texto.text()

        self.Texto.clear()

        resposta = self.chatbot_responder(pergunta)

        self.Resposta.append('Usuário: "' + pergunta + '"\n\nVerdãoBot: ' + resposta)

    def chatbot_responder(self, pergunta):
        chat = Chat(pares_palmeiras, reflections)
        resposta = chat.respond(pergunta)
        return resposta

if __name__ == '__main__':
    app = QApplication([])

    bot = VerdãoBot()
    bot.show()

    app.exec_()