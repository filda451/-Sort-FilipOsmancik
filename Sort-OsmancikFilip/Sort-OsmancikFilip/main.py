import random

#1. Vytvoření pole s 10 random přeházenými hodnotami od 0-100.
random_hodnota = [random.randint(0, 100) for random_hodnota in range (10)]
    
for hodnota in random_hodnota:
    print(hodnota)

#2. Vytvoření bubble sortu
    for i in range(len(numbers)):
    for j in range (len(numbers) - i - 1):
    if numbers [j] > numbers [j + 1]:
    numbers [j], numbers [j + 1] = number [j + 1], numbers[j]

#3. Vypsání výsledků
    print("Uspořádaní")
    for num in numbers:
        print(num)

#4. Vytvoření bogo sortu
