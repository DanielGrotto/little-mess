#CABEÇALHO
print('=' * 50)
print('{:^50}'.format('PROJETO INTEGRADOR II-A'))
print('{:^50}'.format('UCS - Universidade de Caxias do Sul'))
print('{:^50}'.format('Aluno: Daniel Grotto'))
print('=' * 50)

#PERGUNTAS
print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
1 - texto
2 - variável
3 - uma caixa de sapatos
''')
resposta = input().lower()
if resposta == "1":
    print("Resposta incorreta. A resposta correta é a: alternativa 2")
    input('0 pontos')
elif resposta == "2":
    print("Resposta Correta!")
    NotaQ1=input('20 pontos') 
elif resposta == "3":
    print("Resposta Incorreta - A resposta correta é a: alternativa 2")
    input('0 pontos')
else:
    print("Você não escolheu uma alternativa válida")
    
input('''
Precione ENTER para a próxima questão''')

print('''
Próxima questão''')

print('''
Q2 - Qual a cor do céu numa manhã ensolarada?
1 - roxo
2 - azul
3 - cor de burro quando foge
''')
resposta = input().lower()
if resposta == "1":
    print(" Não :( - Resposta correta b ")
    input('0 pontos')
elif resposta == "2":
    print(" Correto!! :) ")
    NotaQ2=input('20 pontos')
elif resposta == "3":
    print(" Não seja bobinho! :( ")
    input('0 pontos')
else:
    print("Você não escolheu 1, 2 ou 3")
    

