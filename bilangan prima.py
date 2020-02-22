#Program untuk memeriksa bilangan prima atau bukan

bilangan = int(input("Masukkan bilangan: "))
if bilangan > 1:
    for i in range(2,bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "bukan merupaan bilangan prima")
            print(i, "kali",bilangan//i, "=", bilangan)
            break
    else:
        print(bilangan, "merupakan bilangan prima")
else:
    print(bilangan, "bukan merupakan bilangan prima")