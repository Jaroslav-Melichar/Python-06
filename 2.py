print("Hádej random číslo od 1 do 11 máš pouze 2 pokusy");
random = int(input());
import random
a = random.randint(1,11);
if random == a:
    print("Uhodl jsi");
else:
    print("neuhodl jsi máš ještě jeden pokus");
    pokus = int(input());
if random == a:
    print("Uhodl jsi");
else:
    print("neuhodl jsi");