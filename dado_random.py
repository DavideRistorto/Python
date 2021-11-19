#simulare un gioco tra due dadi
import random

lancio_bob = random.randint(1,6)
lancio_alice = random.randint(1,6)
print(f"lancio di bob: {lancio_bob}   lancio di alice: {lancio_alice}")
if(lancio_bob>lancio_alice):
    print("bob ha vinto")
elif(lancio_bob<lancio_alice):
    print("ha vinto alice")
else:
    print("pareggio")

