print("Zadejte cislo:");
a = int(input());
b = [];
while a>0:
    b.append(a%10)
    a //= 10
for i in range(len(b)-1,-1,-1):
    print('|'+b[i]*'*');