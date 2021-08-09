import random


def arti_eksi_cozucu(asil_sayi, sayi):

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


    return [arti, eksi]



def cozucu(bilinmeyen):

    global a
    tur_sayisi = 0

    tur_sayisi += 1
    durum = arti_eksi_cozucu(bilinmeyen, 1023)
    if (durum[0] == 4):
        a = tur_sayisi
        print("\n Sonuç:", 1023, "\t Tur sayısı: ", tur_sayisi)
        return (1023)

    if (durum[0] >= 2):
        a=1
    else:
        a=0

    tur_sayisi += 1
    durum2 = arti_eksi_cozucu(bilinmeyen, 4567)
    if (durum2[0] == 4):
        a = tur_sayisi
        print("\n Sonuç:", 4567, "\t Tur sayısı: ", tur_sayisi)
        return (4567)

    if a == 1:
        kosul3 = 8913
    elif a == 0:
        kosul3 = 8945

    tur_sayisi += 1
    durum3 = arti_eksi_cozucu(bilinmeyen, kosul3)
    if (durum3[0] == 4):
        a = tur_sayisi
        print("\n Sonuç:", kosul3, "\t Tur sayısı: ", tur_sayisi)
        return (kosul3)

    liste = []

    for i in range(1000, 10000):
        i_durum = arti_eksi_cozucu(i, 1023)
        i_durum2 = arti_eksi_cozucu(i, 4567)
        i_durum3 = arti_eksi_cozucu(i, kosul3)

        if(i_durum[0] == durum[0] and i_durum[1] == durum[1] and i_durum2[0] == durum2[0] and i_durum2[1] == durum2[1] and i_durum3[0] == durum3[0] and i_durum3[1] == durum3[1]):
            liste.append(i)



    while True:
        x = random.choice(liste)

        tur_sayisi += 1
        x_durum = arti_eksi_cozucu(bilinmeyen, x)
        if(x_durum[0] == 4):
            a=tur_sayisi
            print("\n Sonuç:", x,"\t Tur sayısı: ", tur_sayisi)
            return(x)

        for element in liste:
            element_durum = arti_eksi_cozucu(element, x)

            if(x_durum[0] != element_durum[0] or x_durum[1] != element_durum[1]):
                liste.remove(element)

        if(len(liste) == 1):
            a=tur_sayisi
            print("\n Sonuç:", liste[0],"\t Tur sayısı: ", tur_sayisi)
            return(liste[0])



