import random
import string

try:
    while True:
        print("### ŞİFRE OLUŞTURUCU ###")
        print("*Bu program belirlediğiniz uzunluk aralığında rasgele şifre kombinasyonları üretir*")

        harfler = string.ascii_letters
        sayilar = string.digits
        harf_sayilar = harfler + sayilar

        while True:
            min_uzunluk_str = input("Minimum şifre uzunluğunu girin: ")
            if not min_uzunluk_str.isdigit():
                print("Lütfen sadece rakam kullanın.")
            else:
                min_uzunluk = int(min_uzunluk_str)
                if min_uzunluk < 4:
                    print("Minimum şifre uzunluğu en az 4 olmalıdır.")
                else:
                    break

        while True:
            max_uzunluk_str = input("Maksimum şifre uzunluğunu girin: ")
            if not max_uzunluk_str.isdigit():
                print("Lütfen sadece rakam kullanın.")
            else:
                max_uzunluk = int(max_uzunluk_str)
                if max_uzunluk < min_uzunluk:
                    print("Maksimum şifre uzunluğu minimum uzunluğun altında olamaz.")
                else:
                    break

        print("İŞLEMLER\n1-Sayısal şifre oluştur\n2-Harf şifre oluştur\n3-Sayı + Harf şifre oluştur\n0-Çıkış")

        secim = input("Yapmak istediğiniz işlemi girin: ")

        if secim == '0':
            print("Çıkış yapıldı..")
            break
        elif secim == '1':
            rasgele_sifre = ''.join(random.choice(sayilar) for _ in range(random.randint(min_uzunluk, max_uzunluk)))
        elif secim == '2':
            rasgele_sifre = ''.join(random.choice(harfler) for _ in range(random.randint(min_uzunluk, max_uzunluk)))
        elif secim == '3':
            rasgele_sifre = ''.join(random.choice(harf_sayilar) for _ in range(random.randint(min_uzunluk, max_uzunluk)))
        else:
            print("Geçersiz bir seçenek. Lütfen tekrar deneyin.")
            continue

        print("=========================================")
        print("OLUŞTURULAN ŞİFRE >>>", rasgele_sifre, "<<<")
        print("=========================================")
except:
    print("Bir hata oluştu!")
    print("Programı yeniden başlatın...")
