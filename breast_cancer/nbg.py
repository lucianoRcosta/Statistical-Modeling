import numpy as np

# Função para calcular os parâmetros do Naive Bayes Gaussiano
def calcular_parametros(x, y):
    classes = np.unique(y)
    parametros = []

    for classe in classes:
        x_classe = x[y == classe]
        media = np.mean(x_classe, axis=0)
        desvio_padrao = np.std(x_classe, axis=0)
        parametros.append((media, desvio_padrao))

    return parametros

# Função para calcular a probabilidade de uma amostra pertencer a uma classe
def calcular_probabilidade_classe(x, media, desvio_padrao):
    probabilidade = 1.0
    for i in range(len(x)):
        probabilidade *= (1 / (np.sqrt(2 * np.pi) * desvio_padrao[i])) * \
                        np.exp(-((x[i] - media[i]) ** 2) / (2 * (desvio_padrao[i] ** 2)))
    return probabilidade

# Função para fazer previsões
def prever(x, parametros):
    previsoes = []
    for x in x:
        probabilidades_classe = []
        for media, desvio_padrao in parametros:
            probabilidade = calcular_probabilidade_classe(x, media, desvio_padrao)
            probabilidades_classe.append(probabilidade)
        classe_prevista = np.argmax(probabilidades_classe)
        previsoes.append(classe_prevista)
    return previsoes