class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []

    def adicionar_notificador(self, notificador):
        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):
        print(f"\n Enviando para todos os canais:")
        for notificador in self.notificadores:
            notificador.notificar(mensagem)
