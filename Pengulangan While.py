jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break
print ("total ngulang " + str(hitung))