from models.notificador import Notificador

class NotificadorSMS(Notificador):

    def notificar(self, mensagem):
        print(f" [SMS] Enviando mensagem: '{mensagem}'")
