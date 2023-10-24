import random

def avalia(sequencia,matriz):
    distancia_atual = 0
    for j in range(len(sequencia)):
        for i in range(len(sequencia)):
            
            if j+1<len(sequencia) and i==sequencia[j+1]:
                distancia_atual+=matriz[sequencia[j]][i]
    distancia_atual += matriz[sequencia[-1]][sequencia[0]]
    return distancia_atual    

def subida(curso,max_iteracoes,matriz):
    curso_atual = curso[:]
    distancia_atual = avalia(curso_atual,matriz)
    print("primeira distancia:"+str(distancia_atual))
    n = 0
    for i in range(max_iteracoes):
        cidade_aleatoria = [1,0,2,3,2,4,5]
        novo_curso = curso_atual[:]
        n = random.randint(0,5)
        nova_distancia = 0
        for j in range(len(novo_curso)):
            if novo_curso[j] == cidade_aleatoria[i]:
                
                while n == j:
                     n = random.randint(0,5)

                novo = novo_curso[j]
                novo_curso[j] = novo_curso[n]
                novo_curso[n] = novo
                
                nova_distancia = avalia(novo_curso,matriz)
                    
             
                

        
        if nova_distancia<= distancia_atual:
            curso_atual = novo_curso
            distancia_atual = nova_distancia    
        c = []
        for x in range(len(novo_curso)):
            c.append(novo_curso[x]+1)    
        print("Iteracao:"+str(i)+"\n ValorAtual:"+str(nova_distancia)+"Atual:"+str(c))
        d= []
        for x in range(len(novo_curso)):
            d.append(curso_atual[x]+1)    
    return d,distancia_atual



def iniciar():
    matriz_distancias = [[0, 2, 4, 6, 8, 4], [7, 0, 3, 5, 6, 3], [6, 4, 0, 2, 1, 3], [4, 4, 6, 0, 2, 2], [2, 3, 12, 8, 0, 2], [3, 3, 1, 6, 7, 0]]
    sequencia_atual = [4, 2, 1, 0, 5, 3]

    print("Solucao inicial:"+str(sequencia_atual),"Tamanho:"+str(len(sequencia_atual)))
    curso,distancia= subida(sequencia_atual,7,matriz_distancias)
    return curso,distancia
curso,distancia = iniciar()
print(curso)
print(distancia)


    
    
    

