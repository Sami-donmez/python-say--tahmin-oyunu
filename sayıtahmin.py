import random
kontrol=True
while(kontrol):
    kontrol2=True
    randsayi=random.randint(0,100)
    while(kontrol2):
        sayi=input("Lütfen tahmin giriniz.\n 0-Çıkış\n")
        if(len(sayi)!=0):#bosluk kontrolü yapıyoruz
            if(0<int(sayi)<100):#aralık kontrolu yaptık
                if(randsayi==int(sayi)):#sayıların eşitligini kontrol ediyoruz
                    print("tebrikler dogru tahmin\n")
                    break
                elif(randsayi<int(sayi)):
                    print("tahmin degerinizi küçültün lütfen\n")
                else:
                    print("tahmin degerinizi arttırın lütfen\n")
            else:
                print("sayı 0-100 arasında olmalıdır\n")
        else:
            print("boş deger giremezsiniz\n")
        
