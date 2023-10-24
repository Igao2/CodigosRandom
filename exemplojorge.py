import random
def avalia(sequencia,matriz):
    distancia_atual = 0
    print("o caminho atual é:"+str(sequencia))
    for linha in range(len(sequencia)):
        
        for posicao in range(len(sequencia)):
            if linha+1<len(sequencia) and posicao==sequencia[linha+1]:
                print("A proxima posicao do caminho é:"+str(posicao))
                print("O valor até a posicao é:"+str(matriz[sequencia[linha]][posicao]))
                distancia_atual+=matriz[sequencia[linha]][posicao]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual    

def Solucao_inicial(tamanhomattriz):
    sequencia_atual = random.sample(range(tamanhomattriz),tamanhomattriz)
    return sequencia_atual



matriz = [[0,10,20,30],[10,0,40,50],[20,40,	0,60],[30,50,60,0]]


sol = Solucao_inicial(len(matriz))
avaliAa = avalia(sol,matriz)

print(sol)
print(avaliAa)