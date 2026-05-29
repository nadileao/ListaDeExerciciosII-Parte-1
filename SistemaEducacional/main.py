from models.video import Video
from models.podcast import Podcast
from models.texto_narrado import TextoNarrado
from services.plataforma import Plataforma

# Criando a plataforma
plataforma = Plataforma("EduPlay")

# Criando as mídias
v1 = Video("Introdução ao Python", 15, "1080p")
p1 = Podcast("Tecnologia na Educação", 40, "Prof. Carlos")
t1 = TextoNarrado("História da Computação", 20, "Português")

# Adicionando à plataforma
plataforma.adicionar_midia(v1)
plataforma.adicionar_midia(p1)
plataforma.adicionar_midia(t1)

# Listando e reproduzindo
plataforma.listar_midias()
plataforma.reproduzir_todas()
