import string
f = open("text.txt", "w")
szo = "kodolt"
titkositott = ""
a =["A","Á","B","C","D"],["E","É","F","G","H"],["I","Í","J","K","L"],["M","N","O","Ó","Ö"],["Ő","P","Q","R","S"],["T","U","Ú","Ü","Ű"],["V","W","X","Y","Z"]
for i in szo:
    for e in range(len(a)):
        for k in range(len(a[e])):
            if i.upper() == a[e][k]:
                titkositott += (str(e+1)+str(k+1))
                # titkositott += ("["+str(e+1)+";"+str(k+1)+"]")
f.write(titkositott)
f.close()