import time as t
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma", 
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "LMAO": "Respuesta común a algo muy gracioso"
            }
            
print("¡Bienvenido!")
t.sleep(1)
print("Este diccionario funcionará para entender mejor el lenguaje utilizado en Internet.")
t.sleep(2.5)
for i in range(7):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esta palabra no está registrada")
