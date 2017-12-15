G=int(input("ANGKA AWAL : "))
H=int(input("BATAS BILANGAN PRIMA : "))
for x in range (G,H) :
    prima = True
    for ch in range(2,x):
        if (x % ch == 0):
            prima = False
    if prima == True:
        print(x)
        print("bilangan prima")
print("TUGAS SELESAI")
