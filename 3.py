print("Zadej heslo tak aby mělo : Nejméně jedno malé písmeno [a-z]  a jedno velké písmeno [A-Z].Nejméně jedna číslice [0-9].Nejméně jeden znak [$#@].Nejméně 6 znaků. Nejvíce 16 znaků.")
heslo = input();
import re
x = True
while x:
    if (len(heslo)<6 or len(heslo)>16):
        print ("Heslo musí mít nejméně 6 znaků a nejvíce 16 znaků.")
        break
    elif not re.search("[a-z]",heslo):
        print ("Heslo musí mít nejméně jedno malé písmeno [a-z].")
        break 
    elif not re.search("[A-Z]",heslo):
        print ("Heslo musí mít nejméně jedno velké písmeno [A-Z].")
        break
    elif not re.search("[0-9]",heslo):
        print ("Heslo musí mít nejméně jednu číslici [0-9].")
        break
    elif not re.search("[$#@]",heslo):
        print ("Heslo musí mít nejméně jeden znak [$#@].")
        break
    elif re.search("\s",heslo):
        print ("Heslo nesmí obsahovat mezery.")
        break
    else:
        print("Hodně dobré heslo");
        x=False
        break;