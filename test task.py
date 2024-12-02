bal = 0
duz_cavab = 0
sehv_cavab = 0
print("1) Birləşmiş Almaniyanın ilk federal kansleri :  A) K. Adenauer  B) L. Erxard  C) H. Koll D)  H. Ş. Şmidt")
cavab1 = input("cavab variantini daxil edin : ")
if cavab1 =="A":
    bal += 10
    duz_cavab += 1
else:
    sehv_cavab +=1
print("2)  Sultan Mehmet II Istanbulu neçənci ildə fəth etmişdir ? A) 1444 B) 1452 C) 1501 D) 1453")
cavab1 = input("cavab variantini daxil edin : ")
if cavab1 =="A":
    bal += 10
    duz_cavab += 1
else:
    sehv_cavab +=1
print("3) Dehli sultanlığının əsasını qoydu: A)Qiyasəddin Balaban B)Əlaəddin Hilçi C)Eltutmuş xan D)Qütbəddin Aybək")
cavab1 = input("cavab variantini daxil edin : ")
if cavab1 =="D":
    bal += 10
    duz_cavab += 1
else:
    sehv_cavab +=1
print("4) Osmanlı dövlətində sultandan sonra əsas vəzifəni kim tuturdu?  A)Baş vəzir B)Dəftərdar C)Paşa D)Sancaqbəyi E) Bəylərbəyi")
cavab1 = input("cavab variantini daxil edin : ")
if cavab1 =="C":
   bal += 10
   duz_cavab += 1
else:
    sehv_cavab +=1
print("Yekun misal:")
print("dogru cavab sayi: ",duz_cavab)
print("yanlis cavab sayi: ",sehv_cavab )
print("yekun bal: ",bal)
