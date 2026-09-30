def calcular_situacao(n1, n2, n3, frequencia, tem_atestado):
    media = (n1 + n2 + n3) / 3

    if (media >= 7 and frequencia >= 75) or (media >= 6 and frequencia >= 75 and tem_atestado):
        resultado = "Aprovado"
        mensagem = f"Parabéns! Média {media:.1f} e frequência {frequencia}%."
    else:
        if frequencia < 75:
            resultado = "Reprovado por falta"
            mensagem = f"Frequência de {frequencia}% abaixo do mínimo de 75%."
        else:
            resultado = "Reprovado por nota"
            mensagem = f"Média {media:.1f} abaixo do mínimo exigido."

    return resultado, mensagem


print(calcular_situacao(8, 7, 6, 80, False))   # ('Aprovado', ...)
print(calcular_situacao(5, 6, 7, 90, True))    # ('Aprovado', ...)
print(calcular_situacao(9, 8, 9, 60, False))   # ('Reprovado por falta', ...)