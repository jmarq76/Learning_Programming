import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frase = []
    for bloco in sentenca:
        frase = frase + re.split(r'[,:;]+', bloco)
    return frase

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    palavra = []
    for parte in frase:
        palavra = palavra + parte.split()
    return palavra

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    ab = 0
    i = 0
    for traco in as_a:
        if traco > as_b[i]:
            ab = ab + (traco - as_b[i])
        else:
            ab = ab + (as_b[i] - traco)
        i += 1
    Sab = ab / 6
    return Sab

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    conta_caracter = numero_caracteres(texto)
    sentenca = separa_sentencas(texto)
    conta_caracteres_sentenca = caracteres_bloco_texto(sentenca)
    frase = separa_frases(sentenca)
    conta_caracteres_frase = caracteres_bloco_texto(frase)
    palavras = separa_palavras(frase)
    wal = conta_caracter / len(palavras) #Tamanho médio de palavra
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = conta_caracteres_sentenca / len(sentenca) #Tamanho medio de sentença
    sac = len(frase) / len(sentenca)#Complexidade média de sentença
    pal = conta_caracteres_frase / len(frase) #Tamanho médio de frase
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    Sab = []
    i = 0
    n = 1
    for parte in textos:
        as_a = calcula_assinatura(parte)
        Sab.append(compara_assinatura(as_a, ass_cp))
    while n <= (len(Sab) - 1):
        if Sab[i] < Sab[n]:
            n += 1
        else:
            i += 1
            n = i + 1
        
    return (i + 1)

def numero_caracteres(texto):
    '''Essa função recebe um valor tipo str e devolve a quantidade total de carateres'''
    texto = re.split(r'[.!?,:;]+', texto)
    conta_caracter = 0
    for elemento in texto:
        freq = elemento.split()
        for caracter in freq:
            conta_caracter = len(caracter) + conta_caracter
    return conta_caracter

def caracteres_bloco_texto(bloco_texto):
    numero_caracteres = 0
    for parte in bloco_texto:
        numero_caracteres = len(parte) + numero_caracteres
    return numero_caracteres

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    print("\nO autor do texto", avalia_textos(textos, ass_cp), "está infectado com COH-PIAH")

def teste():
    compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0], [3.96, 0.05, 0.02, 22.22, 3.41, 0.0])
    calcula_assinatura('Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.')
    
