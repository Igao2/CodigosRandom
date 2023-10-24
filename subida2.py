import random as rd
def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual


def sucessor(solucao,posicao):
    x = rd.randrange(0,len(solucao)-1)
    nova_solucao = solucao[:]
    for i in range(len(solucao)):
        if x==i:
            x=rd.randint(0,len(solucao)-1)
        if solucao[i]==posicao:
            a = nova_solucao[i]
            b = nova_solucao[x]
            nova_solucao[x] = a
            nova_solucao[i] = b
    return nova_solucao  


def subidaencostaestrela(solucaoinicial,matriz,tmax):
    t = 0
    curso_atual = solucaoinicial[:]
    valoratual = avalia(curso_atual,matriz)
    cidades = [0,1,2,5,5,4,5]
    
    for j in range(7):
        posicao = cidades[j]
        t = 0
        while True:
                
                print("T:"+str(t))
                print("Iteracao:"+str(j))
                novo_curso = sucessor(curso_atual,posicao)
                novo_valor = avalia(novo_curso,matriz)
                print("Curso atual:"+str(curso_atual))
                print("Valor atual:"+str(valoratual))
                print("Novo curso:"+str(novo_curso))
                print("Novo Valor:"+str(novo_valor))

                if novo_valor<=valoratual:
                    print("real")
                    if t>=tmax:
                         break
                
                    else:
                        t=t+1

                else:             
                    valoratual = novo_valor
                    curso_atual = novo_curso
                    t=0
                    
                    
               
        
    return curso_atual,valoratual


matriz = [[0,2,4,3,8,4],[5,0,3,5,6,3],[6,4,0,2,7,3],[4,4,6,0,6,2],[2,3,5,8,0,2],[3,3,6,6,7,0]]

solucaoinicial = [4,1,0,2,5,3]

curso,valor = subidaencostaestrela(solucaoinicial,matriz,3)
print(curso) 
