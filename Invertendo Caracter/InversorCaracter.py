print("--- Inversor de palavras ---")

d = input("Digite uma palavra:")

c = []

i= ''


for l in d:
   
    c.append(l)


t = len(c) - 1


while t >= 0:
    i += (c[t])
    t -= 1

print("Palavra invertida: ")
print(i)