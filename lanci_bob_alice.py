import random
lanci_bob = [ random.randint(1,6) for _ in range(11)]
lanci_alice = [ random.randint(1,6) for _ in range(11)]
f = open("./risultatiDadi.txt","w")
for n in range(11):
    riga = str(f"{lanci_bob[n]}, {lanci_alice[n]}\n")
    f.write(riga)
f.close()
