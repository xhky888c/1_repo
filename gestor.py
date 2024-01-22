import random as rd

elements = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lon = int(input("Indica la longitud: "))

pw = ""

for i in range (lon):
    pw += rd.choice(elements)

print(pw)
