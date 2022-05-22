import random, string

output_file = "isimler.txt"
amount = int(input("\nKaç Tane Üretilecek?: "))
character_amount = int(input("Kaç Karakter Olacak?: "))

for i in range(amount):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))
    print(generated)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()


