import re
alfabeto = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
senha = input('Coloque a senha:')
combinacao = 0
adivinhar = ""
for char in senha:
    combinacao+=1
    if char in alfabeto:
       adivinhar+=char


print("Total de combinacoes"+str(combinacao))
print("Senha adivinhada:"+adivinhar)
