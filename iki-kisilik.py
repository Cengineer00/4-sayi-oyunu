def arti_eksi(asil_sayi):


    kontrol = True

    while kontrol:

        try:
            sayi = int(input("4 basamaklı bir sayı giriniz:"))
        except ValueError:
            print("This is not a whole number.")

        arti = 0
        eksi = 0

        if ((sayi < 10000) and (sayi > 999)):

            yardimci_sayi = str(sayi)
            yardimci_asil_sayi = str(asil_sayi)

            if(str(sayi)[0] == str(asil_sayi)[0]):
                arti += 1
                yardimci_asil_sayi = "a" + yardimci_asil_sayi[1:]
                yardimci_sayi = "b" + yardimci_sayi[1:]

            if (str(sayi)[1] == str(asil_sayi)[1]):
                arti += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0] + "a" + yardimci_asil_sayi[2:]
                yardimci_sayi = yardimci_sayi[0] + "b" + yardimci_sayi[2:]

            if (str(sayi)[2] == str(asil_sayi)[2]):
                arti += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0:2] + "a" + yardimci_asil_sayi[3:]
                yardimci_sayi = yardimci_sayi[0:2] + "b" + yardimci_sayi[3:]

            if (str(sayi)[3] == str(asil_sayi)[3]):
                arti += 1
                yardimci_asil_sayi = yardimci_asil_sayi[:3] + "a"
                yardimci_sayi = yardimci_sayi[:3] + "b"



            if (yardimci_sayi[0] == yardimci_asil_sayi[0]):
                eksi += 1
                yardimci_asil_sayi = "a" + yardimci_asil_sayi[1:]
            elif yardimci_sayi[0] == yardimci_asil_sayi[1]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0] + "a" + yardimci_asil_sayi[2:]
            elif yardimci_sayi[0] == yardimci_asil_sayi[2]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0:2] + "a" + yardimci_asil_sayi[3:]
            elif yardimci_sayi[0] == yardimci_asil_sayi[3]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[:3] + "a"

            if (yardimci_sayi[1] == yardimci_asil_sayi[0]):
                eksi += 1
                yardimci_asil_sayi = "a" + yardimci_asil_sayi[1:]
            elif yardimci_sayi[1] == yardimci_asil_sayi[1]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0] + "a" + yardimci_asil_sayi[2:]
            elif yardimci_sayi[1] == yardimci_asil_sayi[2]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0:2] + "a" + yardimci_asil_sayi[3:]
            elif yardimci_sayi[1] == yardimci_asil_sayi[3]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[:3] + "a"

            if (yardimci_sayi[2] == yardimci_asil_sayi[0]):
                eksi += 1
                yardimci_asil_sayi = "a" + yardimci_asil_sayi[1:]
            elif yardimci_sayi[2] == yardimci_asil_sayi[1]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0] + "a" + yardimci_asil_sayi[2:]
            elif yardimci_sayi[2] == yardimci_asil_sayi[2]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0:2] + "a" + yardimci_asil_sayi[3:]
            elif yardimci_sayi[2] == yardimci_asil_sayi[3]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[:3] + "a"

            if (yardimci_sayi[3] == yardimci_asil_sayi[0]):
                eksi += 1
                yardimci_asil_sayi = "a" + yardimci_asil_sayi[1:]
            elif yardimci_sayi[3] == yardimci_asil_sayi[1]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0] + "a" + yardimci_asil_sayi[2:]
            elif yardimci_sayi[3] == yardimci_asil_sayi[2]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[0:2] + "a" + yardimci_asil_sayi[3:]
            elif yardimci_sayi[3] == yardimci_asil_sayi[3]:
                eksi += 1
                yardimci_asil_sayi = yardimci_asil_sayi[:3] + "a"


            kontrol = False

        else:

            print("Tekrar giriniz..")

    return [arti, eksi]

def oyun(oyuncu1, oyuncu2):

    while True:

        print("1. Oyuncunun sırası")
        deneme1 = arti_eksi(oyuncu1)


        print ("Artı sayısı: {} \t Eksi sayısı: {}".format(deneme1[0], deneme1[1]))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("2. Oyuncunun sırası")
        deneme2 = arti_eksi(oyuncu2)

        print("Artı sayısı: {} \t Eksi sayısı: {}".format(deneme2[0], deneme2[1]))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


        if (deneme2[0] == 4 and deneme1[0] == 4):
            print("Aslındaaa berabere bitti .ss")
            break
        elif (deneme2[0] == 4):
            print("2. oyuncu kazandı hehe")
            break
        elif (deneme1[0] == 4):
            print("1. oyuncu kazandı hehe")
            break


error = False
a=1
b=2
while a==1 and not error:
    try:
        x2 = int(input("1. Oyuncu sayı girsin "))
    except ValueError:
        error = True
        print("This is not a number.")
        break

    if(x2<10000 and x2>999):
        a=0
    else:
        print("Tekrar giriniz.")

while b==2 and not error:
    try:
        x1 = int(input("2. Oyuncu sayı girsin "))
    except ValueError:
        error = True
        print("This is not a number.")
        break

    if (x1 < 10000 and x1 > 999):
        b = 0
    else:
        print("Tekrar giriniz.")

if not error:
    oyun(x1,x2)
