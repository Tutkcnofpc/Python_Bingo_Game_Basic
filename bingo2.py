import math
import random
import string
import time

def elenen_kart(kartno):
    kartlar.remove(kartno)

#16 tane 1 ile 100 arası random sayı seçtirim oyunu oynatma kısmını yazacağım.
#def tombala():
#    for i in 100:

def tombala():
    for i in range(50):
        yenisayı()

def yenisayı():
    sayılar = []
    devam = input("Yeni sayı seç")
    if devam == "e":
        sayı = random.randint(1, 100)
        print(sayı)
        if sayı not in sayılar:
            sayılar.append(sayı)






#kartlar=["kart1","kart2","kart3","kart4","kart5","kart6","kart7","kart8","kart9"] if you want you can add new cards
kartlar=["kart1","kart2","kart3"]

for index in range(len(kartlar)):
    kisi=input("Oyuncu adını girin")
    kartno=(random.choice(kartlar))
    print(kartno)
    elenen_kart(kartno)
    print(kartlar)

if kartlar==[]:
    print("Kartlar dağıtıldı. OYUN BAŞLASIN!")
    tombala()