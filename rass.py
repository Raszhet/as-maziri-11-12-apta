tagam = "palau"
tagam_kal = 150.0
tagam_salmak = 200.0

paidalanyshy_tagamy = input("Sizdin suiikti tagamyńyz: ")
paidalanyshy_kal = float(input("Ol tagamnyń 100 g úshin kaloriasy: "))
try:
    paidalanyshy_salmak = float(input("Siz zheitin mólsher (g): "))
except ValueError:
    print("Сан енгізу керек!")
    paidalanyshy_salmak = 0
jalpy_kal = (paidalanyshy_kal * paidalanyshy_salmak) / 100
ortasha_kal = (tagam_kal + paidalanyshy_kal) / 2

print("\n--- As mәziri ---")
print(f"Negizgi tagam: {tagam}")
print(f"Sizdin tańdauyńyz: {paidalanyshy_tagamy}")
print(f"100 g kaloria: {paidalanyshy_kal}")
print(f"Zhegen mólsherińiz: {paidalanyshy_salmak} g")
print(f"Barlygy: {jalpy_kal:.1f} kkal")
print(f"Ortasha kaloria: {ortasha_kal:.1f} kkal")

def add_food(food_dict, name, calories):
    food_dict[name] = calories
    print(f"{name} мәзірге қосылды!")

def remove_food(food_dict, name):
    if name in food_dict:
        del food_dict[name]
        print(f"{name} өшірілді!")
    else:
        print("Ондай тағам жоқ.")

def find_food(food_dict, name):
    if name in food_dict:
        print(f"{name}: {food_dict[name]} ккал (100 г)")
    else:
        print("Ондай тағам жоқ.")
def show_foods_recursive(food_list, index=0):
    if index < len(food_list):
        print(f"{index + 1}. {food_list[index]}")
        show_foods_recursive(food_list, index + 1)

tagamdar = ["beshbarmaq", "palaý", "sushi", "tort", "kofe", "bauyrsaq", "steik", "omlet", "shai", "burger"]
print("\nTagamdar tizimi:", tagamdar)

biregei_tagamdar = set(tagamdar)
print("Biregei tagamdar:", biregei_tagamdar)

as_turleri = ("tańǵy as", "túski as", "keshki as")
print("\nQai asqa mәzir quraǵymyz?")
for nomer, as_turi in enumerate(as_turleri, 1):
    print(f"{nomer}. {as_turi}")

tańdau = int(input("Nómirin tańdańyz: "))

if tańdau == 1:
    print("Siz tańǵy as mәzirin tańdadyńyz.")
elif tańdau == 2:
    print("Siz túski as mәzirin tańdadyńyz.")
elif tańdau == 3:
    print("Siz keshki as mәzirin tańdadyńyz.")
else:
    print("Qate tańdau!")


izdeletin_tagam = input("\nQai tagamdy izdeisińiz? ").lower()
if izdeletin_tagam in biregei_tagamdar:
    print("Iә, mundaı tagam mәzirde bar!")
else:
    print("Ondaı tagam mәzirde joq.")

sipattama = "Búginǵi mәzirde dәmdi palaý, jumsaq bauyrsaq jáne qoıu kofe bar."
print("\nSipattama:", sipattama)

sózder = sipattama.split()
print("Sózder sany:", len(sózder))

zhańartylǵan_sipattama = sipattama.replace("kofe", "shai")
print("Zhańartylǵan sipattama:", zhańartylǵan_sipattama)

import os
def load_from_file():
    food_dict = {}
    if os.path.exists("tagamdar.txt"):
        with open("tagamdar.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, cal = line.strip().split(",")
                food_dict[name] = float(cal)
    return food_dict

def save_to_file(food_dict):
    with open("tagamdar.txt", "w", encoding="utf-8") as f:
        for name, cal in food_dict.items():
            f.write(f"{name},{cal}\n")
    print("Мәліметтер файлға сақталды!")


tagamdar_dict = load_from_file()
if not tagamdar_dict:
    tagamdar_dict = {
        "beshbarmaq": 320,
        "palaý": 290,
        "sushi": 150,
        "tort": 340,
        "kofe": 40,
        "bauyrsaq": 270,
        "steik": 310,
        "omlet": 154,
        "shai": 10,
        "burger": 330
    }


class Food:
    def __init__(self, name, calories, weight):
        self.name = name
        self.calories = calories
        self.weight = weight

    def total_calories(self):
        return (self.calories * self.weight) / 100

    def info(self):
        print(f"{self.name} | 100г: {self.calories} ккал | Салмақ: {self.weight} г | Жалпы: {self.total_calories():.1f} ккал")

class SweetFood(Food):
    def __init__(self, name, calories, weight, sugar):
        super().__init__(name, calories, weight)
        self.sugar = sugar

    def info(self):
        super().info()
        print(f"Қант мөлшері: {self.sugar} г")
print("\n--- 11 апта: OOP нәтижесі ---")

food1 = Food("Palau", 290, 200)
food1.info()

sweet1 = SweetFood("Tort", 350, 150, 40)
sweet1.info()



while True:
    print("\n--- Mәzir ---")
    print("1 - Tagamdar tizimi")
    print("2 - Tagam qosu")
    print("3 - tagam joiy")
    print("4 - Jalpy kaloria")
    print("5 - Shyǵu")
    print("6 - Malimetterdi failga saqtay")
    print("7 - Kaloria grafik (statistika)")
    

    try:
        tańdau_turi = input("Tańdauyńyz: ")
        if tańdau_turi not in ["1","2","3","4","5","6","7"]:
            raise ValueError("Қате таңдау! 1-ден 7-ге дейін сан енгізіңіз.")
    except ValueError as e:
            print(e)
            continue

    if tańdau_turi == "1":
        print("\nBarlyq tagamdar:")
        for ataý, kal in tagamdar_dict.items():
            print(f"{ataý}: {kal} kkal (100 g)")
    elif tańdau_turi == "2":
        ataý = input("Tagam ataýy: ")
        kal = float(input("100 g úshin kaloria: "))
        add_food(tagamdar_dict, ataý, kal)
    elif tańdau_turi == "3":
        ataý = input("Qai tagamdy joıasyz? ")
        remove_food(tagamdar_dict, ataý)
    elif tańdau_turi == "4":
        ataý = input("Qai tagamdy izdeisińiz? ")
        find_food(tagamdar_dict, ataý)
    elif tańdau_turi == "5":
        print("Baǵdarlama ayaqtaldy. Raqmet!")
        break
    elif tańdau_turi == "6":
        save_to_file(tagamdar_dict)
    elif tańdau_turi == "7":
        import numpy as np
        import matplotlib.pyplot as plt
        import os
        tagam_atalary = list(tagamdar_dict.keys())
        kalorialar = np.array(list(tagamdar_dict.values()))

        ortasha = np.mean(kalorialar)
        print(f"Орташа калория: {ortasha:.1f} ккал")

        plt.plot(tagam_atalary, kalorialar, marker='o')
        plt.axhline(ortasha, linestyle='--')
        plt.title("Tagamdar boıynsha kaloria dinamikasy")
        plt.xlabel("Tagam atawy")
        plt.ylabel("Kaloria (100 g)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print("Qate tańdau! Dúrys nómir engizińiz.")