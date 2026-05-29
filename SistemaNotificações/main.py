from models.notificador_email import NotificadorEmail
from models.notificador_sms import NotificadorSMS
from models.notificador_app import NotificadorApp
from services.central_notificacoes import CentralNotificacoes

# Criando a central
central = CentralNotificacoes()

# Criando os notificadores
email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

# Adicionando à central
central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

# Enviando mensagem para todos
central.enviar_para_todos("Sua aula começa em 10 minutos!")
