def formatar_duracao(minutos):
    horas = minutos // 60
    mins = minutos % 60
    if horas > 0:
        return f"{horas}h {mins}min"
    return f"{mins}min"
