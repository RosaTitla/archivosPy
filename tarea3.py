#Cree una lista llamada j emociones que contenga cada palabra en palabras de emoción, texto que comience con la letra "j".
#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.

f = open("emotions.txt", "r")

listaEmocionesConJ=[]
for aline in f:
    listaEmociones = aline.split()
    #print(listaEmociones)
    for emocion in listaEmociones:
        if emocion.startswith('j'):
            listaEmocionesConJ.append(emocion)
print(listaEmocionesConJ)
