from random import randint, choice

def createFirstpopulation(quantidadeDaspopulacoes):
    listFirstpopulation = []
    for individuo in range(quantidadeDaspopulacoes):
        listFirstpopulation.append((randint(0,255), randint(0,255), randint(0,255)))
    return listFirstpopulation

def populationCheckandSelect(populacao, rgbIdeal):

    def getRankingpopulation(populacao, rgbIdeal):
        ranking = []
        for individuo in populacao:

            pontuacaoDesteindividuo = getPontuacao(rgbIdeal, individuo)

            if pontuacaoDesteindividuo < 0: pontuacaoDesteindividuo *= -1

            ranking.append((pontuacaoDesteindividuo, individuo))

        ranking.sort(reverse=True)

        return ranking

    listaDeescolha = []

    ranking = getRankingpopulation(populacao, rgbIdeal)

    for place in range(len(populacao)):
        for i in range(place):
            listaDeescolha.append(place)

    return (ranking[choice(listaDeescolha)][1], ranking[choice(listaDeescolha)][1])

def crossOverandMutation(pais):
    #Cross Over:
    pai1 = pais[0]
    pai2 = pais[1]

    new_individuo = [choice([pai1, pai2])[0], choice([pai1, pai2])[1], choice([pai1, pai2])[2]]
    #new_individuo = [int((pai1[0]+pai2[0])/2), int((pai1[1]+pai2[1])/2), int((pai1[2]+pai2[2])/2)]

    #Mutation:
    if  randint(1, 100) > 98:
        new_individuo = ((randint(0, 255), randint(0, 255), randint(0, 255)))
    else:
        new_individuo = [new_individuo[0] - randint(-4,4), new_individuo[1] - randint(-4,4), new_individuo[2] - randint(-4,4)]

    #Checks:
    i=0
    for atribute in new_individuo:
        if atribute < 0:
            new_individuo[i] = 0
        elif atribute > 255:
            new_individuo[i] = 255
        i += 1

    return tuple(new_individuo)

def defineNewgeneration(quantidadeDaspopulacoes, pais, filho):
    new_population = list(pais)[::]
    new_population.append(filho)
    for individuo in range(quantidadeDaspopulacoes - 3):
        new_population.append(crossOverandMutation(pais))
    return new_population

def getPontuacao(ideal, individuo):
    atributo1 = ideal[0] - individuo[0]
    atributo2 = ideal[1] - individuo[1]
    atributo3 = ideal[2] - individuo[2]

    if atributo1 < 0:
        atributo1 = atributo1 * -1
    if atributo2 < 0:
        atributo2 = atributo2 * -1
    if atributo3 < 0:
        atributo3 = atributo3 * -1

    soma = atributo1 + atributo2 + atributo3

    return round((soma / len(individuo)), 2)

def hasColision(area1, area2):
    area1ponto1 = area1[0]
    area1ponto2 = [area1[1][0], area1[0][1]]
    area1ponto3 = [area1[0][0], area1[1][1]]
    area1ponto4 = area1[1]
    area2ponto1 = area2[0]
    area2ponto2 = [area2[1][0], area2[0][1]]
    area2ponto3 = [area2[0][0], area2[1][1]]
    area2ponto4 = area2[1]
    if (area2ponto1[0]>=area1ponto1[0]) and (area2ponto1[1]>=area1ponto1[1]) and (area2ponto1[0]<=area1ponto4[0]) and (area2ponto1[1]<=area1ponto4[1]):
        return True
    elif (area1ponto2[0]>=area2ponto1[0]) and (area1ponto2[1]>=area2ponto1[1]) and (area1ponto2[0]<=area2ponto4[0]) and (area1ponto2[1]<=area2ponto4[1]):
        return True
    elif (area1ponto1[0]>=area2ponto1[0]) and (area1ponto1[1]>=area2ponto1[1]) and (area1ponto1[0]<=area2ponto4[0]) and (area1ponto1[1]<=area2ponto4[1]):
        return True
    elif (area2ponto2[0]>=area1ponto1[0]) and (area2ponto2[1]>=area1ponto1[1]) and (area2ponto2[0]<=area1ponto4[0]) and (area2ponto2[1]<=area1ponto4[1]):
        return True

    return False
