#2. Menghitung nilai rata-rata seorang siswa dari siswa dari 5 mata pelajaran (IPA,IPS,MTK,English,Indonesia)
ipa = int(input("Masukan nilai IPA:"))
ips = int(input("Masukan nilai IPS:"))
mtk = int(input("Masukan nilai MTK:"))
english = int(input("Masukan nilai English:"))
indonesia = int(input("Masukan nilai Indonesia:"))

rata_rata_1 = (ipa + ips + mtk + english + indonesia) / 5

nilai = (ipa,ips,mtk,english,indonesia)

print(f"Rata-rata nilai seorang siswa dari 5 mata pelajaran adalah {rata_rata_1}")

# 3.Mengecek nilai lulus atau tidak lulus dengan Kritea
#  - Dinyatakan lulus, jika rata-rata dari semuanya lebih dari 75, atau
#  - Dinyatakan lulus, jika hanya 2 mata pelajaran yang nilainya di bawah 50, atau 
#  - MEndapatkan nilai sempurna (100) dari salah satu mata pelajaran 

nilai_di_bawah_50 = 2
if(ipa < 50):
    nilai_di_bawah_50 += 1
if(ips < 50):
    nilai_di_bawah_50 += 1
if(mtk < 50):
    nilai_di_bawah_50 += 1
if(english < 50):
    nilai_di_bawah_50 += 1
if(indonesia < 50):
    nilai_di_bawah_50 += 1
    
if (rata_rata_1 > 75):
    print("Lulus, karena rata-rata nilai lebih dari 75")
elif (nilai.count(100) >= 1):
    print("Lulus, karena mendapatkan nilai sempurna dari salah satu mata pelajaran")
elif (nilai_di_bawah_50 == 2):
    print("Lulus, karena hanya 2 mata pelajaran yang nilainya di bwah 50")
else : 
    print("Tidak Lulus")