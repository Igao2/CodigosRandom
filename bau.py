def verificar(ra,matriz):
    numrepetido = 0
    for i in range(ra):
        for j in range(ra):
            if j!=i and matriz[j] == matriz[i]:
                numrepetido+=1  
    return numrepetido            

matriz = ['Hayama Sushi Bar', 'BAR DO ZICO', "Geninho's Bar e Boliche", 'Bar Do Alexandre', 'Choperia Central', 'Bar Guimaraes', 'Mercearia Fernandes', 'Jardim Secreto Bar', 'Quintal Boteco', 'MOTORBIER CERVEJARIA E HAMBURGUERIA', 'PIT STOP 2', "Korno's bar", 'Bar do Beto B&B', 'Bar Do Capixaba', "Junior's CHOPERIA", 'Bar e Mercearia Clarice', 'Kiosque Trem Bao', 'Mercearia São José', 'Bar do Marcinho', 'Bar do betão o point dos amigos']
print(len(matriz))