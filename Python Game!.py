import os
import random

os.system('cls')



print('======================')
print('adivinhador de numeros')
print('======================')
print('versão early access 0,1')
print('======================')
print('adivinhe o numero')
print('')
print('escolha a quantidade de numeros')
quantidade= int(input())

numero = random.randint(1,quantidade)
print('')
print('o jogo começou')
print('')
print('adivinhe um numero de 1 ate', quantidade)
while True:
    adivinha= int(input())
 
    if adivinha > numero:
     print(' o numero e menor :D')
     print('')
    if adivinha < numero:
     print('o numero e maior :D')
     print('')
    if adivinha == numero:
     print('acertou :D')
     break
