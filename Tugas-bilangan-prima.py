
var = int(input(" BILANGAN PRIMA YANG DI INGINKAN : "))

for var in range (2,var+1) :

    prima = True

    for ch in range(2,var):

        if (var % ch == 0):

            prima = False

    if prima == True:

        print(var) 
    

print(TUGAS SELESAI)
