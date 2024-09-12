import random
i
maxfiy_son = random.randint(1, 100)
taxminlar_soni = 0

son = int(input("Son kiriting: "))
taxminlar_soni = taxminlar_soni + 1

if son == maxfiy_son:
    print("Yutdingiz!")
elif son < maxfiy_son:
    print("KIritilgan son kichik.")
else:
    print("Kiriting son katta.")


        



while son != maxfiy_son:
    son = int(input("Yana son kiriting: "))
    taxminlar_soni = taxminlar_soni + 1
    
    if son == maxfiy_son:
        print("Yutdingiz!")
    elif son < maxfiy_son:
        print("KIritilgan son kichik.")
    else:
        print("Kiriting son katta.")


print(f"Taxminlar soni {taxminlar_soni}ta")

