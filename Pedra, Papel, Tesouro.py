import random

pontos_user = 0
pontos_computador = 0

options = ['r' , 't' , 'p']


while True:
    user_choice = input('Escolha R(Pedra) / T(Tesoura) / P(Papel) ou Q para sair :').lower()

    if user_choice == 'q':
       break
    
    if user_choice not in options:
        continue
    
    computer_choice = random.randint(0, 2)
    #0=R, 1=T , 2=P
    computer_options = options[computer_choice]

    print('o computador escolheu:' + computer_options)    

    if user_choice == computer_options:
         print('Empate!')
    
    elif user_choice == 'r' and computer_options == 't':
         print('Você ganhou!')
         pontos_user = pontos_user + 1

    elif user_choice == 'p' and computer_options == 'r':
         print('Você ganhou!')
         pontos_user = pontos_user + 1

    elif user_choice == 't' and computer_options == 'p':
         print('Você ganhou!')
         pontos_user = pontos_user + 1

    else: 
         print('Você perdeu')
         pontos_computador = pontos_computador + 1

print('Sua pontuação:' + pontos_user)
print('Pontuação Computador' + pontos_computador)

if pontos_computador > pontos_user:
    print('Vitória!!')
elif pontos_computador == pontos_user:
    print('Empate!')
else:
    print('Você perdeu')

print('Tchau!')

   