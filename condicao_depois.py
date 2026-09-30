MEDIA_MINIMA = 7
MEDIA_MINIMA_COM_ATESTADO = 6
FREQUENCIA_MINIMA = 75


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# --- Condições extraídas ---
def tem_frequencia_suficiente(frequencia):
    return frequencia >= FREQUENCIA_MINIMA


def tem_nota_suficiente(media, tem_atestado):
    return media >= MEDIA_MINIMA or (media >= MEDIA_MINIMA_COM_ATESTADO and tem_atestado)


def esta_aprovado(media, frequencia, tem_atestado):
    return tem_frequencia_suficiente(frequencia) and tem_nota_suficiente(media, tem_atestado)


# --- Ramos extraídos ---
def resultado_aprovacao(media, frequencia):
    return "Aprovado", f"Parabéns! Média {media:.1f} e frequência {frequencia}%."


def resultado_reprovacao(media, frequencia):
    if not tem_frequencia_suficiente(frequencia):
        return "Reprovado por falta", f"Frequência de {frequencia}% abaixo do mínimo de {FREQUENCIA_MINIMA}%."
    return "Reprovado por nota", f"Média {media:.1f} abaixo do mínimo exigido."


# --- Função principal, agora legível como uma frase ---
def calcular_situacao(n1, n2, n3, frequencia, tem_atestado):
    media = calcular_media(n1, n2, n3)

    if esta_aprovado(media, frequencia, tem_atestado):
        return resultado_aprovacao(media, frequencia)
    return resultado_reprovacao(media, frequencia)


print(calcular_situacao(8, 7, 6, 80, False))   # ('Aprovado', ...)
print(calcular_situacao(5, 6, 7, 90, True))    # ('Aprovado', ...)
print(calcular_situacao(9, 8, 9, 60, False))   # ('Reprovado por falta', ...)