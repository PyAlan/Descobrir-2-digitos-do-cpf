cpf = input('CPF: ')    
b = 10 
maior = 0
dig1 = 0
dig2 = 0
for a in cpf:        
    a = int(a)  
    c = a * b
    b -= 1
    maior = maior + c 
    if b < 1:
        break
cal = 11 -((maior) % 11)

if cal > 9:
    dig1 = 0
else:
    dig1 = cal

dig1 = str(dig1)

novo = cpf + dig1

b = 11
maior2 = 0
for a in novo:        
    a = int(a)  
    c = a * b
    b -= 1
    maior2 = maior2 + c 
    if b < 1:
        break
cal = 11 -((maior2) % 11)

if cal > 9:
    dig2 = 0
else:
    dig2 = cal

dig2 = str(dig2)

novo_cpf = novo + dig2

print(f'Seu cpf é {novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:11]}')