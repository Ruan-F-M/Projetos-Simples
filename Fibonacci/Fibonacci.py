n1 = 0
n2 = 1

i = int(input("Insira um número para iniciar a Fibonacci: "))


print('Sequência de Fibonacci:')

print('{} -> {}'.format(n1, n2), end = '')

cont = 3

while cont <= i:

   n3 = n1 + n2

   print('-> {}'.format(n3), end = '')

   n1 = n2

   n2 = n3

   cont += 1

print('\nFIM')