from colorama import Fore #çıktıyı renklerdirmek için kullandığım kütüphane

x1,x2,B1 = 1,2,0    #1. Örnek Değerleri
x3,x4,B2 = 1,5,1    #2. Örnek Değerleri
x5,x6,B3 = 1,56,1   #3. Örnek Değerleri
w1,w2 = -1,2        #Ağırlıklar
esik_deger = 0.5    #Eşik Değer
learning_rate = 0.6 #Öğrenme Katsayısı

cıktı1,cıktı2,cıktı3= None,None,None
i = 1               #İterasyon Sayısı

while cıktı1 != B1 or cıktı2 != B2 or cıktı3 != B3:
    net1 = w1*x1+w2*x2
    if net1 <= esik_deger:
        cıktı1 = 0
        if cıktı1 == B1:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i+1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1=w1+learning_rate*x1
            w2=w2+learning_rate*x2
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)
    elif net1>esik_deger:
        cıktı1 =1
        if cıktı1 == B1:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1=w1-learning_rate*x1
            w2=w2-learning_rate*x2
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)


    net2 = w1 * x3 + w2 * x4
    if net2 <= esik_deger:
        cıktı2 = 0
        if cıktı2 == B2:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i + 1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1 = w1 + learning_rate * x3
            w2 = w2 + learning_rate * x4
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)
    elif net2 > esik_deger:
        cıktı2 = 1
        if cıktı2 == B2:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i, Fore.CYAN, "\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1 = w1 - learning_rate * x3
            w2 = w2 - learning_rate * x4
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)


    net3 = w1 * x5 + w2 * x6
    if net3 <= esik_deger:
        cıktı3 = 0
        if cıktı3 == B3:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i + 1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1 = w1 + learning_rate * x5
            w2 = w2 + learning_rate * x6
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net<=Eşik Değer\n Çıktı = 0")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)
    elif net3 > esik_deger:
        cıktı3 = 1
        if cıktı3 == B3:
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i, Fore.CYAN, "\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.BLUE,"Ağırlıklar değitirilmedi. w1=", w1, "w2=", w2)
        else:
            w1 = w1 - learning_rate * x5
            w2 = w2 - learning_rate * x6
            print(Fore.LIGHTWHITE_EX,"\n İTERASYON", i,Fore.CYAN,"\n Net>Eşik Değer\n Çıktı = 1")
            i = i + 1
            print(Fore.RED,"Ağırlıklar değitirildi. w1=",w1,"w2=",w2)

print(Fore.LIGHTGREEN_EX,"\n Öğrenme tamamlandı.\n Yeni Ağırlıklar w1=", w1,"w2=",w2)


